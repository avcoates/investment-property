from investment import analyzeDeal 

# murray hill
# 1-5
# owner pays none
# https://my.flexmls.com/chrisantonicci/search/saved_searches/20210317211216945809000000/listings/20210111215144498426000000
# repairs 1% 2,500
# capEx 2,160


# Current price
# current rent
# https://my.flexmls.com/chrisantonicci/search/saved_searches/20210317211216945809000000/listings/20210111215144498426000000
analyzeDeal(propertyPrice=249900,
    downPayment=12000,
    interestRate=0.035,
    yearlyPropertyTaxes=5940,
    yearlyLandlordInsurance=1500,
    scheduledMonthlyIncome=2265,
    totalSquareFeet=1650,
    lotSize=0.1,
    additionalOperatingExpenses=4660,
    log=True)
# 
# Current price
# market rent
# 1 bed x 1 900
# 5 bed x 1 2000
# https://my.flexmls.com/chrisantonicci/search/saved_searches/20210317211216945809000000/listings/20210111215144498426000000
analyzeDeal(propertyPrice=249900,
    downPayment=12000,
    interestRate=0.035,
    yearlyPropertyTaxes=5940,
    yearlyLandlordInsurance=1500,
    scheduledMonthlyIncome=2900,
    totalSquareFeet=1650,
    lotSize=0.1,
    additionalOperatingExpenses=4660,
    log=True)


analyzeDeal(propertyPrice=249900,
    downPayment=12000,
    interestRate=0.035,
    yearlyPropertyTaxes=5940,
    yearlyLandlordInsurance=1500,
    scheduledMonthlyIncome=1800,
    totalSquareFeet=1650,
    lotSize=0.1,
    additionalOperatingExpenses=4660,
    log=True)