#create a webscraper using beautifullsoup and scrape job opening from the internet 

import requests
from bs4 import BeautifulSoup


def get_jobs(word):
    url = f"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{word}&txtLocation="
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for job in jobs:
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            print(f"Company Name: {company_name.strip()}")
            print(f"Skills: {skills.strip()}")


get_jobs('python')
get_jobs('java')
get_jobs('c++')
get_jobs('c')