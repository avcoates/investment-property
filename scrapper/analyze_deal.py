from loan import getMonthlyPrincipalAndInterest, getMonthlyPrincipalAndIntrestTaxesAndInsurance, getUpFrontInvestment, getMonthlyMIP

milwaukeeMultiFamilyCAPRate = 0.055
milwaukeeVaccancyRate = 0.051
conservativeMilwaukeeVaccancyRate = 0.08
monthsInYear = 12
yearsOfLoan = 30 # for my case

def getVaccancyRateExpense(income, log=False):
    vaccancyExpense = milwaukeeVaccancyRate * income

    if (log):
        print('Vaccancy Rate: ', milwaukeeVaccancyRate)
        print('Vaccancy Expense: ', vaccancyExpense)
    
    return vaccancyExpense

# All revenue from property minus reasonable operating expenses.
# Operating expense: normal business operation expense.
#                ex: taxes, insurance, common electric, any owner covered utilities, maintenence/upkeep
def getNetOperatingIncome(scheduledIncome, taxesAndInsurance, otherOperatingExpenses, log=False):
    if (log):
        print('Scheduled Income: ', scheduledIncome)

    vaccancy = getVaccancyRateExpense(scheduledIncome)
    actualIncome = scheduledIncome - vaccancy
    netOperatingExpenses = taxesAndInsurance + otherOperatingExpenses
    netOperatingIncome = actualIncome - netOperatingExpenses

    if (log):
        print('Actual Income: ', actualIncome)
        print('Net Operating Expenses: ', netOperatingExpenses)
        print('Net Operating Income: ', netOperatingIncome)

    return netOperatingIncome

# Capitalization Rate - indicates the rate of return
# Most useful as a comparison of relative value of similar real estate investments
def getCapitalizationRate(NOI, propertyValue):
    return NOI / propertyValue * 100

# Cash on cash return measures the annual return in relation to the initial investment
def getCashOnCash(cashFlow, totalInitialInvestment):
    return cashFlow / totalInitialInvestment * 100

# ROI
# def getReturnOnInvestment(yearlyCashFlow, totalInitialInvestment):
#     return (yearlyCashFlow / totalInitialInvestment) * 100

# Net operating income - net operating expenses
def getCashFlow(NOI, NOE):
    return NOI - NOE

def analyzeDeal(propertyPrice, downPayment, interestRate, yearlyPropertyTaxes, yearlyLandlordInsurance, scheduledMonthlyIncome, totalSquareFeet, lotSize, additionalOperatingExpenses, log=False):
    principal = propertyPrice - downPayment
    monthlyPITI = getMonthlyPrincipalAndIntrestTaxesAndInsurance(principal, downPayment, interestRate, yearsOfLoan, yearlyPropertyTaxes, yearlyLandlordInsurance)
    monthlyPI = getMonthlyPrincipalAndInterest(principal, interestRate, yearsOfLoan)
    monthlyPMI = getMonthlyMIP(principal)
    monthlyTaxes = yearlyPropertyTaxes / 12
    monthlyInsurance = yearlyLandlordInsurance / 12
    totalInitialInvestment = getUpFrontInvestment(propertyPrice, downPayment)
    PITI = monthlyPITI * 12
    PMI = monthlyPMI * 12
    PI = monthlyPI * 12

    print('PITI ', end='')
    print(PITI)

    print('additionalOperatingExpenses ', end='')
    print(additionalOperatingExpenses)

    print('monthlyPITI ', end='')
    print(monthlyPITI)

    print('monthlyPI ', end='')
    print(monthlyPI)

    print('monthlyPMI ', end='')
    print(monthlyPMI)

    print('monthlyTaxes ', end='')
    print(monthlyTaxes)

    print('monthlyInsurance ', end='')
    print(monthlyInsurance)


    print('')

    NOI = getNetOperatingIncome(scheduledMonthlyIncome * monthsInYear, (yearlyPropertyTaxes + yearlyLandlordInsurance), additionalOperatingExpenses, log)
    capRate = getCapitalizationRate(NOI, propertyPrice)
    cashFlow = getCashFlow(NOI, PI)
    # ROI = getReturnOnInvestment(cashFlow, totalInitialInvestment)
    cashOnCash = getCashOnCash(scheduledMonthlyIncome, totalInitialInvestment)

    print('capRate ', end='')
    print(capRate)

    print('cashFlow ', end='')
    print(cashFlow)

    print('cashFlow with 10% prop. mang', end='')
    print(cashFlow - ((scheduledMonthlyIncome * monthsInYear) * .1))

    print('cashOnCash ', end='')
    print(cashOnCash)
