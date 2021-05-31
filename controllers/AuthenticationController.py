import time

import jwt
from services.CodeService import CodeService
from errors.InvalidUsage import InvalidUsage
from services.EmailService import EmailService


class AuthenticationController:
    def __init__(self):
        self.authenticateUserService = {}
        self.emailService = EmailService()

    def login(self, request):
        body = request.get_json(force=True)

        try:
            email = body['email']
        except KeyError:
            raise InvalidUsage(status_code=400, message="Digite o email!")

        # -- START -- #
        # Change to authenticate with database
        # USE THE SERVICE TO CREATE THE LOGIC, NOT THE CONTROLLER
        if body['email'] == 'mateusjosepretti@gmail.com':
            code = CodeService.generate()
            print(code)
            self.emailService.sendCode(email, code)
            return 'Código enviado com sucesso', 201
        else:
            raise InvalidUsage(status_code=401, message="Email não encontrado!")
        # --- END --- #
