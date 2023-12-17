import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import requests
from bs4 import BeautifulSoup


def extract_name(html_extract):
    new_ID = []
    end_ID = False
    start_ID = False
    for i in range(len(html_extract)):
        if start_ID == False:
            if html_extract[i] == '"':
                start_ID = True
        elif start_ID == True:
            if end_ID == False:  
                if html_extract[i] == '"':
                    break
                else:
                    new_ID.append(html_extract[i])
    return new_ID

def extract_date(html_extract):
    new_date = []
    end_ID = False
    start_ID = False
    text_ID = False
    for i in range(len(html_extract)):
        if start_ID == False:
            if html_extract[i] == '\n':
                start_ID = True
        elif start_ID == True:
            if end_ID == False:  
                if html_extract[i] == '\n':
                    break
                elif text_ID == False:
                    if html_extract[i].isalnum():
                        text_ID = True
                        new_date.append(html_extract[i])
                else: 
                    new_date.append(html_extract[i])
    return new_date

def extract_revenue(html_extract):
    new_revenue = []
    end_ID = False
    start_ID = False
    for i in range(len(html_extract)):
        if start_ID == False:
            if html_extract[i].isdigit():
                new_revenue.append(html_extract[i])
                start_ID = True
        elif start_ID == True:
            if end_ID == False:  
                if html_extract[i] == '\n':
                    break
                else:
                    new_revenue.append(html_extract[i])
    return new_revenue

def extract_runtime(html_extract):
    new_runtime = []
    end_ID = False
    start_ID = False
    for i in range(len(html_extract)):
        if start_ID == False:
            if html_extract[i].isdigit():
                new_runtime.append(html_extract[i])
                start_ID = True
        elif start_ID == True:
            if end_ID == False:  
                if html_extract[i] == '\n':
                    break
                else:
                    new_runtime.append(html_extract[i])
    return new_runtime

def extract_languages(html_extract):
    new_languages = []
    end_ID = False
    start_ID = False
    text_ID = False
    for i in range(len(html_extract)):
        if start_ID == False:
            if html_extract[i] == '\n':
                start_ID = True
        elif start_ID == True:
            if end_ID == False:  
                if html_extract[i] == '\n':
                    break
                elif text_ID == False:
                    if html_extract[i].isalnum():
                        text_ID = True
                        new_languages.append(html_extract[i])
                else: 
                    new_languages.append(html_extract[i])
    return new_languages

def extract_genre(html_extract):
    new_genre = []
    end_ID = False
    start_ID = False
    text_ID = False
    for i in range(len(html_extract)):
        if start_ID == False:
            if html_extract[i] == '\n':
                start_ID = True
        elif start_ID == True:
            if end_ID == False:  
                if html_extract[i] == '\n':
                    break
                elif text_ID == False:
                    if html_extract[i].isalnum():
                        text_ID = True
                        new_genre.append(html_extract[i])
                else: 
                    new_genre.append(html_extract[i])
    return new_genre

def extract_sequel(html_extract):

    new_sequel = []
    end_ID = False
    start_ID = False
    for i in range(len(html_extract)):
        if start_ID == False:
            if html_extract[i] == 'Q':
                start_ID = True
                new_sequel.append(html_extract[i])
        elif start_ID == True:
            if end_ID == False:  
                if html_extract[i].isdigit() == True:
                    new_sequel.append(html_extract[i])
                else:
                    break
    return new_sequel

