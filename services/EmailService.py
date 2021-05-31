import sendgrid
import os
from sendgrid.helpers import mail
from errors.InvalidUsage import InvalidUsage


class EmailService:
    def __init__(self):
        self.sendgrid = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_CLIENT"))
        self.mail = mail
        self.fromEmail = "mateus.jpt@puccampinas.edu.br"
        self.templateId = "d-8ffe69e1bb7c430c880d027e01f41ced"

    def sendCode(self, email, code):
        message = mail.Mail(
            from_email=self.fromEmail,
            to_emails=email,
        )

        message.dynamic_template_data = {
            'code': code
        }

        message.template_id = self.templateId

        try:
            response = self.sendgrid.send(message)
        except Exception as e:
            print("Error: {0}".format(e))
            raise InvalidUsage(status_code=500, message="Could not send the email")
        return str(response.status_code)
