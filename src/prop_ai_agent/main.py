#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from typing_extensions import Optional, List, Dict, TypedDict

from crewai.flow import Flow, listen, start

from crews.prop_crew.prop_crew import ProposalCrew

from dotenv import load_dotenv

load_dotenv()


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

    @start()
    def set_company_profile(self):
        profile = """
    About the Softmeets
When someone asks what we do softmeets Info Solutions, it’s tempting to point out our four-decade track record for helping to transform the world’s great companies into sharper, smarter, better versions of themselves. It’s true, our mission is to help management teams create such high levels of economic value that together we redefine our respective industries.

We work with top executives to help them make better decisions, convert those decisions to actions, and deliver the sustainable success they desire. For forty years, we’ve been passionate about achieving better results for our clients-results that go beyond financial and are uniquely tailored, pragmatic, holistic, and enduring.

We advise global leaders on their most critical issues and opportunities: strategy, marketing, organization, operations, technology, transformations and mergers & acquisitions, across all industries and geographies.

Our unique approach to traditional change management, called Results Delivery, helps clients measure and manage risk and overcome the odds to realize results.

Providing digital transformation, SaaS, Automation, Internet of Things, Artificial intelligence & Analytics technologies.
Webel IT Park (3rd Floor), Kalyanpur Satellite Township, Asansol – 713302, Dist – Paschim Bardhaman (W.B). India
+ (91) 9434 811 929, 0341-3500346
INFO@SOFTMEETS.COM

Trusted by our Government of India customers.
Trusted by our esteemed Government of India customers, we deliver reliable, innovative solutions tailored to meet critical
operational and strategic needs. Our commitment to excellence ensures robust performance, security, and compliance,
fostering enduring partnerships built on trust and proven success.
Our customers are Indian Railways, Indian Army, SAIL, Ministry of Communication, ICMR, West Bengal Housing Board, Chittaranjan Locomotive Works, and many more.

Our Partners are Microsoft, HP, Elnova
We are CMMI Level 5 certified and ISO 27001:2013, ISO 20000-1:2018, ISO 9001:2015 certified.

Our Mission is to Transform your entire business to innovative digital business process
Embrace cutting-edge automation, advanced analytics, and seamless integrations to optimize operations, improve decision-making, and deliver exceptional customer experiences.
Visit us at https://softmeets.com/
    """
        print("Setting Company Profile")
        self.state.company_profile = profile

    @listen(set_company_profile)
    def generate_company_info(self):
        print("Extracting company info")
        result = (
            ProposalCrew()
            .crew()
            .kickoff(inputs={"company_profile": self.state.company_profile})
        )

        print("Company info generated", result.raw)
        self.state.company_info = result.raw

    # @listen(generate_poem)
    # def save_poem(self):
    #     print("Saving poem")
    #     with open("poem.txt", "w") as f:
    #         f.write(self.state.poem)


def kickoff():
    proposal_flow = ProposalFlow()
    proposal_flow.kickoff()


def plot():
    proposal_flow = ProposalFlow()
    proposal_flow.plot()


if __name__ == "__main__":
    kickoff()
