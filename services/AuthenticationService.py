import json
import hashlib

from errors.InvalidUsage import InvalidUsage
from models.Companies import Companies
from models.Otp import Otp
from services.CodeService import CodeService
from services.EmailService import EmailService
from services.TokenService import TokenService


class AuthenticationService:

    def __init__(self):
        self.emailService = EmailService()
        self.tokenService = TokenService()

    @staticmethod
    def verify_email(email):
        return Companies.objects(email=email, deleted_at='')

    def send_code(self, email):
        try:
            user = self.verify_email(email)[0]
            tokens = Otp.objects(company_id=user["id"], deleted_at='')
            for token in tokens:
                token.delete()
        except IndexError:
            raise InvalidUsage(status_code=404, message="Email não encontrado")

        code = CodeService.generate()

        hashed = hashlib.sha1(code.encode('utf-8')).hexdigest()

        Otp(company_id=user['id'], code=hashed).save().to_json()

        self.emailService.send_code(user.email, code)

    def login(self, email, code):
        try:
            user = self.verify_email(email)[0]
            otp = Otp.objects(company_id=user["id"], deleted_at='').order_by('-created_at')[0]
        except IndexError:
            raise InvalidUsage(status_code=404, message="Email ou OTP não encontrado")

        if otp.code != hashlib.sha1(code.upper().encode('utf-8')).hexdigest():
            raise InvalidUsage(status_code=401, message="Código OTP incorreto")

        token = self.tokenService.generate(json.loads(user.to_json()))

        data = {"token": token, "user": json.loads(user.to_json())}

        otp.delete()

        return data

    @staticmethod
    def create(data):

        return Companies(
                email=data[0],
                name=data[1],
                cnpj=data[2]
        ).save()
