###################################################### APPLICATION INPUTS ######################################################


# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Relative path to the resume PDF the bot uploads for Easy Apply. If missing, LinkedIn uses your last uploaded resume.
# Put your exported PDF at this exact path (see folder `all resumes/default/` in the project root).
default_resume_path = "all resumes/default/resume.pdf"      # (In Development)

# Total years of professional experience (full-time + internships you count as work). Use whole years only.
# 5 months ≈ less than 1 year → use "0" on forms that ask for years; use months_of_experience when the form asks for months.
years_of_experience = "0"          # A number in quotes Eg: "0","1","2","3","4", etc.
months_of_experience = 5           # Used when the form label mentions "month(s)" (e.g. 5 months at Amdocs)

# How you heard about the job (never use the bot project's GitHub URL here)
referral_source = "LinkedIn"       # e.g. "LinkedIn", "Company website", "Job board"

# Do you need visa sponsorship now or in future?
require_visa = "No"               # "Yes" or "No"

# Portfolio / personal site (GitHub is fine if you have no separate site)
website = "https://github.com/v1enkat"                        # "www.example.bio" or "" and so on....

# LinkedIn profile URL
linkedIn = "https://www.linkedin.com/in/venkat-manikantha-6b78a9287/"       # "https://www.linkedin.com/in/example" or "" and so on...

# U.S. EEO / work authorization style questions. Use "" to skip if allowed. Edit if you apply mostly to U.S. roles.
# Valid options are: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer", "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization", "Canadian Citizen/Permanent Resident" or "Other"
us_citizenship = ""



## SOME ANNOYING QUESTIONS BY COMPANIES 🫠 ##

# Expected CTC / salary (numbers only). INR examples below—set to your real target.
desired_salary = 1000000          # EDIT: your expected annual CTC in INR (or USD annual if applying abroad)
'''
Note: If question has the word "lakhs" in it (Example: What is your expected CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
And if asked in months, then it will divide by 12 and answer. Examples:
* 2400000 will be answered as "200000"
* 850000 will be answered as "70833"
'''

# Current CTC (numbers only). Use 0 if not applicable (student / stipend only).
current_ctc = 0            # EDIT: current annual CTC in INR, or 0
'''
Note: If question has the word "lakhs" in it (Example: What is your current CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
# And if asked in months, then it will divide by 12 and answer. Examples:
# * 2400000 will be answered as "200000"
# * 850000 will be answered as "70833"
'''

# (In Development) # Currency of salaries you mentioned. Companies that allow string inputs will add this tag to the end of numbers. Eg: 
# currency = "INR"                 # "USD", "INR", "EUR", etc.

# What is your notice period in days?
notice_period = 0                   # Any number >= 0 without quotes. Eg: 0, 7, 15, 30, 45, etc.
'''
Note: If question has 'month' or 'week' in it (Example: What is your notice period in months), 
then it will divide by 30 or 7 and answer respectively. Examples:
* For notice_period = 66:
  - "66" OR "2" if asked in months OR "9" if asked in weeks
* For notice_period = 15:"
  - "15" OR "0" if asked in months OR "2" if asked in weeks
* For notice_period = 0:
  - "0" OR "0" if asked in months OR "0" if asked in weeks
'''

# LinkedIn headline (used when applications ask for headline / title line)
linkedin_headline = "Software Engineer @ Amdocs | B.Tech ECE @ NIT Agartala | Python, MERN, AWS, Azure, Data Reconciliation" # or ""

# LinkedIn-style summary. Use \\n in single-quoted strings for line breaks; triple quotes can use real newlines.
linkedin_summary = """
Software Engineer at Amdocs building data reconciliation experiences (MERN) with 10-day trend views across recon types, comparisons, and batch reports per recon type.
Strong in Python tooling (Azure integrations for ingest/storage), AWS automation (daily operational reporting, lightweight ETL with IAM-aware patterns), Docker, and Kubernetes.
Also experienced shipping full-stack systems (Node/Express, MongoDB, React, JWT, RBAC) through freelance and product-style projects.
"""

