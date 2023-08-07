import smtplib

my_email = "t72189519@gmail.com"
password = "tdqwngwakikmzexk"

with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    connection.starttls() #Encrypting the connection
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="testing12345555@yahoo.com",
        msg="Subject:Happy Birthday!\n\nHello, World!")