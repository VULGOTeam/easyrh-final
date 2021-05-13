from services.TaxasService import TaxasService
from errors.InvalidUsage import InvalidUsage


class VacationService:
    def __init__(self):
        self.taxasService = TaxasService()

    def get(self, gross, days=30):

        if days > 30:
            raise InvalidUsage("Férias acima do total permitido (30 dias)", status_code=400)

        oneThird = round(gross / 3, 2)
        gross = gross + oneThird
        days = days

        taxes = self.taxasService.calculate((gross / 30) * days)

        response = {
            "days": days,
            "one_third": oneThird
        }
        response.update(taxes)

        return response
