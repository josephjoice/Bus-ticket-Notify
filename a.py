import requests
from subprocess import call
from bs4  import BeautifulSoup
for line in open("servicesTocheck.txt"):
    params = line.split()
    r=requests.get("http://www.ksrtc.in/oprs-web/forward/booking/avail/services.do?txtJourneyDate="+params[0]+"&startPlaceId="+params[1]+"&endPlaceId="+params[2]+"&ajaxAction=fw&singleLady=&qryType=0")
    soup = BeautifulSoup(r.content,'html.parser')
    dontWantServices=params[3:]
    count=0;
    for one in soup.findAll("div", { "class" : "row" }):
        serviceName=one.find("div",{"class" : "col1"}).text.split()[0]
        if (serviceName not in dontWantServices):
            seatsHtml=one.find("span", { "class" : "availCs" })
            count+=int(seatsHtml.get('availcs'))
    print count
#     if (count>0):
#         call(["python","sendMail.py",str(count)])

