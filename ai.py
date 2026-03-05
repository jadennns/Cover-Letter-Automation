import json
import anthropic
import pdfplumber
import re
from bs4 import BeautifulSoup
from scrape import scrape_job
from dotenv import load_dotenv

load_dotenv()

# CONFIGURATIONS
RESUME_FILE = "../../Resume/resume.pdf"

def parse_resume() -> str:
    if RESUME_FILE.endswith(".pdf"):
        text = ""
        with pdfplumber.open(RESUME_FILE) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
            return text.strip()
    else:
        raise ValueError("Unsupported file format. Only PDF is supported.")
    
# MAIN AI FUNCTION

def ai(job_url: str):
    client = anthropic.Anthropic()
    resume_text = parse_resume()
    job_text = scrape_job(job_url)

    prompt = f"""
    You are helping write a professional cover letter for a job/intern application.

    Applicant: Jaden Nathanael Simanjuntak

    Here is the applicant's resume:
    ---
    {resume_text}
    ---

    Here is the job posting: 
    ---
    {job_text}
    ---


    Then generate the following in JSON format (raw JSON only, no markdown, no preamble):
    {{
    "salutation": "Dear Hiring Manager,",
    "subject": "Application for [Role] at [Company]",
    "body": "Full cover letter body in LaTeX-safe plain text, do not use em dash, 2-3 paragraphs."
    }}

    Rules:
    - Fetch and read the job posting URL before generating anything
    - Salutation: use the hiring manager's name if found, otherwise "Dear Hiring Manager,"
    - Subject: include the exact role and company name from the posting
    - Body: tailor it to the job, referencing specific skills/experience from the resume
    - Body: no LaTeX special characters (avoid &, %, $, #, _, {{, }}, ~, ^, \\)
    """

    message = client.messages.create(
        model="claude-4-sonnet-20250514",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
        tools=[{"type": "web_search_20250305", "name": "web_search"}]
    )

    
    full_response = " ".join(
        block.text for block in message.content if hasattr(block, "text")
    )

    match = re.search(r'\{.*\}', full_response, re.DOTALL)
    if not match:
        raise ValueError("No JSON found in Claude's response")

    return json.loads(match.group())
