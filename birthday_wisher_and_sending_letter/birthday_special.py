import pandas
data=pandas.read_csv("birthdays.csv")
birthdays_dict={(row.month, row.day) : row for (index,row) in data.iterrows()}

import datetime as dt
now=dt.datetime.now()
today=now.day
this_month=now.month
this_year=now.year
tuple_date=(this_month,today)

if tuple_date in birthdays_dict:
        birthday_person=birthdays_dict[tuple_date]
        import smtplib
        import random
        num=random.randint(1,3)
        letter=f"letter_templates\\letter_{num}.txt"     
        with open(f"letter_templates\\letter_{num}.txt") as letter_file:
                content=letter_file.read()
                birthday_wish=content.replace("[NAME]",birthday_person["name"])

        my_name="20d3725bathrinath@gmail.com"
        my_password="kzkjwppvxdmsyysh"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_name,password=my_password)
            connection.sendmail(from_addr=my_name,to_addrs=birthday_person["email"],msg=f"Subject:Happy Birthday!!!\n\n{birthday_wish}")



    

