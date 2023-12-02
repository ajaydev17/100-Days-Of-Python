import smtplib

user = ""
password = ""
to_address = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=user, password=password)
    connection.sendmail(
        from_addr=user,
        to_addrs=to_address,
        msg=f"Subject: Hello\n\nThis is a test email!!"
    )