def scrape_metadata(df, i):
    metadata = ['', '', '', '', '', '', '']
    # test url 
    # url = 'https://www.wikidata.org/wiki/Q4786598'

    # specify the wikipedia page url
    url = "https://www.wikidata.org/wiki/" + str(df['SequelID'].iloc[i])

    # make a request to the url 
    response = requests.get(url)

    # parse the html content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # looking if the prequel and sequel index on the page exist
    movieName = soup.prettify().find('og:title') - 50
    releaseDate = soup.prettify().find('publication date')
    boxOffice = soup.prettify().find('box office')
    runtime = soup.prettify().find('duration')
    languages = soup.prettify().find('original language')
    genres = soup.prettify().find('genre')
    sequel = soup.prettify().find('followed by')

    # print([movieName, releaseDate, boxOffice, runtime, languages, genres, sequel])


    if movieName != -1:
        movieName2 = soup.prettify()[movieName:].find('content="')
        movieName3 = soup.prettify()[movieName + movieName2 : movieName + movieName2 + 200]
        metadata[0] = "".join(extract_name(movieName3))
    else: 
        metadata[0] = "NaN"

    if releaseDate != -1:
        releaseDate2 = soup.prettify()[releaseDate:].find('wikibase-snakview-variation-valuesnak')
        releaseDate3 = soup.prettify()[releaseDate + releaseDate2 : releaseDate + releaseDate2 + 150]
        metadata[1] = "".join(extract_date(releaseDate3))
    else:
        metadata[1] = "NaN"

    if boxOffice != -1:
        boxOffice2 = soup.prettify()[boxOffice:].find('dollar') - 100
        boxOffice3 = soup.prettify()[boxOffice + boxOffice2 : boxOffice + boxOffice2 + 50]
        metadata[2] = "".join(extract_revenue(boxOffice3))
    else:
        metadata[2] = "NaN"

    if runtime != -1:
        runtime2 = soup.prettify()[runtime:].find('wikibase-snakview-variation-valuesnak') or soup.prettify()[runtime:].find('minute') or soup.prettify()[runtime:].find('hour') or soup.prettify()[runtime:].find('second')
        runtime3 = soup.prettify()[runtime + runtime2 - 100 : runtime + runtime2 + 150]
        metadata[3] = "".join(extract_runtime(runtime3))
    else:
        metadata[3] = "NaN"

    if languages != -1:
        languages2 = soup.prettify()[languages:].find('href="')
        languages3 = soup.prettify()[languages + languages2 : languages + languages2 + 100]
        metadata[4] = "".join(extract_languages(languages3))
    else:
        metadata[4] = "NaN"
        
    if genres != -1:
        genres2 = soup.prettify()[genres:].find('href="')
        genres3 = soup.prettify()[genres + genres2 : genres + genres2 + 100]
        metadata[5] = "".join(extract_genre(genres3))
    else:
        metadata[5] = "NaN"

    if sequel != -1:
        sequel_index_2 = soup.prettify()[sequel:].find('<a ')
        wikidata_id = soup.prettify()[sequel + sequel_index_2 : sequel + sequel_index_2 + 300]
        metadata[6] = "".join(extract_sequel(wikidata_id))
    else:
        metadata[6] = "NaN"

    return metadata

# Load the data
DATA_PATH = ''

# Import tsv file, where each line is a movie and the metadata is separated by tabs and the first line is the header of columns : WikipediaID,WikidataID,PrequelID,SequelID
movie = pd.read_csv(DATA_PATH + 'sequels.csv', sep=',', header=0)

# adding the following categories to the movie dataframe ['WikipediaID', 'FreebaseID', 'MovieName', 'ReleaseDate', 'BoxOffice', 'Runtime', 'Languages', 'Countries', 'Genres']
movie['FreebaseID'] = ''
movie['MovieName'] = ''
movie['ReleaseDate'] = ''
movie['BoxOffice'] = ''
movie['Runtime'] = ''
movie['Languages'] = ''
movie['Countries'] = ''
movie['Genres'] = ''

# Creating a new dataframe with only the movies that have a sequel
movie_with_sequel = movie[movie['SequelID'].notnull()]

# For sequel, we get check if the movie is in the original dataframe. if it is not, we add it to a new dataframe
movie_with_sequel_not_in_original = movie_with_sequel[~movie_with_sequel['SequelID'].isin(movie['WikidataID'])]

# for all sequels not in the original dataframe, we scrape the metadata and add it to the dataframe
metadata = ['', '', '', '', '', '', '']

# creating a dataframe for the new movies and their metadata
new_movies = pd.DataFrame(columns=['WikipediaID', 'WikidataID', 'PrequelID', 'SequelID', 'FreebaseID', 'MovieName', 'ReleaseDate', 'BoxOffice', 'Runtime', 'Languages', 'Countries', 'Genres'])

new_movies['WikidataID'] = movie_with_sequel_not_in_original['SequelID']
new_movies['PrequelID'] = movie_with_sequel_not_in_original['WikidataID']

start = int(input("Enter start index: "))
end = int(input("Enter end index: "))

for i in range(start, end):
    metadata = scrape_metadata(movie_with_sequel_not_in_original, i)
    print(i, ' / ', len(movie_with_sequel_not_in_original)) 

    # adding the metadata to the new dataframe   
    new_movies['SequelID'].iloc[i] = metadata[6]
    new_movies['MovieName'].iloc[i] = metadata[0]
    new_movies['ReleaseDate'].iloc[i] = metadata[1]
    new_movies['BoxOffice'].iloc[i] = metadata[2]
    new_movies['Runtime'].iloc[i] = metadata[3]
    new_movies['Languages'].iloc[i] = metadata[4]
    new_movies['Genres'].iloc[i] = metadata[5]


# create new document with the results, where the name includes the start and end index
new_movies.to_csv('missing_sequels' + str(start) + '_' + str(end) + '.csv', sep=',', index=False, encoding='utf-8')
