###################################################### LINKEDIN SEARCH PREFERENCES ######################################################

# These Sentences are Searched in LinkedIn (India-focused software / data roles)
# Enter your search terms inside '[ ]' with quotes ' "searching title" ' for each search followed by comma ', '
search_terms = [
    "Software Engineer",
    "Backend Developer",
    "Full Stack Developer",
    "MERN Stack Developer",
    "Frontend Developer",
    "React Developer",
    "Java Developer",
    "Front End Developer",
    "Web Developer",
    "Nodejs Developer",
    "Data Scientist",
    "Machine Learning Engineer",
    "AI Engineer",
    "Data Engineer",
    "Data Analyst",
]

# Role used when you press Enter at the startup prompt (or pick option 1)
default_search_role = "Software Engineer"

# When True, the bot asks which role to search before logging into LinkedIn
prompt_role_selection_at_start = True

# "India" = nationwide; use "" to leave the location box empty; or e.g. "Bengaluru, Karnataka, India" to narrow.
search_location = "India"

# After how many number of applications in current search should the bot switch to next search? 
switch_number = 30                 # Only numbers greater than 0... Don't put in quotes

# Do you want to randomize the search order when more than one role is selected?
randomize_search_order = False     # False = Software Engineer (or your pick) runs first; True shuffles multi-role runs


# >>>>>>>>>>> Job Search Filters <<<<<<<<<<<
''' 
You could set your preferences or leave them as empty to not select options except for 'True or False' options. Below are some valid examples for leaving them empty:
This is below format: QUESTION = VALID_ANSWER

## Examples of how to leave them empty. Note that True or False options cannot be left empty! 
* question_1 = ""                    # answer1, answer2, answer3, etc.
* question_2 = []                    # (multiple select)
* question_3 = []                    # (dynamic multiple select)

## Some valid examples of how to answer questions:
* question_1 = "answer1"                  # "answer1", "answer2", "answer3" or ("" to not select). Answers are case sensitive.
* question_2 = ["answer1", "answer2"]     # (multiple select) "answer1", "answer2", "answer3" or ([] to not select). Note that answers must be in [] and are case sensitive.
* question_3 = ["answer1", "Random AnswER"]     # (dynamic multiple select) "answer1", "answer2", "answer3" or ([] to not select). Note that answers must be in [] and need not match the available options.

'''

sort_by = ""                       # "Most recent", "Most relevant" or ("" to not select)
date_posted = "Past week"          # "Any time", "Past month", "Past week", "Past 24 hours" or ("" to not select)
# LinkedIn salary chip text is locale-specific. For India, open "All filters" once, copy the exact label for ≥10 LPA, and paste here.
# Examples to try if click fails: "₹10,00,000+", "₹12,00,000+", or leave "" to skip LinkedIn salary filter (JD rules below still apply).
salary = ""

easy_apply_only = True             # True or False, Note: True or False are case-sensitive

# Include internships + early career (matches India campus + lateral hiring)
experience_level = ["Internship", "Entry level", "Associate"]
job_type = ["Full-time", "Internship", "Contract"]
# All work arrangements (India-wide search — no location restriction in filters)
on_site = ["On-site", "Remote", "Hybrid"]

companies = []                     # (dynamic multiple select) make sure the name you type in list exactly matches with the company name you're looking for, including capitals. 
                                   # Eg: "7-eleven", "Google","X, the moonshot factory","YouTube","CapitalG","Adometry (acquired by Google)","Meta","Apple","Byte Dance","Netflix", "Snowflake","Mineral.ai","Microsoft","JP Morgan","Barclays","Visa","American Express", "Snap Inc", "JPMorgan Chase & Co.", "Tata Consultancy Services", "Recruiting from Scratch", "Epic", and so on...
location = []                      # (dynamic multiple select)
industry = []                      # (dynamic multiple select)
job_function = []                  # (dynamic multiple select)
job_titles = []                    # (dynamic multiple select)
benefits = []                      # (dynamic multiple select)
commitments = []                   # (dynamic multiple select)

under_10_applicants = False        # True or False, Note: True or False are case-sensitive
in_your_network = False            # True or False, Note: True or False are case-sensitive
fair_chance_employer = False       # True or False, Note: True or False are case-sensitive


## >>>>>>>>>>> India compensation (JD heuristics) <<<<<<<<<<<
# When True, skips jobs only if the description/title clearly states pay BELOW your minimums.
# Posts with no stipend/CTC numbers are NOT auto-skipped (LinkedIn rarely lists pay).
enforce_india_salary_rules = True
min_fulltime_ctc_lpa = 10          # e.g. skip "6-8 LPA" or "CTC 8 lakhs"; do not skip if no CTC is mentioned
min_internship_stipend_inr = 15000 # monthly INR; skip only if stipend is explicitly below this (e.g. "8000/month")


## >>>>>>>>>>> RELATED SETTING <<<<<<<<<<<

# Pause after applying filters to let you modify the search results and filters?
pause_after_filters = False        # False = fewer clicks for unattended India-wide runs; set True to manually tweak filters once

##




## >>>>>>>>>>> SKIP IRRELEVANT JOBS <<<<<<<<<<<
 
# Avoid applying to these companies, and companies with these bad words in their 'About Company' section...
about_company_bad_words = ["Crossover"]       # (dynamic multiple search) or leave empty as []. Ex: ["Staffing", "Recruiting", "Name of Company you don't want to apply to"]

# Skip checking for `about_company_bad_words` for these companies if they have these good words in their 'About Company' section... [Exceptions, For example, I want to apply to "Robert Half" although it's a staffing company]
about_company_good_words = []      # (dynamic multiple search) or leave empty as []. Ex: ["Robert Half", "Dice"]

# Bad words in job description (case-insensitive). Trimmed for India tech applications — add back any stack you want to avoid.
bad_words = ["US Citizen", "USA Citizen", "US-only", "No C2C", "No Corp2Corp", "polygraph", "US Secret"]

# Do you have an active Security Clearance? (True for Yes and False for No)
security_clearance = False         # True or False, Note: True or False are case-sensitive

# Set False if you are not a master's graduate (affects experience tolerance when JD mentions "master's")
did_masters = False                # True or False, Note: True or False are case-sensitive

# Max years of experience required in JD to still apply (-1 = ignore experience filter)
current_experience = 0             # ~5 months professional (see months_of_experience in questions.py); use -1 to apply to all levels
##





