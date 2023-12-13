import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "sanjanaarj2003@gmail.com"
    password = "nydq xnka enuu hhqc"    #Google account--Security--App passwords--copypaste

    receiver = "kjai1972@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)