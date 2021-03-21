class property:
    id = ''
    status = ''
    daysOnMarket = 0
    streetAddress = ''
    postalMunicipality = ''
    buildYear = 0
    price = 0
    propertyTaxes = 0
    squareFeet = 0
    lotSize = 0
    units = []
    garageSpaces = 0

    def __init__(self,
        id,
        status, 
        daysOnMarket,
        streetAddress,
        postalMunicipality,
        buildYear,
        price,
        propertyTaxes,
        squareFeet,
        lotSize,
        units,
        garageSpaces):

        self.id = id                  
        self.status = status
        self.daysOnMarket = daysOnMarket
        self.streetAddress = streetAddress
        self.postalMunicipality = postalMunicipality
        self.buildYear = buildYear
        self.price = price
        self.propertyTaxes = propertyTaxes
        self.squareFeet = squareFeet
        self.lotSize = lotSize
        self.units = units
        self.garageSpaces = garageSpaces       
