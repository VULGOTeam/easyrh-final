from flask import render_template, request

from controllers.SalaryController import SalaryController
from controllers.AuthenticationController import AuthenticationController
from models.Companies import Companies


class Routes:
    def __init__(self, app):
        self.salaryController = SalaryController()
        self.authenticationController = AuthenticationController()

        @app.route('/')
        def _home():
            user = Companies(
                name="Mateus Teste",
                email="mateusjosepretti@gmail.com",
                cnpj="1234567891234567890"
            ).save()
            user.delete()
            return 'ok'

        @app.route('/salary/calculate', methods=['GET'])
        def _calculate():
            return self.salaryController.index(request)

        @app.route('/users/sign-in', methods=['POST'])
        def _signIn():
            return self.authenticationController.login(request)
