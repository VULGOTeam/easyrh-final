from flask import Response, jsonify
from services.AuthenticationService import AuthenticationService
from errors.InvalidUsage import InvalidUsage
from services.EmailService import EmailService

class AuthenticationController:
    def __init__(self):
        self.authenticationService = AuthenticationService()
        self.emailService = EmailService()

    def login(self, request):
        body = request.get_json(force=True)

        try:
            email = body['email']
        except KeyError:
            raise InvalidUsage(status_code=400, message="Digite o email!")

        try:
            self.authenticationService.send_code(email=email)
        except InvalidUsage as e:
            raise e
        except Exception as e:
            print(e)
            raise InvalidUsage(status_code=500, message="Falha ao procurar usuário")

        raise InvalidUsage(status_code=201, message="Código enviado com sucesso!")

    def verify_otp(self, request):
        body = request.get_json(force=True)

        try:
            email = body['email']
            otp = body['otp']
        except KeyError:
            raise InvalidUsage(status_code=400, message="Verifique os dados")

        data = self.authenticationService.login(email, otp)

        return jsonify(data)

    def register(self, request):
        body = request.get_json(force=True)

        try:
            data = [body['email'], body['name'], body['cnpj']]
        except KeyError:
            raise InvalidUsage(status_code=400, message="Verifique os dados")

        try:
            user = self.authenticationService.verify_email(data[0])
        except Exception as e:
            print(e)
            raise InvalidUsage(status_code=500, message="Falha ao criar o usuário")

        if len(user) > 0:
            raise InvalidUsage(status_code=401, message="Email já cadastrado")

        try:
            user = self.authenticationService.create(data)
        except Exception as e:
            print(e)
            raise InvalidUsage(status_code=500, message="Falha ao criar o usuário")

        return Response(user.to_json(), mimetype='application/json')

    def me(self, request):
        return jsonify(self.authenticationService.me(request.headers.get("Authorization")))
