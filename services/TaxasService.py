import json

from models.Taxes import Taxes


class TaxasService:
    def calculate(self, gross):
        taxes = self.taxes(gross)

        response = {
            "liquid": round(gross - taxes["descontos"][0] - taxes["descontos"][1], 2),
            "gross": round(gross, 2),
            "taxes": taxes
        }

        return response

    def taxes(self, bruto):
        inss = float(0.0)
        irrf = float(0.0)

        # Calculo INSS
        try:
            taxaInss = json.loads(Taxes.objects(
                __raw__={
                    'year': '2021',
                    'type': 'inss',
                    'range.0': {'$lte': bruto},
                    'range.1': {'$gte': bruto}
                }
            )[0].to_json())
            inss = (bruto * (taxaInss["aliquot"] / 100)) - taxaInss["deduction"]

            inss = round(inss, 2)
        except IndexError:
            taxaInss = {
                'aliquot': 0.0,
                'deduction': 0.0
            }
            pass

        # Calculo IRRF
        brutoINSS = bruto - inss

        try:
            taxaIrrf = json.loads(Taxes.objects(
                __raw__={
                    'year': '2021',
                    'type': 'irrf',
                    'range.0': {'$lte': brutoINSS},
                    'range.1': {'$gte': brutoINSS}
                }
            )[0].to_json())

            irrf = (brutoINSS * (taxaIrrf["aliquot"] / 100)) - taxaIrrf["deduction"]

            irrf = round(irrf, 2)
        except IndexError:
            taxaIrrf = {
                'aliquot': 0.0,
                'deduction': 0.0
            }
            pass

        # Fim Calculos Taxas
        return {
            'descontos': [inss, irrf],
            "taxas": {
                "inss": taxaInss,
                "irrf": taxaIrrf
            }
        }
