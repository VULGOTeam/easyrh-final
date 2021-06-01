taxasFixed = {
    "inss": [
        {
            'aliquota': 7.5,
            'deducao': 0,
            'range': [1100, 1100]
        },
        {
            'aliquota': 9,
            'deducao': 16.50,
            'range': [1100.01, 2203.48]
        },
        {
            'aliquota': 12,
            'deducao': 82.61,
            'range': [2203.49, 3305.22]
        },
        {
            'aliquota': 14,
            'deducao': 148.72,
            'range': [3305.23, 10000000000000000]
        }
    ],
    "irrf": [
        {
            'aliquota': 7.5,
            'deducao': 142.80,
            'range': [1903.99, 2826.65]
        },
        {
            'aliquota': 15,
            'deducao': 354.80,
            'range': [2826.66, 3751.65]
        },
        {
            'aliquota': 22.5,
            'deducao': 636.13,
            'range': [3751.06, 4664.68]
        },
        {
            'aliquota': 27.5,
            'deducao': 869.36,
            'range': [4664.68, 10000000000000000]
        }
    ]
}


class TaxasService:
    @staticmethod
    def get(type):
        if type.lower() == 'inss':
            return taxasFixed["inss"]
        elif type.lower() == 'irrf':
            return taxasFixed["irrf"]
        else:
            raise Exception("NOT_FOUND")

    @staticmethod
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
        def filtroInss(x):
            return bruto >= x['range'][0] and bruto <= x['range'][1]

        try:
            taxaInss = list(filter(filtroInss, self.get("inss")))[0]

            inss = (bruto * (taxaInss["aliquota"] / 100)) - taxaInss["deducao"]

            inss = round(inss, 2)
        except IndexError:
            taxaInss = {
                'aliquota': 0.0,
                'deducao': 0.0
            }
            pass

        # Calculo IRRF
        brutoINSS = bruto - inss

        def filtroIrrf(x):
            return brutoINSS >= x['range'][0] and brutoINSS <= x['range'][1]

        try:
            taxaIrrf = list(filter(filtroIrrf, self.get("irrf")))[0]

            irrf = (brutoINSS * (taxaIrrf["aliquota"] / 100)) - taxaIrrf["deducao"]

            irrf = round(irrf, 2)
        except IndexError:
            taxaIrrf = {
                'aliquota': 0.0,
                'deducao': 0.0
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
