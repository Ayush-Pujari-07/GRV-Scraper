import pandas as pd

data_frame = pd.read_excel('C:\\Users\\user\\Desktop\\Project\\GVR_Scrapper\\Complete '
                           'Lists\\bulk-chemicals_Complete_List.xlsx')

for titles in data_frame['Title'][1:10]:
    print(titles)

