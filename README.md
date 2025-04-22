# PropAgent AI - Business Proposal Generation Tool

## Framework & Tech Stack
- **Frontend:** Streamlit
- **Backend:** CrewAI
- **Vector Database:** ChromaDB (for retrieving stored proposal templates)
- **LLM:** OpenAI GPT models
- **Document Processing:** Python-docx, ReportLab
- **Data Processing:** Pandas

## Project Phases

### Phase 1: UI Development
- Implement a **sidebar menu** with two options: Freelancing Proposal (default) and Business Proposal.
- Display input fields:
  - **Freelancing Proposal:** "About You" and "Job Requirements"
  - **Business Proposal:** "About Your Business" and "Job Requirements"
- Add a button to generate proposals in **DOCX** and **PDF** formats.

### Phase 2: Proposal Generation Pipeline
- Design a **Prompting Strategy** for proposal generation:
  - If freelancer/business details are missing, model should prompt the user to provide them.
  - If job requirements are unclear, model should request clarification.
- Load **predefined proposal templates** from a template folder.
- Utilize **CrewAI’s LLM integration** to generate proposals dynamically.

### Phase 3: Document Generation
- Convert LLM-generated proposals into:
  - **DOCX format** using `python-docx`
  - **PDF format** using `ReportLab`

### Phase 4: Enhancements & Optimization
- Improve response validation for missing information.
- Implement caching for faster proposal retrieval.
- Fine-tune prompt engineering for better-quality proposals.

This structured approach ensures an AI-powered proposal generation tool tailored for freelancers and business owners. 🚀


## 🔧 Installation & Setup
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/arghads9177/prop-ai-agent.git
   cd prop-ai-agent
   ```

2. **Create a Virtual Environment** (Recommended)  
   ```bash
   conda create -p venv python==3.11
   conda activate venv/
   source env/bin/activate   # On Windows use: env\Scripts\activate
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit App**  
   ```bash
   streamlit run src/app.py
   ```

## 📖 Usage Guide
- Enter your business requirements in the chatbot.
- The bot retrieves relevant information from FAQs, past proposals, and pricing data.
- It calculates estimated costs based on structured pricing.
- Generates a customized business proposal in **DOCX/PDF format**.
- Download and share the proposal with clients.

## 🛠 Future Enhancements
- Integration with **GPT-4** for improved proposal writing.
- **Multi-language support** for international clients.
- **User authentication** to save and manage proposals.
- **API support** for integrating PropAgent AI with third-party apps.

## 🤝 Contributing
Contributions are welcome! Feel free to fork this repo, create a feature branch, and submit a PR.

## 📜 License
This project is licensed under the **GNU Open License**.

---
Made by [Argha Dey Sarkar](https://github.com/arghads9177/)

