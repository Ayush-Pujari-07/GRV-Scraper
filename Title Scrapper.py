from bs4 import BeautifulSoup
import pandas as pd
import time
from urllib.request import Request, urlopen
import logging

logging.basicConfig(filename='Logger.txt', level=logging.DEBUG, format=' %(asctime)s %(name)s %(message)s')


# Function for the extraction of the HREF LINKS.
def extract_links(args):
    hrefs = []
    hrefs = set([l.get('href') for l in args])
    link_pages = []
    for i in hrefs:
        if i != '/ongoing-pipeline-reports' and i != '/ongoing-reports':
            link_pages.append(i)
    return link_pages


newlist = []
try:
    logging.info('Extraction started !!')
    # Get the Url oF the Website
    url = str(input(f"Input the URL For Scrapping:\n"))
    # NEw way to get the details of the page that is using security for bot
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    web_byte = urlopen(req).read()
    # opening the webpage in UTF-8
    webpage = web_byte.decode('utf-8')
    # parsing the html using beautiful soup
    soup = BeautifulSoup(webpage, 'html.parser')
    # getting list through the id='showResultHere'
    List_ids = soup.find(class_="col-sm-9 col-md-9 col-xs-12")
    # href string list to get the href extracted calling anchor or a tag
    href = List_ids.find_all('a')
    # Call the function for extraction of all URL and turn it into a list
    href_extracted = []
    href_extracted = extract_links(href)
    # This is complete the lisk so it could be executable
    links_prefix = 'https://www.grandviewresearch.com/'
    for i in href_extracted:
        newlist.append(links_prefix + i)
    logging.info(url)
except Exception as e:
    logging.info('There is an ERROR!!')
    logging.error(e)
    pass

logging.info('The Extraction is complete')
time.sleep(10)

df = pd.DataFrame()

Name = str(url).split('/')[4]

df[f'{Name}'] = newlist

logging.info('The extraction is loaded to data frame')
df.to_excel(f'C:\\Users\\user\\Desktop\\Project\\GVR_Scrapper\\Extraceted files\\{Name}.xlsx')
logging.info('EXCEL File is Created!!!!')
