from services.TaxasService import TaxasService


class ThirteenthService:
    def __init__(self):
        self.taxasService = TaxasService()

    def get(self, gross, months):

        taxes = self.taxasService.calculate(months * (gross / 12))

        response = {
            "months": months
        }
        response.update(taxes)

        return response
