#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from typing_extensions import Optional, List, Dict, TypedDict

from crewai.flow import Flow, listen, start


import streamlit as st
from io import BytesIO
from docx import Document
from crews.prop_crew.prop_crew import ProposalCrew
from docx import Document

import markdown2
import weasyprint
from dotenv import load_dotenv
from html2docx import html2docx
import datetime
import os

load_dotenv()

# Create a folder to store the proposals
os.makedirs("proposals", exist_ok=True)

# Generate filename with timestamp
timestamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
pdf_filename = f"proposals/proposal_{timestamp}.pdf"
docx_filename = f"proposals/proposal_{timestamp}.docx"

# Convert Markdown to DOCX
def get_docx(proposal):
    """Converts Markdown to DOCX using html2docx"""
    docx_stream = BytesIO()

    # Convert Markdown to HTML first
    html_content = markdown2.markdown(proposal)

    # Convert HTML to DOCX
    docx_bytes = html2docx(html_content, "Proposal")

    # Write to BytesIO
    docx_stream.write(docx_bytes.getvalue())
    docx_stream.seek(0)

    return docx_stream

# Convert Markdown to PDF Using WeasyPrint
def get_pdf(proposal):
    html_content = markdown2.markdown(proposal)
    pdf_stream = BytesIO()
    
    # Convert HTML to PDF
    pdf = weasyprint.HTML(string=html_content).write_pdf()
    pdf_stream.write(pdf)
    pdf_stream.seek(0)

    return pdf_stream


class ProposalState(BaseModel):
    company_profile: Optional[str] = None
    job_description: Optional[str] = None
    # Output from Company Profile Checker Agent
    company_info: Optional[Dict[str, str]] = None
    # Output from Job Description Researcher Agent
    job_analysis: Optional[Dict[str, str]] = None
    # Output from Proposal Writer Agent
    generated_proposal: Optional[str] = None


class ProposalFlow(Flow[ProposalState]):


    def set_input(self, company_profile: str, job_description: str):
        print("Setting Company Profile")
        self.state.company_profile = company_profile
        print("Setting Job Description")
        self.state.job_description = job_description

    @start()
    def generate_proposal(self):
        print("Extracting company info and job description and generating proposal")
        result = (
            ProposalCrew()
            .crew()
            .kickoff(inputs={"company_profile": self.state.company_profile, "job_description": self.state.job_description})
        )

        print("Generated Proposal", result.raw)
        self.state.generated_proposal = result.raw

    def get_proposal(self):
        return self.state.generated_proposal

# Streamlit app

st.set_page_config(page_title="AI Proposal Generator", layout="wide")

st.title("🧠 AI Proposal Generator using CrewAI")
st.markdown("Provide your company profile and job description to generate a well-structured business proposal.")

# Company Profile Input
company_profile = st.text_area("📋 Company Profile", height=200, placeholder="Paste your company profile here")

# Job Description Input
job_description = st.text_area("📄 Job Description (optional if uploading a file)", height=300, placeholder="Paste job description here")
uploaded_file = st.file_uploader("📎 Upload Job Description (PDF or Word)", type=["pdf", "docx"])

# Function to extract text from uploaded file
def extract_text_from_file(file):
    import PyPDF2
    if file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        return "\n".join([page.extract_text() for page in reader.pages])
    elif file.name.endswith(".docx"):
        doc = Document(file)
        return "\n".join([para.text for para in doc.paragraphs])
    return ""

# Run generation on button click
if st.button("🚀 Generate Proposal"):
    if not company_profile:
        st.warning("Please provide a company profile.")
    else:
        # Determine job description source
        jd_text = job_description
        if uploaded_file:
            jd_text = extract_text_from_file(uploaded_file)

        if not jd_text:
            st.warning("Please provide a job description or upload a file.")
        else:
            with st.spinner("Generating your proposal..."):
                try:
                    proposal_flow = ProposalFlow()
                    proposal_flow.set_input(company_profile, jd_text)
                    proposal_flow.kickoff()
                    result = proposal_flow.get_proposal()

                    if isinstance(result, dict) and "error" in result:
                        st.error(result["error"])
                    else:
                        st.success("✅ Proposal generated successfully!")
                        st.markdown(result, unsafe_allow_html=True)

                        # Download buttons for DOCX and PDF
                        # col1, col2 = st.columns(2)
                        # with col1:
                        #     st.download_button("Download as DOCX", get_docx(result), "proposal.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document")
                        # with col2:
                        #     st.download_button("Download as PDF", get_pdf(result), "proposal.pdf", "application/pdf")
                        # Save PDF
                        pdf_file = get_pdf(result)
                        with open(pdf_filename, "wb") as f:
                            f.write(pdf_file.getbuffer())

                        # Save DOCX
                        docx_file = get_docx(result)
                        with open(docx_filename, "wb") as f:
                            f.write(docx_file.getbuffer())

                        # Confirmation
                        st.info(f"📄 Proposal saved successfully!\n\n**PDF:** `{pdf_filename}`\n\n**Word:** `{docx_filename}`")
                except Exception as e:
                    st.error(f"❌ Something went wrong: {str(e)}")
