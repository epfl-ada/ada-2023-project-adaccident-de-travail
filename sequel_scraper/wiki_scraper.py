import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import requests
from bs4 import BeautifulSoup

# Load the data
DATA_PATH = './MovieSummaries'

# Import tsv file, where each line is a movie and the metadata is separated by tabs
movie = pd.read_csv(DATA_PATH + '/movie.metadata.tsv', sep='\t', header=None)
movie.columns = ['WikipediaID', 'FreebaseID', 'MovieName', 'ReleaseDate', 'BoxOffice', 'Runtime', 'Languages', 'Countries', 'Genres']

#characters = pd.read_csv(DATA_PATH + '/character.metadata.tsv', sep='\t', header=None)
#characters.columns = ['WikipediaID', 'FreebaseID', 'ReleaseDate', 'CharName', 'ActorDOB', 'ActorGender', 'ActorHeight', 'ActorEthnicity', 'ActorName', 'ActorAge', 'FreebaseMapID', 'FreebaseCharID', 'FreebaseActorID']

# Import txt file where the first number is the movie ID and the rest of the line is the plot summary
# plot_summaries = pd.read_csv(DATA_PATH + '/plot_summaries.txt', sep='\t', header=None)

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


# Creating a new pandas to later add the sequel IDs
online_scraping = pd.DataFrame(columns = ['WikipediaID', 'WikidataID', 'PrequelID', 'SequelID'])

# Copying all the wikipedia IDs to the new dataframe
online_scraping['WikipediaID'] = movie['WikipediaID']

#ask user for start and end index
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))

for i in range(start, end):
    online_scraping['WikidataID'][i] = scrape_wikidata_id(online_scraping, i)
    sequel_ID = scrape_sequels(online_scraping, i)
    online_scraping['PrequelID'][i] = sequel_ID[0]
    online_scraping['SequelID'][i] = sequel_ID[1]

#create new document with the results, where the name includes the start and end index
online_scraping.to_csv('online_scraping_' + str(start) + '_' + str(end) + '.csv', sep=',', index=False, encoding='utf-8')