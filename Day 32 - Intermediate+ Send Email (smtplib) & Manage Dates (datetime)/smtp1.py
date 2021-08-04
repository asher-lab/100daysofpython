import random
import smtplib
from datetime import datetime

day = datetime.today().strftime('%A')
MY_EMAIL = "cocofasher1@gmail.com"
MY_PASSWORD = "amtabha27"

if day == "Wednesday":
    #TODO open quotes.txt
    with open("quotes.txt",encoding="utf-8") as file:
        file = file.read().splitlines()

    quote = file[random.randrange(0, 100, 1)]
    quote = random.choice(file)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg = f"Subject: Wednesday Motivation\n\n {quote}".encode('utf-8') )
