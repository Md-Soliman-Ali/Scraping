import requests
from bs4 import BeautifulSoup
import json

print("""
########################################
 #### MADE BY W3B (MD SOLIMAN ALI) ####
 ##### LIVE SUBDOMAIN ENUMURATION #####
########################################
""")

domain = input("Input Your Root Domain (Example: google.com) -> ")
res = requests.get("https://crt.sh/?q=%25."+str(domain))

soup = BeautifulSoup(res.text, 'html.parser')

tr = soup.findAll('tr')

all_domain = []


for each in range(3, len(tr) - 1):
	td = tr[each].findAll('td')[4].text
	td_split = str(td).split()
	for each_domain in td_split:
		if each_domain not in all_domain:
			print(each_domain)
			all_domain.append(each_domain)

for a in all_domain:
    try:
        requests.get("http://"+str(a)+"/", timeout=3)
        print("GOOD "+str(a))
    except:
        print("BAD "+str(a))

print("Total Domain "+str(len(all_domain)))