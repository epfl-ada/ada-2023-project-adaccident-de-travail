import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import requests
from bs4 import BeautifulSoup

# Extract all characters until the next non-numerical character
def extract_ID(html_extract):
    """
    Extracts the Wikidata ID from a string.

    Args:
    html_extract (str): The string to extract the ID from.

    Returns:
    str: The Wikidata ID extracted from the string.
    """

    new_ID = []
    start_ID = False
    for i in range(len(html_extract)):
        if html_extract[i] == 'Q':
            new_ID.append(html_extract[i])
            start_ID = True
            break
    if start_ID == True:
        for j in range(i+1, len(html_extract)):
            if html_extract[j].isdigit():
                new_ID.append(html_extract[j])
            else:
                break
    return new_ID

def scrape_wikidata_id(db, index):
    """
    Scrapes the Wikidata ID for a given movie from its Wikipedia page.

    Args:
    db (pandas.DataFrame): The dataframe containing the movie metadata.
    index (int): The index of the movie in the dataframe to scrape the ID for.

    Returns:
    str: The Wikidata ID for the movie.
    """
        
    # specify the wikipedia page url
    url = "https://en.wikipedia.org/wiki/index.php?curid=" + str(db['WikipediaID'][index])

    # make a request to the url 
    response = requests.get(url)

    # parse the html content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    id_index = soup.prettify().find('https://www.wikidata.org/wiki/')
    wikidata_id = soup.prettify()[id_index+40:id_index+70]

    return "".join(extract_ID(wikidata_id))

def scrape_sequels(db, index):
    """
    Scrapes the prequel and sequel IDs for a given movie from its Wikidata page.

    Args:
    db (pandas.DataFrame): The dataframe containing the movie metadata.
    index (int): The index of the movie in the dataframe to scrape the IDs for.

    Returns:
    list: A list containing the prequel and sequel IDs for the movie.
    """
    
    sequel_ID = ["", ""]
    
    # test url 
    # url = 'https://www.wikidata.org/wiki/Q4786598'

    # specify the wikipedia page url
    url = "https://www.wikidata.org/wiki/" + str(db['WikidataID'][index])

    # make a request to the url 
    response = requests.get(url)

    # parse the html content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # looking if the prequel and sequel index on the page exist
    prequel_index = soup.prettify().find('follows')
    sequel_index = soup.prettify().find('followed by')
    
    # if the prequel and sequel index exist, find the first time the string '<a title="Q' appears after the index
    if prequel_index != -1:
        prequel_index_2 = soup.prettify()[prequel_index:].find('<a ')
        wikidata_id = soup.prettify()[prequel_index + prequel_index_2 : prequel_index + prequel_index_2 + 300]
        sequel_ID[0] = "".join(extract_ID(wikidata_id))
    else: 
        sequel_ID[0] = "NaN"

    if sequel_index != -1:
        sequel_index_2 = soup.prettify()[sequel_index:].find('<a ')
        wikidata_id = soup.prettify()[sequel_index + sequel_index_2 : sequel_index + sequel_index_2 + 300]
        sequel_ID[1] = "".join(extract_ID(wikidata_id))
    else:
        sequel_ID[1] = "NaN"

    return sequel_ID

# load the csv separated by , and with the first row as the header
original_df = pd.read_csv('./online_scraping_all.csv', sep=',', header=0)

no_value = []
duplicate = []

# go through each row in the original dataset : if there is no value for the WikidataID, add it to the no_value dataframe. If the WikidataID is the same as the PrequelID or SequelID add it to the duplicate dataframe.
for index, row in original_df.iterrows():
    if pd.isnull(row['WikidataID']):
        no_value += [row]
    elif row['WikidataID'] == row['PrequelID'] or row['WikidataID'] == row['SequelID']:
        duplicate += [row]

# create a new dataframe with the lists of no_value and duplicate
no_value_df = pd.DataFrame(no_value)
duplicate_df = pd.DataFrame(duplicate)

# add headers to the new dataframes
no_value_df.columns = ['WikipediaID', 'WikidataID', 'PrequelID', 'SequelID']
duplicate_df.columns = ['WikipediaID', 'WikidataID', 'PrequelID', 'SequelID']

# for all items in no_value_df, scrape the WikidataID and the sequels and prequels and add it to the original dataframe
for index, row in no_value_df.iterrows():
    no_value_df['WikidataID'][index] = scrape_wikidata_id(no_value_df, index)
    no_value_df['PrequelID'][index], no_value_df['SequelID'][index] = scrape_sequels(no_value_df, index)

# for the first 100 items in duplicate_df, scrape the sequels and prequels and add it to the original dataframe
for index, row in duplicate_df.iterrows():
    duplicate_df['PrequelID'][index], duplicate_df['SequelID'][index] = scrape_sequels(duplicate_df, index)
   
original_df.to_csv('all_sequel_scraping.csv', sep=',', index=False, encoding='utf-8')