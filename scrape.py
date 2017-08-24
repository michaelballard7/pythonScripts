import requests
from bs4 import BeautifulSoup

# establish the target URL or URL's
base_url = "https://www.yelp.com/search?find_desc=&find_loc="
location = "New York, NY"
search_pg = 0
url = base_url + location + "&start=" + str(search_pg)

# utilize the request get method to get the target url page
yelp_req = requests.get(url)
# use the beautifulsoup library to clean the html text from target site
yelp_soup = BeautifulSoup(yelp_req.text, 'html.parser')
# use the status_code method to from requests library to check for 200 connection
print(" My status code is: " + str(yelp_req.status_code))

 # prints out raw HTML text from the target site
 print(yelp_req.text)

 # The beautifulsoup prettify method allows me to beautify the text extraction from target
 print(yelp_soup.prettify())

 # use methods to target specific element on a page
 print(yelp_soup.title)

 # use the find all method to target all iterations of a specific elements
 print(yelp_soup.find_all('p'))

# build a loop to iterate through all the links on the target site
for link in yelp_soup.find_all('a'):
     print(link)

# I can use the find method instead of find_all
yelp_soup.find_all('li', class_="regular-search-result")

# I can use a dictionary with find_all to extract element with classes and id's
for business in yelp_soup.find_all('a',{"class":'biz-name'}):
    print(business.text)

# organize business information by location and save to a txt file
file_path = 'yelp-{location}.txt'.format(location=location)

# create a loop to write each listing info stored in yelp_soup
with open(file_path, "a") as textfile:
    # Scrape all the business information using find_all and class_ or {'class': 'x'}
    businesses = yelp_soup.find_all('div', class_="biz-listing-large")
    for business in businesses:
        title = business.find_all('a', {'class': 'biz-name'})[0].text
        print(title)
        address = business.find_all('address')[0].text
        print(address)
        print('\n')
        phone = business.find_all('span', {'class':'biz-phone'})[0].text
        print(phone)

        page_line = "{title}\n{address}\n{phone}\n\n".format (
            title = title.encode('utf8'),
            address = address.encode('utf8'),
            phone = phone.encode('utf8')
        )

        # debug UnicodeEncodeError: 'ascii' codec can't encode character u'\u2019' in position 1: ordinal not in range(128)
        textfile.write(page_line)
