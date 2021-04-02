

import requests
from bs4 import BeautifulSoup
url = "https://www.doviz.com/"
response = requests.get(url)
html_içeriği = response.content
soup = BeautifulSoup(html_içeriği,"html.parser")
deger_isimleri = soup.find_all("span",{"class":"name"})
donusum = soup.find_all("span",{"class":"value"})
print("-To exit 0\n-To see the values 1\n-To calculate from Euro to TL 2\n-To calculate from TL to Euro 3")
print()
a = int(input("Exit : "))
while a!=0:
    if a == 1:
        for i,j in zip(deger_isimleri,donusum):
            print(i.text,"->",j.text)
        a = int(input("Exit : "))
    elif a==2:
        for i,j in zip(deger_isimleri,donusum):
            if i.text == "EURO":
                k = j.text.replace(",",".")
                translate = float(k)
                cost = float(input("Please enter the cost of your product : "))
                print("The cost of the product you are searching TL is : ",translate*cost)
        a = int(input("Exit : "))

    elif a == 3:
        for i,j in zip(deger_isimleri,donusum):
            if i.text == "EURO":
                k = j.text.replace(",",".")
                translate = float(k)
                cost = float(input("Please enter the cost of your product : "))
                print("The cost of the product you are searching in Euro is : ",cost/translate)
        a = int(input("Exit : "))

    



        
