import pandas
import smtplib
import random
import datetime as dt

MY_EMAIL = "pedroeusebio45@gmail.com"
PASSWORD = "exirpfsmroawwchf"

# 1. Check if today matches a birthday in the birthdays.csv
birthdays = pandas.read_csv("birthdays.csv")
now = dt.datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day
for index, row in birthdays.iterrows():
    day = row["day"]
    month = row["month"]
    year = row["year"]
    if day == current_day and month == current_month:
        years_old = str(current_year - year)
        years_old_sliced = int(years_old[1::])
        if years_old_sliced == 1:
            suffix = "st"
        elif years_old_sliced == 2:
            suffix = "nd"
        elif years_old_sliced == 3:
            suffix = "rd"
        else:
            suffix = "th"
        file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(file_path) as letter_file:
            contents = letter_file.read()
            email = contents.replace("[NAME]", row["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="teste123teste12@yahoo.com",
                msg=f"Subject:Happy Birthday, enjoy your {years_old}{suffix}!\n\n{email}"
            )


# 2. If step 1 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
# from birthdays.csv

# 3. Send the letter generated in step 2 to that person's email address.
