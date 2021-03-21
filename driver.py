from scrapper import getAllListingKeysForSavedSearch, getListing, getListingKeys, getListingDetails, MLSDailyCSVCreator

# bayviewSearchKey = '20201218165702711370000000'

# bayviewListingKeys = getAllListingKeysForSavedSearch(bayviewSearchKey)

# report = MLSDailyCSVCreator(bayviewSearchKey)

# for bayviewListingKey in bayviewListingKeys:
#     listingDictionary = getListing(bayviewSearchKey, bayviewListingKey)
#     listingDetailsDictionary = getListingDetails(bayviewSearchKey, bayviewListingKey)

#     report.addListing(listingDictionary | listingDetailsDictionary)

# report.createReport()


everythingEveryWhereKey = '20210317211216945809000000'

everythingEveryWhereListingKeys = getAllListingKeysForSavedSearch(everythingEveryWhereKey, 1)

report = MLSDailyCSVCreator(everythingEveryWhereKey)

for everythingEveryWhereListingKey in everythingEveryWhereListingKeys:
    listingDictionary = getListing(everythingEveryWhereKey, everythingEveryWhereListingKey)
    listingDetailsDictionary = getListingDetails(everythingEveryWhereKey, everythingEveryWhereListingKey)

    report.addListing(listingDictionary | listingDetailsDictionary)

report.createReport()