'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Default cover letter (tailor per role). Plain text; applications may paste this verbatim.
cover_letter = """
Dear Hiring Manager,

I am a Software Engineer at Amdocs with hands-on work on a data reconciliation application (MERN) that highlights 10-day trends across reconciliation types, comparisons, and batch-style reporting per recon type. I also build and extend Python reconciliation tooling with Microsoft Azure connectivity for data movement and persistence, plus Python-based AWS automation for daily team reporting and small ETL-style workflows. I routinely work with Docker and Kubernetes for containerized services.

Outside of my role, I have delivered full-stack projects using the MERN stack with secure authentication (JWT), RBAC, and MongoDB-backed APIs. I hold a B.Tech in Electronics and Communication Engineering from NIT Agartala and am motivated by clear ownership, measurable outcomes, and collaborative delivery.

Thank you for your consideration.

Sincerely,
Venkat Manikantha Peddiboina
+91-9014522399
22uec115venkat@gmail.com
https://www.linkedin.com/in/venkat-manikantha-6b78a9287/
https://github.com/v1enkat
"""
# Rich profile text for AI-assisted answers (keep updated with your resume). Include facts you are comfortable sharing.
user_information_all = """
Name: Venkat Manikantha Peddiboina
Email: 22uec115venkat@gmail.com
Phone: +91-9014522399
Location: Current — Lane 9, Wagholi, Pune, Maharashtra 412207, India. Permanent — Challapalli, Krishna District, Vijayawada, Andhra Pradesh 521126, India.
LinkedIn: https://www.linkedin.com/in/venkat-manikantha-6b78a9287/
GitHub: https://github.com/v1enkat

IMPORTANT FOR NUMERIC QUESTIONS:
- Total professional work experience: 5 months (started 05 Feb 2026). For "years of experience" answer 0 or less than 1 year, NEVER 12, 15, 25, or 30.
- For "months of experience" answer 5 only.
- Current employer name: Amdocs (exact spelling). Never answer 0 for company name.
- Current job title / role at Amdocs: Software Engineer (exact spelling).
- Portfolio/website/GitHub URL: https://github.com/v1enkat only.

Headline: Software Engineer at Amdocs; B.Tech ECE, NIT Agartala (2022–2026).

Work experience:
- Software Engineer, Amdocs (from 05 Feb 2026, India): Data reconciliation web application (MERN) with 10-day trends across all recon types, comparisons, and batch reports per recon type. Python reconciliation tool with Azure integration to upload/pull data and persist outputs. Python on AWS for automated daily operational reports to the team. Small AWS ETL-style pipeline (ingestion, validation/dedup, IAM-scoped access, orchestrated steps, curated outputs). Docker containerization; running and troubleshooting services on Kubernetes.
- Freelance Web Developer, Aditya University (Jan 2024–Mar 2024): Full-stack faculty evaluation system (Agile), Node/Express REST APIs, MongoDB, RBAC for four roles, testing/debugging workflows, performance reports and analytics.

Education:
- B.Tech Electronics and Communication Engineering, NIT Agartala, 2022–2026.
- Higher Secondary, Narayana Jr. College, 2020–2022; JEE Main 96.4 percentile.

Technical skills:
Languages: C/C++, JavaScript, Python, Java, SQL.
Data: PySpark, Pandas, SQL, batch processing, reconciliation workflows.
Frontend: React.js, HTML, CSS, Tailwind CSS, Figma.
Backend: Node.js, Express.js, REST APIs, middleware, JWT.
Databases: MongoDB, MySQL, PostgreSQL.
Cloud: AWS, Microsoft Azure; Docker, Kubernetes; shell scripting.
Practices: Git, GitHub, Agile, debugging, testing, RBAC, DSA, OOP.

Notable projects:
- NITA-PlacementPro (HTML/CSS/JS, Node, Express, MongoDB): placement portal, JWT auth, CRUD, MongoDB schema—demo placementpro.onrender.com; GitHub v1enkat/PlacementPro.
- TeamNest club management (MERN): RBAC, async patterns, collaboration—YouTube demo and GitHub v1enkat/Full-Stack.
- ThreadCart tailoring e-commerce (MERN): JWT, orders/cart, MongoDB—GitHub v1enkat/Style-Sync; demo stylesync.vercel.app.

Leadership: President, Anima – The Aero Club, NIT Agartala (2023–2024); drone competitions (incl. TECHNOXIAN top placements).

Certifications: Meta Front-End Developer Professional (Coursera); Complete Backend Developer Bootcamp Node/Express (Udemy).

Achievements: 1st Drone Soccer & 3rd Drone Rescue, TECHNOXIAN World Cup 2024; Amazon Hackathon rank 41 among teams; 500+ DSA problems practiced.
"""
##<
'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Name of your most recent employer (must match how you list it on LinkedIn if possible)
recent_employer = "Amdocs" # "", "Lala Company", "Google", "Snowflake", "Databricks"

# Your current / most recent job title at the employer above
current_job_title = "Software Engineer"

# Example question: "On a scale of 1-10 how much experience do you have building web or mobile applications? 1 being very little or only in school, 10 being that you have built and launched applications to real users"
confidence_level = "8"             # Any number between "1" to "10" including 1 and 10, put it in quotes ""
##



# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

## Allow Manual Inputs
# Should the tool pause before every submit application during easy apply to let you check the information?
pause_before_submit = True         # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''

# Should the tool pause if it needs help in answering questions during easy apply?
# Note: If set as False will answer randomly...
pause_at_failed_question = True    # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''
##

# Do you want to overwrite previous answers?
overwrite_previous_answers = False # True or False, Note: True or False are case-sensitive






