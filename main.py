import requests
from openpyxl import Workbook

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"

response = requests.get(url)
if response.ok:
    data = response.json()
else:
    print("Failed to fetch the data")
    data = []

def get_number_of_TechJobs(technology):
    number_of_jobs = 0
    for job in data:
        if "Key Skills" in job and technology.lower() in job["Key Skills"].lower():
            number_of_jobs += 1
    return technology, number_of_jobs

def get_number_of_LocationJobs(location):
    number_of_jobs = 0
    for job in data:
        if "Location" in job and location.lower() in job["Location"].lower():
            number_of_jobs += 1
    return location, number_of_jobs


tech_languages = [
    "C", "C#", "C++", "Java", "JavaScript",
    "Python", "Scala", "Oracle", "SQL Server",
    "MySQL Server", "PostgreSQL", "MongoDB"
]

wb = Workbook()
ws = wb.active
ws.title = "Job Listings"

# Add headers
ws.append(["Technology", "Number of Job Postings"])


for tech in tech_languages:
    tech_name, number_of_jobs = get_number_of_TechJobs(tech)  
    ws.append([tech_name, number_of_jobs])

wb.save("job-postings.xlsx")
print("Saved in 'job-postings.xlsx'")
