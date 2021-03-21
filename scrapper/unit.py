def Unit:
    numberOfRooms = 0
    fullBaths = 0
    halfBaths = 0
    rent = 0
    squareFeet = 0
    vaccancy = ''
    leaseExpires = Date()

    def __init__(self, numberOfRooms, fullBaths, halfBaths, rent, squareFeet, vaccancy, leaseExpires):
        self.numberOfRooms = numberOfRooms
        self.fullBaths = fullBaths
        self.halfBaths = halfBaths
        self.rent = rent
        self.squareFeet = squareFeet
        self.vaccancy = vaccancy
        self.leaseExpires = leaseExpires