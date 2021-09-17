from smtplib import SMTP
import os
import dotenv

dotenv.load_dotenv('.env')


def send_mail():
        try:
            SENDER_EMAIL = os.environ['SENDER_EMAIL']
            PASSWORD = os.environ['PASSWORD']

            RECIPIENT_EMAIL = os.environ['RECIPIENT_EMAIL']

            server = SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(SENDER_EMAIL, PASSWORD)

            subject = 'Theme'
            body = 'Text'
            message = f'Subject: {subject}\n\n{body}'

            server.sendmail(SENDER_EMAIL, [RECIPIENT_EMAIL, ], message)
            server.quit()

            print('Your message has been sent')
        except:
            print('Error')


send_mail()
