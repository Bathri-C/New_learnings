# import smtplib
# my_name="20d3725bathrinath@gmail.com"
# my_password="kzkjwppvxdmsyysh"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_name,password=my_password)
#     connection.sendmail(from_addr=my_name,to_addrs="bitbatbathri0608@gmail.com",msg="Subject:Hii!!!\n\nHow are you?I am fine.")

# import datetime as dt
# now=dt.datetime.now()
# year=now.year
# month=now.month
# print(now,year,month)
# day=now.weekday()
# print(day)

import smtplib
import datetime as dt
import random
now=dt.datetime.now()
day=now.weekday()
print(day)
if day==5:
    with open("Birthday_wisher\\quotes.txt") as data:
        all_quotes=data.readlines()
        
    my_name="20d3725bathrinath@gmail.com"
    my_password="kzkjwppvxdmsyysh"
    quotes=random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_name,password=my_password)
        connection.sendmail(from_addr=my_name,to_addrs="bitbatbathri0608@gmail.com",msg=f"Subject:quotes!!!\n\n{quotes}")



