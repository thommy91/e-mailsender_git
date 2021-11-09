import smtplib

my_email = "thomas91code@gmail.com"
password = "??????????"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)

    connection.sendmail(
                        from_addr=my_email, 
                        to_addrs="thomas_aj_9@hotmail.com", 
                        msg="Subject: Hello test\n\n This is the body of the e-mail"
                        )

