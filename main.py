import pandas
import random
import datetime as dt
import smtplib

my_email = "jp0739396@gmail.com"
my_password = "rs6z3f+&z%70LaNV)e"

birthdays = pandas.read_csv("birthdays.csv")
birthdays_dic = birthdays.to_dict(orient="records")

letters = []

with open("letter_templates/letter_1.txt") as letter_1:
    letter = letter_1.read()
    letters.append(letter)
with open("letter_templates/letter_2.txt") as letter_2:
    letter = letter_2.read()
    letters.append(letter)
with open("letter_templates/letter_3.txt") as letter_3:
    letter = letter_3.read()
    letters.append(letter)

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

for i in range(0, len(birthdays)):
    if day == birthdays_dic[i]["day"] and month == birthdays_dic[i]["month"]:
        name = birthdays_dic[i]["name"]
        new_letter = random.choice(letters)
        new_letter_replaced = new_letter.replace("[NAME]", name)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthdays_dic[i]["email"],
                msg=f"Subject:Happy Birthday!!\n\n{new_letter_replaced}"
            )
        print(new_letter_replaced)
        print(day)
