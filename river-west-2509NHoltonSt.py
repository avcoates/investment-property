from investment import analyzeDeal 

# LETS DO A SHOWING
# Riverwest: 3 unit doable
# https://my.flexmls.com/chrisantonicci/search/saved_searches/20210317211216945809000000/listings/20201102183413948103000000?_filter=StandardStatus+Eq+%27Active%27+And+PropertyClass+Eq+%27MultiFamily%27%2C%27Two-Family%27+And+MlsId+Eq+%2720080502212544227270000000%27%2C%2720010602000846355519000000%27+And+ListPrice+Bt+101000.0%2C350000.0+And+Location+Eq+polygon%28%2743.08620585973485+-87.91141425061035%2C43.05422844927357+-87.91016970562744%2C43.05510648324155+-87.88823996472168%2C43.07492161990803+-87.88137350964355%2C43.086832701010216+-87.87832652020263%27%29&listing_id=20210226213707309523000000
# analyzeDeal(propertyPrice=169900,
#     downPayment=12000,
#     interestRate=0.035,
#     yearlyPropertyTaxes=2111,
#     yearlyLandlordInsurance=1000,
#     scheduledMonthlyIncome=1625,
#     totalSquareFeet=1650,
#     lotSize=0.1,
#     additionalOperatingExpenses=7200,
#     log=True)

# avg rent 2 bed 900 X 2 + avg rent 3 unit 1000 X 1
analyzeDeal(propertyPrice=169900,
    downPayment=12000,
    interestRate=0.035,
    yearlyPropertyTaxes=2111,
    yearlyLandlordInsurance=2500,
    scheduledMonthlyIncome=2800,
    totalSquareFeet=1650,
    lotSize=0.1,
    additionalOperatingExpenses=7200,
    log=True)
