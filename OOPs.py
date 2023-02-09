import requests
from bs4 import BeautifulSoup

# URL for job search
URL = "https://www.indeed.com/jobs?q=AI+Developer&l="

# Send a GET request to the URL
response = requests.get(URL)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract all job listings
job_listings = soup.find_all('div', class_='jobsearch-SerpJobCard')

# Iterate through each job listing and extract the title, company, and last date
for job in job_listings:
    title = job.find('a', class_='jobtitle')
    company = job.find('span', class_='company')
    last_date = job.find('span', class_='date')
    
    # Print the extracted information
    print("Job Title: ", title.text.strip())
    print("Company: ", company.text.strip())
    print("Last Date: ", last_date.text.strip())
    print()