##################### Extra Hard Starting Project ######################
import pandas
import random
import smtplib
from datetime import datetime
data = pandas.read_csv("birthdays.csv")

# ----------Credentials----------#
MY_EMAIL = "cocofasher1@gmail.com"
MY_PASSWORD = "amtabha27"


# ----------Function Definition ----------#
def send_email(message_to_pass, to_email):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=to_email,
                            msg = f"Subject: HAPPY BIRTHDAY!\n\n {message_to_pass}".encode('utf-8') )


# ----- BIRTHDAY BY WEEKDAY -------#
# 2. Check if today matches a birthday in the birthdays.csv
daynow = datetime.today().strftime('%A')
count = 0
for day in data["day"]:
    if day == daynow:
        celebrant = data["name"][count]
        celebrant_email = data["email"][count]


        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
            message = letter.read()
            message = message.replace('[NAME]', celebrant)
            send_email(message, celebrant_email)
    count += 1

# 4. Send the letter generated in step 3 to that person's email address.




