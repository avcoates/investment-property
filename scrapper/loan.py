import math 

monthsInYear = 12

def getMonthlyPrincipalAndInterest(principal, interestRate, yearsOfLoan):
    monthlyInterestRate = interestRate / monthsInYear
    totalPayments = yearsOfLoan * monthsInYear

    numerator = monthlyInterestRate * math.pow((monthlyInterestRate + 1), totalPayments)
    denominator = math.pow((1 + monthlyInterestRate), totalPayments) - 1

    return principal * (numerator/denominator)


def getMonthlyMIP(principal):
    MIPRate = 0.0085;

    return principal * MIPRate / monthsInYear


def getMonthlyPrincipalAndIntrestTaxesAndInsurance(principal, downPayment, interestRate, yearsOfLoan, yearlyPropertyTaxes, yearlyLandlordInsurance):
    monthlyPrincipalAndIntrest = getMonthlyPrincipalAndInterest(principal, interestRate, yearsOfLoan)
    monthlyMIP = getMonthlyMIP(principal)
    monthlyTaxes = yearlyPropertyTaxes / monthsInYear
    insurance = yearlyLandlordInsurance / monthsInYear

    return monthlyPrincipalAndIntrest + monthlyMIP + monthlyTaxes + insurance


def getUpFrontInvestment(purchasePrice, downPayment):
    upFrontMIP = 0.0175

    return downPayment + purchasePrice * upFrontMIP