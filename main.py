import pandas, smtplib, random
import datetime as dt
import os


def send_email(message, to_email):
    my_email = os.environ.get("EMAIL")
    pwd = os.environ.get("EMAIL_PWD")
    receiver_email = to_email

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=pwd)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=receiver_email,
            msg=message
        )


today = dt.datetime.now()
today_tuple = (today.month, today.day)


data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}


if today_tuple in birthdays_dict:
    birthday_person = str(birthdays_dict[today_tuple]["name"])
    birthday_person_email = birthdays_dict[today_tuple].email
    file_path = f"./letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as file:
        text = file.read()
        new_text = text.replace("[NAME]", birthday_person).replace("Angela", "Nauman")

    final_text = f"Subject:Happy Birthday!\n\n{new_text}"
    print(final_text)

    send_email(final_text, birthday_person_email)


