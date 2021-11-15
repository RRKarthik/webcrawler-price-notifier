# webcrawler-price-notifier
Project by:Dukka Ravi Ram Karthik  

IMPORTANT:1.Please allow less secure app access from your email for proper working of the program.
          2.As price drop cannot be filmed in a video the discounted price is set to be more than website price
             to prove that the program works.
          3.Use only gmail as the smtplib is a Google module that works with only gmail.

Introduction:
The program is intented for users who want to buy a product on FLIPKART but cannot as the price is too high.
This program uses web scrapping and scrapes the price of the product from the given url.It then checks to see if the 
price is the website is less than or equal to the price at which user wants to buy the product.If this is true then an
e-mail will be sent to the reciever's e-mail notifying them of the price drop.The user need not open the website several times to 
check if the price is low as the program is designed to check for the price everyday, It can be executed and be left to run in the 
background.

Inputs:
1.The url of the product on Flipkart.
2.The discounted price at which you want to buy the product.
3.The sender gmail.
4.The sender password to use the smtplib module from google to send gmails.
5.The reciever e-mail.

The user can allow the program to run in background as it will sleep for 1-day after every check for price.In otherwords,It checks
for the price drop everyday.

