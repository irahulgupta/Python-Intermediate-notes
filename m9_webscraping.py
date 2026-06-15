import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print("MODULE 9 HANDS-ON: API + SCRAPING TOOL")
print("-" * 55)

# --------------------------------------------------
# 1. API HANDLING - JSON RESPONSE
# --------------------------------------------------
print("\n1. API HANDLING - JSON DATA")

api_url = "https://jsonplaceholder.typicode.com/users/1"

try:
    response = requests.get(api_url, verify=False, timeout=10)

    if response.status_code == 200:
        user_data = response.json()
        print("API call successful")
        print("User ID:", user_data["id"])
        print("Name:", user_data["name"])
        print("Email:", user_data["email"])
        print("City:", user_data["address"]["city"])
    else:
        print("API request failed with status code:", response.status_code)

except Exception as e:
    print("API request error:", e)


# --------------------------------------------------
# 2. XML HANDLING
# --------------------------------------------------
print("\n2. XML DATA HANDLING")

xml_data = """
<courses>
    <course>
        <id>101</id>
        <title>Python Basics</title>
        <duration>3 Days</duration>
    </course>
    <course>
        <id>102</id>
        <title>Data Analysis with Python</title>
        <duration>2 Days</duration>
    </course>
</courses>
"""

root = ET.fromstring(xml_data)

for course in root.findall("course"):
    course_id = course.find("id").text
    title = course.find("title").text
    duration = course.find("duration").text
    print(f"Course ID: {course_id}, Title: {title}, Duration: {duration}")


# --------------------------------------------------
# 3. WEB SCRAPING USING BEAUTIFULSOUP
# --------------------------------------------------
print("\n3. WEB SCRAPING - HTML PARSING")

html_content = """
<html>
    <head><title>Training Courses</title></head>
    <body>
        <h1>Available Courses</h1>
        <ul>
            <li class="course">Python Intermediate</li>
            <li class="course">SQL Fundamentals</li>
            <li class="course">Web Scraping Essentials</li>
        </ul>
    </body>
</html>
"""

soup = BeautifulSoup(html_content, "html.parser")

print("Page Title:", soup.title.text)
print("Course List:")

courses = soup.find_all("li", class_="course")
for course in courses:
    print("-", course.text)


# --------------------------------------------------
# 4. REQUEST TO FETCH HTML PAGE
# --------------------------------------------------
print("\n4. FETCHING HTML PAGE USING REQUESTS")

page_url = "https://example.com"

try:
    page_response = requests.get(page_url, verify=False, timeout=10)

    if page_response.status_code == 200:
        print("HTML page fetched successfully")
        print("Response length:", len(page_response.text))
    else:
        print("Failed to fetch HTML page. Status code:", page_response.status_code)

except Exception as e:
    print("HTML page request error:", e)


print("\nLab completed successfully.")

