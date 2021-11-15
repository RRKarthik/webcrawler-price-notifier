""" Project by:Dukka Ravi Ram Karthik  B.Tech 1 year
    e-mail:raviramkarthik7@gmail.com   
    Project name: Scrapper
"""

import requests
from bs4 import BeautifulSoup
import smtplib
from time import sleep

url=input("Enter the url of the Flipkart product you want to buy")   #URL Of the PRODUCT on Flipkart
idealPrice = int(input("Enter the discounted price : "))             #The discounted price at which you want to buy the product
senderEmail = input("Enter sender email")                            #Sender's e-mail
password = input("Enter the password")                               #Sender's password
recieverEmail = input("Enter reciever email")                        #Reciever's e-mail

while True:   #Running the loop until the price drops and a mail is sent

        message = "The product you wanted to buy is at the discounted price you wanted \n "+ url
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')
        price = soup.find('div',attrs={'class':'_1vC4OE _3qQ9m1'})
        money = price.text         #For example the price we get is like ₹25,000. Remove '₹' and comma to make it a float
        money = money.strip("₹")   #Removing the Rupee symbol from the price to make it a float
        money1 = money.replace(",","") #Removing the comma from the price to make it a float
        if(int(money1) <= idealPrice):  #checking to see if the actual price is less than or equal to our required price
                    server = smtplib.SMTP('smtp.gmail.com', 587)  #Setting up e-mail service
                    server.ehlo()
                    server.starttls()
                    server.ehlo()
                    server.login(senderEmail,password)
                    server.sendmail(senderEmail,recieverEmail,message)   #Notifying the person regarding the price drop
                    server.quit()
                    print("Mail has been sent")
                    break;            #Breaking the loop once the mail is sent
        sleep(86400)                  #Making the program to sleep for a day so it can check again for price drop the next day.
    

