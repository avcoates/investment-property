import urllib.request
import re
from bs4 import BeautifulSoup
import time

baseUrl = 'https://my.flexmls.com/chrisantonicci/search/saved_searches/'
headers = {
    'X-Requested-With': 'XMLHttpRequest'
}

# step 1 ---------------------------------------------------------------------------------------

# helper
def createHeadingsUrl(searchKey, page):
    return baseUrl + str(searchKey) + '/listings?page=' + str(page) + '&_limit=10'

# helper
def getListingKeys(searchKey, page):
    listingKeys = []
    # url =  'https://my.flexmls.com/chrisantonicci/search/saved_searches/20201218165702711370000000/listings?page=1&_limit=10'
    url = createHeadingsUrl(searchKey, page)
    # url = "https://httpbin.org/ip"

    # proxy = '208.80.28.208:8080'
    print(url)
    req = urllib.request.Request(url, headers=headers)
    # req.set_proxy(proxy, 'https')
    with urllib.request.urlopen(req) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        inputListingKeys = soup.find_all(id=re.compile("select_[0-9]+"))

        for listingHeader in inputListingKeys:
            listingKeys.append(listingHeader.get('data-listing-key'))

    return listingKeys

# main step 1
def getAllListingKeysForSavedSearch(searchKey):

    allListingKeys = []

    listingKeys = getListingKeys(searchKey, 1)
    allListingKeys = allListingKeys + listingKeys;

    page = 2;
    while(len(listingKeys) > 0):
        time.sleep(2) # be a good scrapper
        listingKeys = getListingKeys(searchKey, page)
        allListingKeys = allListingKeys + listingKeys;
        page = page + 1

    return allListingKeys;

# step 2 ---------------------------------------------------------------------------------------

# helper
def createListingUrl(searchKey, listingKey):
    return baseUrl + str(searchKey) + '/listings/' + str(listingKey)

# main step 2
def getListing(searchKey, listingKey):
    print('getting listing...', end='', flush=True)
    time.sleep(2) # be a good scrapper
    keyValuePairs = {}

    url = createListingUrl(searchKey, listingKey)

    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        html = response.read()

        soup = BeautifulSoup(html, 'html.parser')
        keyValuePairs['url'] = url
        keyValuePairs['street_address'] = soup.find('div', class_='listing-detail-street-address').text.lower()
        keyValuePairs['city_state_zip'] = soup.find('div', class_='listing-detail-city-state-zip').text.lower()
        keyValuePairs['price'] = soup.find('div', class_='listing-detail-price').text.replace('$', '').replace(',', '').lower()
        keyValuePairs['square_feet'] = soup.find('div', class_='listing-detail-beds-baths-area').find('span').text.lower().replace(',', '').replace('sf', '')

        keyValuePairs['last_modified'] = soup.find_all('div', class_='listing-detail-field-line')[1].text.replace('\n', '').replace('Last Modified', '').strip().lower()
        
        print('done', flush=True)
        return keyValuePairs

# step 3 ---------------------------------------------------------------------------------------

# helper
def createListingDetailUrl(searchKey, listingKey):
    return baseUrl + str(searchKey) + '/listings/' + str(listingKey) + '/report/general'

# helper
def stripBadCharactersHeader(strin):
    return strin.replace('\n', '').strip().replace('\r', '').replace('\n', '').replace('\'', '').replace('\"', '').replace(';', '').replace('&', '').replace('(', '').replace(')', '').replace(':', '').replace('#', '').replace(',', '').replace('$', '').replace(' ', '_').replace('+', '').replace('.', '').replace('/', '-').replace('2nd', 'second')
# helper
def stripBadCharactersValye(strin):
    return strin.replace('\n', '').strip().replace('\r', '').replace('\n', '').replace('\'', '').replace('\"', '').replace(';', '').replace('&', '').replace('(', '').replace(')', '').replace(':', '').replace('#', '').replace(',', '').replace('$', '').replace(' ', '_').replace('+', '').replace('/', '-').replace('2nd', 'second')

# main step 3
def getListingDetails(searchKey, listingKey):
    print('getting listing details...', end='', flush=True)
    time.sleep(2) # be a good scrapper
    keyValuePairs = {}
    url = createListingDetailUrl(searchKey, listingKey)

    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        html = response.read()

        soup = BeautifulSoup(html, 'html.parser')
        fields = soup.find_all('div', class_='listing-detail-custom-field-line')
        for field in fields:
            label = stripBadCharacters(field.contents[1].contents[0]).lower()
            value = stripBadCharacters(field.contents[2]).lower()
            keyValuePairs[label] = value

        moreFields = soup.find_all('div', class_='listing-detail-field-line')
        for field in moreFields:
            label = stripBadCharacters(field.contents[1].contents[0]).lower()
            value = stripBadCharacters(field.contents[2]).lower()
            keyValuePairs[label] = value
        
        print('done', flush=True)
        return keyValuePairs






