import bs4
import urllib.request as url

path = "https://www.freshersworld.com/python-jobs/3535127"
response = url.urlopen(path)
page_html = bs4.BeautifulSoup(response, "lxml")
jobTitles = page_html.find_all("h3", {"class" : "latest-jobs-title"})
degree = page_html.find_all('span', {'class' : 'qualifications'})
skills = page_html.find_all("span", {'class' : "eligibility-skills"})

for i in range(len(jobTitles)):
    print(jobTitles[i].text)
    print(degree[i].text)
    print(skills[i].text)
    print("*" * 20)
