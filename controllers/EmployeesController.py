from models.Employees import Employees
from flask import Response
from errors.InvalidUsage import InvalidUsage


class EmployeesController:
    @staticmethod
    def index(request):
        employees = Employees.objects(company_id=request.user["id"], deleted_at='')
        return Response(employees.to_json(), mimetype="application/json")

    @staticmethod
    def view(request):
        try:
            employee = Employees.objects(id=request.view_args["id"], company_id=request.user["id"], deleted_at='')[0]
        except IndexError:
            raise InvalidUsage(status_code=404, message="Funcionário não encontrado")

        return Response(employee.to_json(), mimetype="application/json")

    @staticmethod
    def create(request):
        body = request.get_json(force=True)

        try:
            # Required Fields
            [name, gross, hired_at] = [
                body['name'],
                body['gross'],
                body['hired_at']
            ]
        except KeyError:
            raise InvalidUsage(status_code=400, message="Campos obrigatórios não preenchidos")

        employee = Employees(
            company_id=request.user['id'],
            name=name,
            gross=gross,
            hired_at=hired_at,
            data=body.get('data'),
            vacations=body.get('vacations'),
            department=body.get('department'),
        ).save()

        return Response(employee.to_json(), mimetype="application/json")


    def update(self, request):
        pass

    @staticmethod
    def delete(request):
        try:
            employee = Employees.objects(id=request.view_args["id"], company_id=request.user["id"], deleted_at='')[0]
        except IndexError:
            raise InvalidUsage(status_code=404, message="Funcionário não encontrado")

        employee.delete()

        return Response(employee.to_json(), mimetype="application/json")
