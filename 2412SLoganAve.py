from investment import analyzeDeal 

# https://my.flexmls.com/chrisantonicci/search/saved_searches/20210317211216945809000000/listings/20210322124912101637000000
# bay view
# 2/2

# reparis (1% of home value) 2,500
# water bill 600 per year avg single fam x 2 600
# Current Price
# Current Rent 1000, 850
# ---------------
# PITI                        17842.22859502294
# additionalOperatingExpenses 3000
# monthlyPITI                 1486.8523829185783
# monthlyPI                   911.5607162519116
# monthlyPMI                  143.79166666666669
# monthlyTaxes                306.5
# monthlyInsurance            125.0

# Scheduled Income:           22200
# Actual Income:              21067.8
# Net Operating Expenses:     8178
# Net Operating Income:       12889.8
# capRate                     5.995255813953488
# cashFlow                    1951.0714049770613
# cashFlow with 10% PM       -268.9285950229387
# cashOnCash                  11.736716891356066
# analyzeDeal(propertyPrice=215000,
#     downPayment=12000,
#     interestRate=0.035,
#     yearlyPropertyTaxes=3678,
#     yearlyLandlordInsurance=1500,
#     scheduledMonthlyIncome=1850,
#     totalSquareFeet=1650,
#     lotSize=0.1,
#     additionalOperatingExpenses=5285,
#     log=True)

# Current Price
# Market rents 1100, 1100
# ---------------
# PITI                        18091.770045171175
# additionalOperatingExpenses 3000
# monthlyPITI                 1507.6475037642647
# monthlyPI                   929.5225037642646
# monthlyPMI                  146.62500000000003
# monthlyTaxes                306.5
# monthlyInsurance            125.0

# Scheduled Income:           26400
# Actual Income:              25053.6
# Net Operating Expenses:     8178
# Net Operating Income:       16875.6
# capRate                     7.849116279069766
# cashFlow                    5721.329954828823
# cashFlow with 10% PM        3081.3299548288232
# cashOnCash                  18.703506907545165
# analyzeDeal(propertyPrice=215000,
#     downPayment=8000,
#     interestRate=0.035,
#     yearlyPropertyTaxes=3678,
#     yearlyLandlordInsurance=1500,
#     scheduledMonthlyIncome=2200,
#     totalSquareFeet=1650,
#     lotSize=0.1,
#     additionalOperatingExpenses=5285,
#     log=True)


# High price
# Market Rents
# ---------------
# PITI                        20275.257733968236
# additionalOperatingExpenses 3000
# monthlyPITI                 1689.6048111640196
# monthlyPI                   1086.6881444973528
# monthlyPMI                  171.41666666666666
# monthlyTaxes                306.5
# monthlyInsurance            125.0

# Scheduled Income:           26400
# Actual Income:              25053.6
# Net Operating Expenses:     8178
# Net Operating Income:       16875.6
# capRate                     6.750239999999999
# cashFlow                    3835.3422660317647
# cashFlow with 10% PM        1195.3422660317647
# cashOnCash                  17.77777777777778
analyzeDeal(propertyPrice=250000,
    downPayment=8000,
    interestRate=0.035,
    yearlyPropertyTaxes=3678,
    yearlyLandlordInsurance=1500,
    scheduledMonthlyIncome=2200,
    totalSquareFeet=1650,
    lotSize=0.1,
    additionalOperatingExpenses=5285,
    log=True)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Owner Occupied, high price, market rent
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# No roommate
# Cost to live: -8691.457733968235
# analyzeDeal(propertyPrice=250000,
#     downPayment=8000,
#     interestRate=0.035,
#     yearlyPropertyTaxes=3678,
#     yearlyLandlordInsurance=1500,
#     scheduledMonthlyIncome=1100,
#     totalSquareFeet=1650,
#     lotSize=0.1,
#     additionalOperatingExpenses=3000,
#     log=True)

# Roommate + 600
# Cost to live: -1858.6577339682353
# analyzeDeal(propertyPrice=250000,
#     downPayment=8000,
#     interestRate=0.035,
#     yearlyPropertyTaxes=3678,
#     yearlyLandlordInsurance=1500,
#     scheduledMonthlyIncome=1700,
#     totalSquareFeet=1650,
#     lotSize=0.1,
#     additionalOperatingExpenses=3000,
#     log=True)