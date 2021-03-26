from investment import analyzeDeal 

# murray hill 2-4
# 126 dom
# repair: 2,750
# capEx 2,160
# https://my.flexmls.com/chrisantonicci/search/saved_searches/20210317211216945809000000/listings/20201113015244957200000000

# Current Price
# Market rents
# 2 bed 1000
# 4 bed 1800
analyzeDeal(propertyPrice=275000,
  downPayment=12000,
  interestRate=0.035,
  yearlyPropertyTaxes=8342,
  yearlyLandlordInsurance=1400,
  scheduledMonthlyIncome=2800,
  totalSquareFeet=1650,
  lotSize=0.1,
  additionalOperatingExpenses=4910,
  log=True)
