from mls_scrapper import getAllListingKeysForSavedSearch, getListing, getListingKeys, getListingDetails
from mls_csv_creator import MLSDailyCSVCreator

bayviewSearchKey = '20201218165702711370000000'

# report = MLSDailyCSVCreator(bayviewSearchKey)
# one = {'living-great_room_level': 'upper', 'living-great_room_length': '16', 'living-great_room_width': '9', 'kitchen_level': 'upper', 'second_bedroom_level': 'upper', 'kitchen_length': '11', 'second_bedroom_length': '12', 'kitchen_width': '9', 'second_bedroom_width': '8', 'master_bedroom_level': 'upper', 'master_bedroom_length': '12', 'master_bedroom_width': '8', 'est_sq_ft_unit_2': '825', 'rent-month_unit_2': '825', 'sec_deposit_unit_2': '1075', 'occupancy_unit_2': 'mtm', 'postal_municipality': 'milwaukee', 'county': '', 'zip_4': '2631', 'flood_plain': 'unknown', 'tax_key_number': '', 'taxes': '6462', 'tax_year': '2020', 'lot_description': 'fenced', 'est_acreage': '012', 'source_est_acreage': 'public_records', 'zoning': '', 'listing_date': 'january_28_2021', 'dom': '43', 'u1__of_rooms': '4', 'u1_bedrooms': '2', 'u1_total_bathrooms': '1', 'u1_full_baths': '1', 'u1_half_baths': '0', 'est_total_sq_ft': '1650', 'u1_rent-mo': '865', 'u1_security_dep': '825', 'u1_mtm-own-vac': 'mtm', '_rooms_u2': '4', 'bedrooms_u2': '2', 'full_baths_u2': '1', 'half_baths_u2': '0', 'est_year_built': '1944', 'source_est_yr_built': 'public_records', 'source_total_sqft': 'public_records', 'garage_spaces': '25', 'garage_type': 'detached', 'school_district': '', 'directions': '', 'inclusions': '2_refrigerators_2_stoves', 'exclusions': 'washer_dryer', 'flyer_headline': "for_more_information_text_'318'_to_414-604-1400"}
# two = {'inclusions': 'refrigerator_x_3_stove_x2_microwave_washer_and_dryer', 'exclusions': 'sellers_personal_property', 'living-great_room_level': 'upper', 'living-great_room_length': '17', 'living-great_room_width': '16', 'kitchen_level': 'upper', 'second_bedroom_level': 'upper', 'kitchen_length': '13', 'second_bedroom_length': '12', 'kitchen_width': '13', 'second_bedroom_width': '10', 'master_bedroom_level': 'upper', 'master_bedroom_length': '16', 'master_bedroom_width': '10', 'est_sq_ft_unit_2': '1173', 'occupancy_unit_2': 'vac', 'postal_municipality': 'milwaukee', 'county': '', 'zip_4': '4501', 'flood_plain': 'no', 'tax_key_number': '', 'taxes': '5728', 'tax_year': '2020', 'est_acreage': '011', 'source_est_acreage': 'public_records', 'zoning': '', 'listing_date': 'march_11_2021', 'dom': '1', 'u1__of_rooms': '7', 'u1_bedrooms': '2', 'u1_total_bathrooms': '1', 'u1_full_baths': '1', 'u1_half_baths': '0', 'est_total_sq_ft': '2412', 'u1_mtm-own-vac': 'vac', '_rooms_u2': '6', 'bedrooms_u2': '2', 'full_baths_u2': '1', 'half_baths_u2': '0', 'est_year_built': '1949', 'source_est_yr_built': 'broker_or_agent', 'source_total_sqft': 'public_records', 'garage_spaces': '2', 'garage_type': 'detached', 'school_district': ''}
# report.addListing(one)
# report.addListing(two)
# report.createReport()


bayviewListingKeys = getAllListingKeysForSavedSearch(bayviewSearchKey)

report = MLSDailyCSVCreator(bayviewSearchKey)

for bayviewListingKey in bayviewListingKeys:
    listingDictionary = getListing(bayviewSearchKey, bayviewListingKey)
    listingDetailsDictionary = getListingDetails(bayviewSearchKey, bayviewListingKey)

    report.addListing(listingDictionary | listingDetailsDictionary)

report.createReport()
# report.out()