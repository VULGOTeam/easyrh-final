from flask import request

from controllers.EmployeesController import EmployeesController
from controllers.SalaryController import SalaryController
from controllers.AuthenticationController import AuthenticationController
from services.TokenService import TokenService


class Routes:
    def __init__(self, application):
        self.tokenService = TokenService()
        self.salaryController = SalaryController()
        self.authenticationController = AuthenticationController()
        self.employeesController = EmployeesController()

        @application.route('/')
        def _home():
            return 'ok'

        # Users Routes
        @application.route('/users/sign-in', methods=['POST'])
        def _sign_in():
            return self.authenticationController.login(request)

        @application.route('/users/sign-in', methods=['PUT'])
        def _verify_otp():
            return self.authenticationController.verify_otp(request)

        @application.route('/users', methods=['POST'])
        def _sign_up():
            return self.authenticationController.register(request)

        @application.route('/users/me', methods=['GET'])
        def _user_details():
            return self.authenticationController.me(request)

        # Employees Routes
        @application.route('/employees', methods=['GET'])
        def _employees_index():
            self.authenticationController.validate(request)
            return self.employeesController.index(request)

        @application.route('/employees', methods=['POST'])
        def _employees_create():
            self.authenticationController.validate(request)
            return self.employeesController.create(request)

        @application.route('/employees/<id>', methods=['GET'])
        def _employees_view(id):
            self.authenticationController.validate(request)
            return self.employeesController.view(request)

        @application.route('/employees/<id>', methods=['DELETE'])
        def _employees_delete(id):
            self.authenticationController.validate(request)
            return self.employeesController.delete(request)

        # Other Routes
        @application.route('/salary/calculate', methods=['get'])
        def _calculate():
            self.authenticationController.validate(request)
            return self.salaryController.index(request)
