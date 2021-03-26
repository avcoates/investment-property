from investment import analyzeDeal 

# 2-2-1
# repairs 2,849
# capEx 2,160
# https://my.flexmls.com/chrisantonicci/search/saved_searches/20210317211216945809000000/listings/20210111213741378035000000

# Current price
# current rent
# analyzeDeal(propertyPrice=284900,
#     downPayment=12000,
#     interestRate=0.035,
#     yearlyPropertyTaxes=6613,
#     yearlyLandlordInsurance=1500,
#     scheduledMonthlyIncome=2520,
#     totalSquareFeet=1650,
#     lotSize=0.1,
#     additionalOperatingExpenses=5009,
#     log=True)


# Current price
# Market rent 2 bed 1000 x 2, 1 bed 900 x 1
# analyzeDeal(propertyPrice=284900,
#     downPayment=12000,
#     interestRate=0.035,
#     yearlyPropertyTaxes=6613,
#     yearlyLandlordInsurance=1500,
#     scheduledMonthlyIncome=2900,
#     totalSquareFeet=1650,
#     lotSize=0.1,
#     additionalOperatingExpenses=5009,
#     log=True)

analyzeDeal(propertyPrice=180000,
    downPayment=12000,
    interestRate=0.035,
    yearlyPropertyTaxes=3812,
    yearlyLandlordInsurance=1500,
    scheduledMonthlyIncome=1900,
    totalSquareFeet=1650,
    lotSize=0.1,
    additionalOperatingExpenses=5009,
    log=True)