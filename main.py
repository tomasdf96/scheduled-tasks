import pandas as pd
import datetime as dt
import random
import smtplib
import os

MY_EMAIL = os.environ.get(MY_EMAIL)
MY_PASSWORD = os.environ.get(MY_PASSWORD)

birthday_df = pd.read_csv("birthdays.csv")
birthday_dict = birthday_df.to_dict(orient="records")

# adding_birthdays = True

# while adding_birthdays:
#     new_entry = input("Do you want to add a birthday to the list? Type 'y' or 'n': ").lower()
#     if new_entry == "y":
#         new_birthday = {
#             "name": input("What is the person's name?\n").title(),
#             "email": input(f"What is their email?\n").lower(),
#             "year": input("Enter year: "),
#             "month": input("Enter month: "),
#             "day": input("Enter day: ")
#         }
#         birthday_dict.append(new_birthday)
#         print("Added a birthday!\n")
#     else:
#         new_birthday_df = pd.DataFrame(birthday_dict)
#         new_birthday_df.to_csv("birthdays.csv", index=False)
#         adding_birthdays = False

today = dt.datetime.now()

for (index, row) in birthday_df.iterrows():
    if row.month == today.month and row.day == today.day:
        letter_num = random.randint(1,3)
        with open(f"letter_templates/letter_{letter_num}.txt", "r") as f:
            filedata = f.read()
            filedata1 = filedata.replace("[NAME]", row["name"])
            filedata2 = filedata1.replace("Angela", "Tomas")
        with open("birthday_letter.txt", "w") as ready:
            ready.write(filedata2)
        with open("birthday_letter.txt", "r") as letter:
            letter_body = letter.read()
            with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=row["email"],
                    msg=f"Subject:Happy Birthday, {row["name"]}!\n\n{letter_body}"
                )
