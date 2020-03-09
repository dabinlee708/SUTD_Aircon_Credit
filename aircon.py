import requests
from bs4 import BeautifulSoup

credit_wallet="https://nus-utown.evs.com.sg/SUTDMain/viewMeterCreditServlet"
login="https://nus-utown.evs.com.sg/SUTDMain/loginServlet"
log_val = dict(
				txtLoginId ='20000596',
				txtPassword='IF YOU ARE LOOKING FOR PW, YOU HAVE FAILED')
s=requests.session()
r=s.post(login,data=log_val)
r=s.get(credit_wallet)
html=r.text
soup = BeautifulSoup(html,'lxml')
parsed_list=[]
for td_tag in soup.find_all('font'):
	parsed_list.append(td_tag.text)
print "Meter ID: ",parsed_list[2],"\nCredit  : ",parsed_list[5], "\nTime    : ",parsed_list[6]
