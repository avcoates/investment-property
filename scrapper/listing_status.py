from enum import Enum

class ListingStatus(Enum):
    All = 0
    Active = 'Active'
    NewListing = 'New Listing'
    Contingent = 'Active (C)'
    Pending = 'Pending'
    Sold = 'Sold'