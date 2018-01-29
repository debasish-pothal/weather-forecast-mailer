
emails = []

try:
    email_file = open('mails.txt', 'r')

    for line in email_file:
        (name, email) = line.split(',')
        emails.append({'name':name.strip(), 'email':email.strip()})
except FileNotFound as err:
    print(err)

print(emails)

schedule_file = open('schedule.txt', 'r')
schedule = schedule_file.read()

print(schedule)
