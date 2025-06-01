import requests
from bs4 import BeautifulSoup
import sqlite3
import csv
import os

URL = "https://realpython.github.io/fake-jobs"
response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")

job_elements = soup.find_all("div", class_="card-content")

conn = sqlite3.connect("jobs.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    title TEXT,
    company TEXT,
    location TEXT,
    description TEXT,
    apply_link TEXT,
    PRIMARY KEY (title, company, location)
)
""")

for job in job_elements:
    title = job.find("h2", class_="title")
    company = job.find("h3", class_="company")
    location = job.find("p", class_="location")
    desc = job.find("div", class_="description")
    apply_link = job.find("a", string="Apply")

    if not (title and company and location and desc and apply_link):
        continue

    title_text = title.text.strip()
    company_text = company.text.strip()
    location_text = location.text.strip()
    desc_text = desc.text.strip()
    link_url = apply_link["href"].strip()

    try:
        cur.execute("""
        INSERT INTO jobs (title, company, location, description, apply_link)
        VALUES (?, ?, ?, ?, ?)
        """, (title_text, company_text, location_text, desc_text, link_url))
    except sqlite3.IntegrityError:

        cur.execute("""
        SELECT description, apply_link FROM jobs
        WHERE title = ? AND company = ? AND location = ?
        """, (title_text, company_text, location_text))
        existing = cur.fetchone()
        if existing and (existing[0] != desc_text or existing[1] != link_url):
            cur.execute("""
            UPDATE jobs
            SET description = ?, apply_link = ?
            WHERE title = ? AND company = ? AND location = ?
            """, (desc_text, link_url, title_text, company_text, location_text))

conn.commit()
print("Data inserted/updated successfully.")

def export_filtered(location=None, company=None):
    query = "SELECT title, company, location, description, apply_link FROM jobs WHERE 1=1"
    params = []

    if location:
        query += " AND location = ?"
        params.append(location)

    if company:
        query += " AND company = ?"
        params.append(company)

    cur.execute(query, params)
    results = cur.fetchall()

    with open("filtered_jobs.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Company", "Location", "Description", "Apply Link"])
        writer.writerows(results)

    print("Filtered data exported to 'filtered_jobs.csv'")

export_filtered(location="New York", company="Sovida")
conn.close()
