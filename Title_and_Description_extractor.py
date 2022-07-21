from bs4 import BeautifulSoup
import pandas as pd
import logging
import time
from urllib.request import Request, urlopen

# Input the Path where the Excel file located
File_path = input(f'Give the file path:\n')
# read the Excel fil with pandas library
df = pd.read_excel(File_path)
# get the column name form the provided path
list_name = File_path.split('\\')[7].split('.')[0]
# convert the column to the list to iterate the links further
Page_links = df[f'{list_name}'].tolist()

logging.basicConfig(filename=f"C:\\Users\\user\\Desktop\\Project\\GVR_Scrapper\\Logging's\\{list_name}.txt",
                    level=logging.DEBUG, format=' %(asctime)s %(name)s %(message)s')

Title_description = []
Title = []

# To iterate through the links in the page_links

for links in Page_links:
    logging.info(str(links))
    try:
        logging.info('Extraction Started for URL' + str(links))
        url = links
        # NEw way to get the details of the page that is using security for bot
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        web_byte = urlopen(req).read()
        # opening the webpage in UTF-8
        webpage = web_byte.decode('utf-8')
        # TO parse the HTML file
        soup = BeautifulSoup(webpage, 'html.parser')
        # Get the Report description
        x = soup.find(id="rprt_summary").text.strip()
        Title_description.append(x)
        # get the heading for the title.
        y = soup.find(class_="report-title-r").text.strip().split('\n')[0]
        Title.append(y)
        time.sleep(5)
        logging.info('Sleep: 10 Sec')
    except Exception as e:
        logging.info('ERROR has occurred !!!')
        logging.error(e)
        pass
# To create a complete file for the Titles and description.

file = pd.DataFrame()
file['Title'] = pd.Series(Title)
file['Title Description'] = pd.Series(Title_description)

# To store into an Excel file
file.to_excel(f'C:\\Users\\user\\Desktop\\Project\\GVR_Scrapper\\Complete Lists\\{list_name}_Complete_List.xlsx')
