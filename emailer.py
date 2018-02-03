import mails
import schedule
import weather

def main():
    schedules = schedule.get_schedule()
    emails = mails.get_emails()
    forecast = weather.get_weather_forecast()
    mails.send_emails(emails, schedules, forecast)

main()
