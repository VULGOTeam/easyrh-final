class SalaryService:
    def total(self, salary, vacation, thirteenth, adds, months):

        totalLiquid = (salary["liquid"]*months) + vacation["liquid"] + thirteenth["liquid"] + adds
        totalGross = (salary["gross"] * months) + vacation["gross"] + thirteenth["gross"] + adds

        response = {
            "liquid": totalLiquid,
            "gross": totalGross,
            "taxes": totalGross - totalLiquid,
            "adds": adds,
            "months": months,
            "vacation_days": vacation["days"]
        }

        return response
