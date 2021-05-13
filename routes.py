from flask import render_template, request

from controllers.SalaryController import SalaryController


class Routes:
    def __init__(self, app):
        self.salaryController = SalaryController()

        @app.route('/')
        def home():
            return render_template('index.html')

        @app.route('/salary/calculate', methods=['GET'])
        def calculate():
            return self.salaryController.index(request)
