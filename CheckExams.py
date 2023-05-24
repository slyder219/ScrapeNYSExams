import requests 
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import webbrowser

# Site for current NYS exam offerings
url = "https://www.cs.ny.gov/examannouncements/types/oc/"

# Send get request
response = requests.get(url)
content = response.content 

# Parse conent 
soup = BeautifulSoup(content, "html.parser")

# Get html
html = soup.find_all("a", href = True)

# Get exam titles
exams = []
for line in html:
    href = line.get("href")
    if ".cfm" in href and "examannouncements/announcements" in href:
        exams.append(line)

# The keywords we want =
arg1 = "data"
arg2 = "entry"
arg3 = "type"

# Find and print keywords
finds = []
for exam in exams:
    if arg1 in exam.text.lower() or arg2 in exam.text.lower() or arg3 in exam.text.lower():
        # print()
        # print(exam.text)
        finds.append(exam)

toaster = ToastNotifier()
if finds:
    print("found")
    message = "Exam Web Scrape Ran. Matches found for:\n '{}' and '{}' and '{}'".format(arg1, arg2, arg3)
    toaster.show_toast("FOUND: NYS Exams", message, duration = 5)
else: 
    message = "Exam Web Scrape Ran. Nothing found. \nSearched for '{}' and '{}' and '{}'".format(arg1, arg2, arg3)
    toaster.show_toast("NOT FOUND: NYS Exams", message, duration = 5)