# Software Engineering Laboratory Portfolio (Labs 1 – 6)

**Student Name:** Kushitha K  
**SRN:** PES1UG24CS247  
**Section:** E  
**GitHub Repository:** [Kushitha30/Software_Engineering_LABS](https://github.com/Kushitha30/Software_Engineering_LABS)  

This repository consolidates all deliverables, reports, source code, and test suites across Software Engineering Labs in clean, dedicated lab folders.

---

## Portfolio Index

| Lab | Title / Topic | Contents & Deliverables |
| :--- | :--- | :--- |
| **Lab 1** | **Requirements Engineering & UML Use-Case Modelling** | [`Lab1_Requirements_Engineering/`](./Lab1_Requirements_Engineering/)<br>• SRS Document: `SRS.pdf` & `1_SRS_StudentRecordSystem.docx`<br>• Work Breakdown Structure: `WBS.pdf`<br>• Architecture & Design Spec: `3_ArchitectureDesign_StudentRecordSystem.docx`<br>• System Architecture Diagram: `Automated Rubric Evaluator Architecture.png`<br>• Use-Case Diagrams & Flow: `UML_Use_Case_Diagram_PES1UG24CS247.pdf`, `USE_CASE_DIAGRAM_ARER7.png`, `Use_Case_Flow_PES1UG24CS247.docx` & `.pdf`<br>• Requirements & RTM: `Automated_Rubric_Assignment_Evaluator_RTM.xlsx`, `Requirements_Table (2).xlsx` |
| **Lab 2** | **Automated Rubric Assignment Evaluator (ARAE)** | [`LAB2_ARAE/`](./LAB2_ARAE/)<br>• Final Lab 2 Deliverables: `ARAE_Final_Deliverables.pdf`<br>• Use Cases, Actor Specifications, and System Requirements documentation: `README.md` |
| **Lab 3** | **Agile Project Management (Scrum, Kanban, Bug Tracking)** | [`Lab3_Agile_Scrum_Kanban/`](./Lab3_Agile_Scrum_Kanban/)<br>• Jira Scrum Planning & Epics: `SCRUM.pdf`, `SCRUM.docx`<br>• Jira Kanban Board Implementation: `KANBAN_KUSHITA_PES1UG24CS247_#BPS1.pdf`<br>• Jira Bug Tracking System: `BUGTRACKING_PES1UG24CS247_#BPS1.pdf`, `BUG_TRACKING_PROJECT.pdf`<br>• Team Execution Playbook: `Team_Execution_Playbook_TEAM-E12.docx`<br>• GitHub Project Setup: `github repository.png` |
| **Lab 4** | **Vibe Coding & Game Logic Engineering** | [`Lab4_VibeCoding/`](./Lab4_VibeCoding/) & [`02_air_hockey-main/`](./02_air_hockey-main/)<br>• Screen Recordings: Before (`SE LAB 04 BEFORE VIDEO _ VIBE CODING.mp4`) & After (`SE__LAB 04__AFTER VIDEO __VIBE CODING.mp4`)<br>• LLM / Vibe Coding Prompt History: `SE_LAB 04_PES1UG24CS247_VIBE CODING__CHAT HISTORY.pdf`<br>• Air Hockey Python Code: (`main.py`, `game_engine.py`, `ai.py`, `collisions.py`, `paddle.py`, `puck.py`, `renderer.py`, `requirements.txt`)<br>• Verification Report: `Verify Air Hockey Project.html`<br>• GitHub Copilot Experiments: [`github_copilot/`](./Lab4_VibeCoding/github_copilot/) (`github_copilot_code.png`, `Copilot_Repository_Link.txt`) |
| **Lab 5** | **Static Code Analysis (Pylint, Bandit, Flake8)** | [`Lab5_Static_Code_Analysis/`](./Lab5_Static_Code_Analysis/)<br>• Cleaned & Refactored Source Code: `pos_system.py` (**Pylint Score: 10.00/10**, **0 Bandit findings**, **0 Flake8 issues**)<br>• Completed Issue Tracking Table: `issues.md`<br>• Answers to Lab Reflection Questions: `reflection.md`<br>• Static Analysis Baseline Reports (Before): `pylint_report_before.txt`, `bandit_report_before.txt`, `flake8_report_before.txt`<br>• Static Analysis Verified Reports (After): `pylint_report_after.txt`, `bandit_report_after.txt`, `flake8_report_after.txt` |
| **Lab 6** | **Code and Branch Coverage Analysis** | [`Lab6_Code_and_Branch_Coverage/car_rental_rate/`](./Lab6_Code_and_Branch_Coverage/car_rental_rate/)<br>• Tested Application Module: `car_rental_rate.py`<br>• Code Coverage Test Suite: `CodeCoverageTest_car_rental_rate.py` (**100% Statement Coverage**)<br>• Branch Coverage Test Suite: `BranchCoverageTest_car_rental_rate.py` (**100% Branch Coverage**)<br>• Unified Pytest Suite: `test_car_rental.py` (**100% Statements / 100% Branches**)<br>• Terminal Execution Screenshots: `code_coverage_screenshot.png`, `branch_coverage_screenshot.png`<br>• Text Reports: `code_coverage_report.txt`, `branch_coverage_report.txt` |

---

## Standalone Repositories

- **Lab 4 Air Hockey Standalone:** [`02_air_hockey-main/`](./02_air_hockey-main/)
- **Lab 6 Car Rental Standalone Repo:** [SETAPESU26/L6_L7_02_car_rental_rate](https://github.com/SETAPESU26/L6_L7_02_car_rental_rate)

---

## Repository Structure

```text
Software_Engineering_LABS/
│
├── README.md                                  # Unified Portfolio Index
│
├── 02_air_hockey-main/                        # Air Hockey Game Module & Assets
│   ├── ai.py, collisions.py, game_engine.py, main.py, paddle.py, puck.py, renderer.py
│   ├── SE LAB 04 BEFORE VIDEO _ VIBE CODING.mp4
│   ├── SE__LAB 04__AFTER VIDEO __VIBE CODING.mp4
│   ├── SE_LAB 04_PES1UG24CS247_VIBE CODING__CHAT HISTORY.pdf
│   └── Verify Air Hockey Project.html
│
├── Lab1_Requirements_Engineering/             # Lab 1 Requirements, Architecture & UML
│   ├── 1_SRS_StudentRecordSystem.docx, 3_ArchitectureDesign_StudentRecordSystem.docx
│   ├── ARAE_Final_Deliverables.pdf, Automated Rubric Evaluator Architecture.png
│   ├── Automated_Rubric_Assignment_Evaluator_RTM.xlsx, Requirements_Table (2).xlsx
│   ├── SRS.pdf, UML_Use_Case_Diagram_PES1UG24CS247.pdf, USE_CASE_DIAGRAM_ARER7.png
│   ├── Use_Case_Flow_PES1UG24CS247.docx, Use_Case_Flow_PES1UG24CS247.pdf, WBS.pdf
│
├── LAB2_ARAE/                                 # Lab 2 Automated Rubric Evaluator
│   ├── ARAE_Final_Deliverables.pdf, README.md
│
├── Lab3_Agile_Scrum_Kanban/                   # Lab 3 Agile Project Management
│   ├── BUGTRACKING_PES1UG24CS247_#BPS1.pdf, BUG_TRACKING_PROJECT.pdf, github repository.png
│   ├── KANBAN_KUSHITA_PES1UG24CS247_#BPS1.pdf, SCRUM.docx, SCRUM.pdf, Team_Execution_Playbook_TEAM-E12.docx
│
├── Lab4_VibeCoding/                           # Lab 4 Vibe Coding
│   ├── README.md, SE LAB 04 BEFORE VIDEO _ VIBE CODING.mp4, SE__LAB 04__AFTER VIDEO __VIBE CODING.mp4
│   ├── SE_LAB 04_PES1UG24CS247_VIBE CODING__CHAT HISTORY.pdf, Verify Air Hockey Project.html
│   ├── air_hockey/
│   └── github_copilot/
│
├── Lab5_Static_Code_Analysis/                 # Lab 5 Static Code Analysis
│   ├── pos_system.py, issues.md, reflection.md, README.md
│   ├── bandit_report_before.txt / bandit_report_after.txt
│   ├── flake8_report_before.txt / flake8_report_after.txt
│   └── pylint_report_before.txt / pylint_report_after.txt
│
└── Lab6_Code_and_Branch_Coverage/             # Lab 6 Code & Branch Coverage Analysis
    └── car_rental_rate/
        ├── car_rental_rate.py                 # Module Under Test
        ├── CodeCoverageTest_car_rental_rate.py    # 100% Code Coverage Test Suite
        ├── BranchCoverageTest_car_rental_rate.py  # 100% Branch Coverage Test Suite
        ├── test_car_rental.py                 # Full Pytest Test Suite
        ├── code_coverage_screenshot.png       # Terminal Screenshot (>90% Code Coverage)
        ├── branch_coverage_screenshot.png     # Terminal Screenshot (>90% Branch Coverage)
        ├── code_coverage_report.txt           # Coverage report output
        ├── branch_coverage_report.txt         # Branch coverage report output
        └── README.md                          # Lab 6 Documentation
```
