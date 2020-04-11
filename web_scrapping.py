# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 14:09:31 2020

@author: suyog
"""
#Importing Libraries
import requests
from bs4 import BeautifulSoup
import smtplib

age_url = "https://www.amazon.in/Nestle-Everyday-Dairy-Whitener-Pouch/dp/B00NYZQX9A/ref=lp_21246948031_1_1?srs=21246948031&ie=UTF8&qid=1586594096&sr=8-1"
browser_agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}

product_page = requests.get(page_url,headers=browser_agent)
soup= BeautifulSoup(product_page.content,'html.parser')
print(soup.prettify())
page_title = soup.find(id = "productTitle").get_text().strip()
product_price = soup.find(id="priceblock_ourprice").get_text()[2:8]
product_price = float(product_price)
if(product_price<500):
    send_me_email()

def send_me_email():
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("suyogyaman@gmail.com","my_password_is_gone_lol_with_123")
    message = "Hey buddy !!! You received my email via python script. Here is the URL"
    s.sendmail("suyogyaman@gmail.com","suyogyaman2019@gmail.com",message)
    s.quit()