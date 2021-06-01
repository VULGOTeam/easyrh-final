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
            return 'ok'

        @app.route('/users/sign-in', methods=['POST'])
        def _sign_in():
            return self.authenticationController.login(request)

        @app.route('/users/sign-in', methods=['PUT'])
        def _verify_otp():
            return self.authenticationController.verify_otp(request)

        @app.route('/users', methods=['POST'])
        def _sign_up():
            return self.authenticationController.register(request)

        @app.route('/salary/calculate', methods=['GET'])
        def _calculate():
            return self.salaryController.index(request)

        @app.route('/users/sign-in', methods=['POST'])
        def _signIn():
            return self.authenticationController.login(request)
