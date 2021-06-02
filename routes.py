from flask import request

from controllers.SalaryController import SalaryController
from controllers.AuthenticationController import AuthenticationController
from services.TokenService import TokenService


class Routes:
    def __init__(self, application):
        self.tokenService = TokenService()
        self.salaryController = SalaryController()
        self.authenticationController = AuthenticationController()

        @application.route('/')
        def _home():
            return 'ok'

        @application.route('/users/sign-in', methods=['POST'])
        def _sign_in():
            return self.authenticationController.login(request)

        @application.route('/users/sign-in', methods=['PUT'])
        def _verify_otp():
            return self.authenticationController.verify_otp(request)

        @application.route('/users', methods=['POST'])
        def _sign_up():
            return self.authenticationController.register(request)

        @application.route('/salary/calculate', methods=['GET'])
        def _calculate():
            self.tokenService.decode(request.headers.get("Authorization"))
            return self.salaryController.index(request)

        @application.route('/users/me', methods=['GET'])
        def _user_details():
            return self.authenticationController.me(request)
