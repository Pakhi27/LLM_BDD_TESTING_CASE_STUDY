# LLM-Assisted BDD Functional Testing – Case Study

## Overview
This project demonstrates an **LLM-assisted Behavior Driven Development (BDD) functional testing workflow**.  
The objective is to show how **Large Language Models (LLMs)** can assist in **test scenario creation** while keeping **test execution controlled, reliable, and human-approved**.

The system converts **plain English business requirements** into **BDD-style Gherkin scenarios**, validates and filters them, requires **manual approval**, and then executes **approved happy-path scenarios** using **Behave and Selenium**.

---

## Problem Statement
Build a simple LLM-assisted Functional Testing module that:

- Accepts plain-English business requirements
- Generates BDD-style scenarios using Given–When–Then format
- Covers at least one positive and one negative flow
- Automatically executes only happy-path scenarios
- Keeps scenario generation separate from execution
- Requires manual approval before running automated tests

---

## High-Level Architecture

1.Business Requirement (Text)

2.LLM Scenario Generator

3.Scenario Validation

4.Happy Path Selection

5.Manual Approval

6.BDD Automation (Behave + Selenium)


---

## Project Structure
llm_bdd_testing/

│

├── llm_generator.py # Mocked LLM (deterministic output)

├── llm_generator_hf.py # Real Hugging Face LLM (FLAN-T5)
│

├── validator.py # Validates generated scenarios

├── happy_path_filter.py # Filters happy-path scenarios

├── approval.txt # Manual approval record
│

├── features/
│ ├── login.feature # Approved BDD scenario

│ └── steps/

│ └── login_steps.py # Selenium step definitions

│

├── requirements.txt

└── README.md


---

## LLM Scenario Generation

### 1. Mocked LLM (`llm_generator.py`)
- Returns predefined Gherkin scenarios
- Used for stable, offline, deterministic execution
- Useful for demonstration and fallback scenarios

### 2. Real LLM (`llm_generator_hf.py`)
- Uses **Hugging Face FLAN-T5** via the Transformers pipeline
- Converts business requirements into BDD scenarios
- Demonstrates real LLM integration without external APIs

Both generators follow the same interface, allowing easy switching without changing the automation layer.

---

## Scenario Validation
Generated scenarios are validated to ensure they contain **only known, automation-safe actions** (e.g., login, click, redirect).  This prevents unreliable or hallucinated steps from reaching the automation stage.

---

## Happy Path Selection
Only **positive (happy-path)** scenarios are selected for automation.  Negative scenarios are generated for documentation and analysis but are not executed automatically to ensure stability and reliability.

---

## Manual Approval
Before automation:
- A human reviewer verifies the selected scenario
- Approval is documented in `approval.txt`

This enforces a **human-in-the-loop** approach and prevents blind execution of AI-generated content.

---

## BDD Automation

### Tools Used
- **Behave** – BDD framework
- **Selenium** – Browser automation

### Execution Command
```bash
python -m behave features/login.feature

```
## Setup Instructions

### Prerequisites
- Python 3.10 or higher
- Google Chrome browser
- Git

---

### 1. Clone the Repository
```bash
git clone https://github.com/Pakhi27/LLM_BDD_TESTING_CASE_STUDY.git
cd LLM_BDD_TESTING_CASE_STUDY
```
### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```
### 3. Install Dependencies
```bash
python -m pip install -r requirements.txt
```
### 4. Generate BDD Scenarios Using LLM
```bash
python llm_generator_hf.py
python llm_generator.py
```
### 5. Validate and Approve Scenario
Review the generated scenarios
Select the happy-path scenario
Copy it into:
```bash
features/login.feature
```
### 6. Execute BDD Automation
```bash
python -m behave features/login.feature
```
## Design Highlights

1.Clear separation of AI generation and test execution.

2.Manual approval before automation.

3.Stable and deterministic test execution.

4.Enterprise-aligned testing workflow.

## Conclusion

This case study demonstrates how LLMs can enhance BDD test creation while maintaining strict control over automation.The approach balances innovation with reliability, making it suitable for enterprise QA environments.
