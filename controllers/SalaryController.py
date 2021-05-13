from errors.InvalidUsage import InvalidUsage
from services.SalaryService import SalaryService
from services.TaxasService import TaxasService
from services.ThirteenthService import ThirteenthService
from services.VacationService import VacationService


class SalaryController:
    def __init__(self):
        try:
            self.taxasService = TaxasService()
            self.vacationService = VacationService()
            self.thirteenthService = ThirteenthService()
            self.salaryService = SalaryService()
        except:
            raise InvalidUsage("Server Error", status_code=500)

    def index(self, request):
        try:
            gross = float(request.args.get('gross'))
            months = int(request.args.get('months'))
            days = int(request.args.get('vacation_days') or 30)
            adds = float(request.args.get('adds') or 0)
        except (ValueError, TypeError):
            raise InvalidUsage("Bad Request", status_code=400)

        try:
            salary = self.taxasService.calculate(gross)
            vacation = self.vacationService.get(gross, days)
            thirteenth = self.thirteenthService.get(gross, months)
            total = self.salaryService.total(salary, vacation, thirteenth, adds, months)
        except InvalidUsage as e:
            raise e
        except:
            raise InvalidUsage("Server Error", status_code=500)

        return {
            "salary": salary,
            "vacation": vacation,
            "thirteenth": thirteenth,
            "total": total
        }
