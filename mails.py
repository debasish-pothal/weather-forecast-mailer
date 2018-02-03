import smtplib

def get_emails():
    emails = []

    try:
        email_file = open('mails.txt', 'r')

        for line in email_file:
            (name, email) = line.split(',')
            emails.append({'name':name.strip(), 'email':email.strip()})
    except FileNotFound as err:
        print(err)

    return emails

def send_emails(emails, schedule, forecast):
    server = smtplib.SMTP('smtp.gmail.com', '587')
    server.starttls()

    username = 'username@gmail.com'
    # use your gmail id here and turn on insecure app setting in your mail account
    password = raw_input('Password :')
    server.login(username, password)

    for email in emails:
        message = 'Subject:Weather Report!\nHi ' + email['name'] + ', \n\n' + forecast
        server.sendmail(username, email['email'], message)

    server.quit()