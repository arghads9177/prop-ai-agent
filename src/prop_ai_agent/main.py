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
    def set_input(self):
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

        print("Setting Job Description")
        job_description = """
        PREAMBLE TO SCHEDULE OF WORK (In conjunction with the schedule of quantities):
“INSTANT PROPOSAL CONSISTS OF PENALTY CLAUSE. BIDDERS ARE REQUESTED TO GO THROUGH THAT”
1.NAME OF WORK: Proposal to Upgrade Traffic Info System to Unified Rail Logistics System.
2. Salient Features:
i)
Upgradation of TRIS system on BSL native Cloud, no hardware required from vendor.
ii)
Integration with Indian Railways CRIS, FOIS, BSL ERP/SAP, IP based CCTV, Loco GPS system.
iii) Latest software framework, Webapp and Mobile app solution.
iv) Coverage to all operational and functional areas of Traffic department, Inward/Outward/Empty Railway
Yard, SWS, Tippler, Loading Bays, RMHP, CHP. BPSCL, etc.
v)
Viewing and logging of the latest information for reports, logbooks, and tracking of rake and wagon
vi)
movement. Includes automated & scheduled reporting with notifications via email, WhatsApp, and SMS.
Ensures long-term sustainability with future-proof architecture, portability, AI and IoT readiness, scalable
architecture and seamless integration capabilities.
3. DETAILED SCOPE OF WORK:
3.1 Introduction:
Bokaro Steel Plant (BSL), a leading steel manufacturer under SAIL, is expanding its production capacity from 5 million
tons (MT) to 8 MT. To support this growth, an efficient rail logistics system is crucial, handling on an average over 350
raw material rakes and 150 finished product rakes per month, covering more than 95% of BSL's logistics operations.
Currently, Traffic dept, BSL manages around 300 km of rail tracks, owns and operates around 57 locomotives, and
utilizes wagons from its own fleet, private vendors, and Indian Railways. Effective coordination is required between
external stakeholders (mines, Indian Railways, FOIS, CRIS, SAP) and internal units (RMHP, BF, SMS, CCS, loading units).
At present, these transactions are managed via the Traffic Info System (TRIS). The objective of this project is to upgrade
TRIS into a unified digital rail logistics solution, ensuring a seamless, technology-driven approach to logistics
management.
Also, as part of SAIL digital transformation and modernization strategy, this project aligns with the company's vision to
implement smart, automated solutions that enhances efficiency, tracking, transparency, and operational control. The
project aims to revolutionize its logistics framework, improved turnaround time, reduced demurrage, reducing manual
intervention, seamless integration with external business and enabling proactive decision-making.
3.2 Functional areas and Software Modules:
1.
External Wagon management:
Tracks and manages hired wagons from Indian Railways & private vendors for raw materials (iron ore, flux,
coal, pellet, iron material, FM, F/oil, Sulphur, scrap, coke, sinter etc) and finished product transportation
(primary steel product like HRC, CRC etc and secondary product like Pig iron, coke, slab, slag etc).
Operations include:
a. Inward Exchange Yard (IEY): Rake takeover, wagon fitness check (TXR), rake brake release, piloting.
b. Inside the Plant: Movement of all loaded and empty wagons.
c. Commercial Operations: Daily rake loading plan, loading bay details, Indenting / allotment, Dispatch
advice, forwarding notes, Railway receipts, SAP integration, rake hand over & made over with
railways.
d. Outward Exchange Yard (OEY): Rake formation and handover/takeover with Indian Railways.
e. Cost Optimization: Automatic detention and demurrage calculation to reduce penalties as per the
extant rail circular2.Internal Wagon management:
Manages in-plant wagons transporting hot metal, slag, and scrap, flue dust, sinter, coke, sand, slab LDS, mill
scale to optimize steel production. Key operations include
a. Blast Furnace: Hot metal and slag ladle transport Steel Melting Shops (SMS), PCM, Foundry shops
and slag disposal.
b. Steel Melting & CCS: Wagon requests, slab & scrap transfer, slag disposal.
c. Slag Dump Station & Central Traffic Control: Track ladle movement and manage derailments.
d. SSD (Scrap Disposal Section): Scrap collection and transfer to SSD.
e. Central station: Wagon movement for both PCM, sinter loading, mill scale wagon movement etc.
3.Loco and Wagon maintenance:
Responsible for maintaining Locos and Wagons. The department is involved in planning of maintenance
schedule for various equipment.
a. Maintenance Scheduling: Prepare equipment maintenance schedule, Monthly Dashboard
b. Internal Maintenance: Record Arrival, Pre-Check, Job Details, Consumables, Test, Delivery.
c. External Maintenance: Equipment record sent outside, Repair Bill and Payments to vendor
4.Permanent Way sections:
The Permanent Way department of BSL plans monthly maintenance of huge network of rail tracks.
a. Scheduled Maintenance: Monthly repair plans, track inspections.
b. Incident Handling: Track management, modifications, downtime requests.
c. Real-time Monitoring: Preventive maintenance alerts and optimization.
d. Shutdown and breakdown maintenance logbook
5.Field services section:
If there is a breakdown of locos or any other equipment in the field, this section comes in to picture.
a. Equipment Booking & Issue, Equipment Movement
b. Refuelling, Wagon Fitness, Dump car Movement
c. Optimizing usage of HSD and lubricants.
d. Incident Handling: Derailment management, modifications, downtime requests.
6.Document Archiving System:
A digital repository for critical business documents, including:
a. Circulars, Railway Receipts (RRs), Business Documents
b. Cloud Storage Integration: Google Drive/Dropbox for easy access.
c. Indexing & Search Features: Quick retrieval of key documents.
7.Traffic Control Section:
a. Traffic control reports for plant wide reporting
b. Electronic logbook for message exchanges with railways
8.Security, Administration, Roles and Policies:
Secure data access with controlled permissions for different user roles:
a. User Role Management: Define access based on job function.
b. Module-Specific Permissions: Restrict or allow dashboard visibility, data entry rights, and reporting
access.
c. Audit & Compliance Tracking: Logs user activity to maintain security standards.
d. Error and fault logging and reporting to Admin user.
3.3 Integration and support with external systems:
1.
2.
3.
4.
Automated data transaction API mechanism with FOIS, CRIS, Loco GPS system and SAP
Existing data sharing mechanism between SAP and TRIS.
Development APIs to provide data to various Plant info systems
Live and archived Feed from IP based CCTV cameras.5.
In case of API provider failure, an alternative transaction system must be available with near real-time data
synchronization once the API is restored.
3.4 Software features, requirement and specifications:
1. Conduct comprehensive field study and analyse existing software to design screens, reports, and data flow.
2. Vendor shall prepare a detailed Software Requirements Specification (SRS) and obtain approval from BSL.
3. Design a new PostgreSQL DB system with capacity to retain existing data and projections for next 20 years.
4. Enable database transactions via APIs with prefetching and caching.
5. Develop a web and mobile app information portal for data entry and access.
6. Implement role-based access and control with multi factor OTP authentication.
7. Provide live and historical data viewing with downloadable reports.
8. Generate detailed reports (Daily, Monthly, Cumulative, Summary) with analytics and insights.
9. Incorporate trends, graphs, and charts with real-time analytics and insights.
10. Enable event based scheduled reporting and notifications via email, WhatsApp, and SMS.
11. Deploy mobile apps on Google Play Store and Apple App Store.
12. Implement audit logging with selective matrix for accountability and clarity.
13. Display system and file processing errors in the UI for easy debugging.
14. Optimize for scalability with load balancing and failover mechanisms.
15. automated daily backup mechanism with a 30-day retention policy and disaster recovery (DR).
16. Latest open-source software and security standard ensuring no proprietary or licensing dependencies.
3.5 Deployment of solution:
1. Deployment shall be carried out exclusively on BSL native cloud, ensuring security compliance.
2. Maintain separate Development, Testing, and Production environments.
3. All source code development, backup must be conducted exclusively on BSL-provided systems.
4. The development priority of software modules (refer to 3.2) will be as per BSL’s requirements.
5. BSL retains full ownership of the developed source code and database.
6. Vendor must provide knowledge transfer of source code and database during development phase.
7. Conduct daily development reviews in coordination with BSL.
8. Testing and commissioning require prior approval for production downtime.
9. Vendor must accommodate customization/modifications during the contract validity and support period.
10. API and services for data and file transaction with FOIS, CRIS, SAP etc. will be essential part of the project.
11. Implement security audits, vulnerability assessments, and penetration testing.
12. Each UI page or screen (entry/view/report) in Web/Mobile will be considered as 1(one) quantity only.
13. Each UI page or screen should include data and design features as per BSL specifications only.
14. Filters, cases, selection etc. addition or modifications of feature within a page/report will be considered
part of the same page/report.
3.6 Training and Documentation:
1.
2.
3.
4.
The vendor must provide an SRS after the study phase and, upon testing and final commissioning, deliver a
comprehensive user manual, operating instructions, and detailed system architecture diagrams.
Submit detailed documentation covering data flow, execution flow, and integration details for all system
components, including Entry screen, Reports, APIs, Services, and Database components.
Conduct a minimum 7-day hands-on training program for operators and general users, covering:
a. System navigation and operations on the live solution.
b. Troubleshooting and basic issue resolution.
c. Best practices for system efficiency and security compliance.
Ensure post-deployment support and knowledge transfer to internal teams for ongoing maintenance and
optimization.4. Duration of Contract: 18 (Eighteen) months.
1.
Phase-1: 6 (Six) Months
a. Field study, analysis of existing software, development, deployment of solution.
b. Perform performance testing and validation of the solution.
2. Phase-2: 12 (Twelve) Months
a. Provide onsite and online support for the commissioned solution 24 hours of request.
b. Implement approved modifications or additions in solution as required, complete within mutually
agreed timeline.
5. Special Terms and Conditions:
All incidental items of work not shown or specified here but reasonably implied and found to be necessary for
successful completion of the objective of this project shall be deemed to be included in the scope of contractor at
no extra cost.
6. Safety Measures for Contractors:
The vendor has to strictly follow the safety guidelines of Bokaro Steel Plant. Any deviation for safety rule / guidelines
will attract penalty as pet the rule of Safety department of Bokaro steel plant.
7. Payment Term:
As per the quantity definition (refer to 3.5.11), the maximum allowable quantity under this contract is 200 during the
contract validity period. A quantity will be deemed complete and eligible for billing only upon BSL’s approval,
confirming its commissioning to the corresponding developed item.
1.
2.
3.
For Phase 1 (First 6 months): A minimum of 80% of the total quantity must be completed. The vendor may
raise invoices only for approved quantities, with a minimum billing threshold of 40 units.
During Phase 2 (Next 12 months): The remaining quantities will be allocated for modifications or new
additions to the commissioned solution (refer to 4.2.b).
Final Billing: If fewer than 200 quantities are approved by the end of the contract period, billing will be
limited to the approved quantity.
8. Penalty Clause:
1.
2.
Start of Work Order: The job must commence within 15 days from the date of issuance of the Work Order (WO).
a) The contractor must ensure:
I.
A complete and sufficient service group is deployed.
II.
Safety approvals and Gate passes are obtained.
b) If the contractor fails to meet these conditions:
III.
A penalty of ₹500 per day will be imposed for the first two weeks.
IV.
Thereafter, a penalty of ₹1,000 per day will be deducted from the RA bill for delays attributable
to the contractor
Milestone-Based Monthly Targets & Penalties:
a. Grace Period: No penalty for the first one month from the Work Order start date.
b. Milestone-Based Monthly Targets & Penalties:
MonthMinimum Approved Quantity Required (Monthly)
2nd Month
3rd Month
4th Month
5th Month
6th Month40
80
120
160
200
c.
Penalty Rupees per Unit
Shortfall
500
500
800
1000
1000
If the cumulative target is not met at the end of each month, the corresponding penalty per unit shortfall
will be deducted from the next RA bill.
    """
        self.state.job_description = job_description

    # @listen(set_input)
    # def generate_company_info(self):
    #     print("Extracting company info")
    #     result = (
    #         ProposalCrew()
    #         .crew()
    #         .kickoff(inputs={"company_profile": self.state.company_profile})
    #     )

    #     print("Company info generated", result.raw)
    #     self.state.company_info = result.raw

    @listen(set_input)
    def generate_proposal(self):
        print("Extracting company info and job description and generating proposal")
        result = (
            ProposalCrew()
            .crew()
            .kickoff(inputs={"company_profile": self.state.company_profile, "job_description": self.state.job_description})
        )

        print("Generated Proposal", result.raw)
        self.state.generated_proposal = result.raw

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
