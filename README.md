# Beyond Originals: A Deep Dive into Sequel Success

## Abstract

Making a sequel in the always-changing face of filmmaking is a creative as well as a calculated decision. Our team aims to explore the multiple factors that play a role in the success of movie sequels, questioning whether these continuations achieve a comparable level of popularity to their original or follow a distinct pattern. 
We examine movies genre dynamics, looking into how changes either support or contradict a sequel's success. We also analyze the effects of cast changes, asking whether they resonate with audiences or break the established storyline. 
This project aims to reveal layers of complexity beneath the surface of popular entertainment, providing nuanced insights into the complex nature of movie sequels. Our goal is to demystify the decision-making process underlying the sequels and provide a deeper understanding of their dynamics.

## Research questions

To better understand the distinctions between sequels and their original films, our investigation focused on these five main research questions:

1. What is the comparative popularity of sequels in terms of box office grossing compared to their original films? How do the financial performances of sequels correlate with their respective original films?
2. Does the cast significantly change between original films and their sequels?
3. Do the genres of a movie vary greatly between sequels and the original? Do genre changes significantly influence the success of a sequel?
4. Do storylines evolve or remain consistent between original films and their sequels?
5. What is the relative impact of critics' reviews or consumer reviews on the success of a film? (If relevant)

## Additional datasets
- Wikidata for meta-information about movies, such as sequels information
- IMDB and RottenTomatoes for reviews

### Methods

#### Part 1: Comparison Between Movies With and Without Sequels

**1.1: Sequel Data Enrichment:**
To initiate our analysis, we first addressed a critical information gap in our initial dataset – the presence or absence of movie sequels. In this phase, we employed a web scraping solution from Wikipedia and Wikidata, implementing a Python script named "wiki_scraper.py" located under "./sequel_scraper." This script, leveraging Pandas, Requests, and BeautifulSoup libraries, systematically loaded movie metadata, extracted Wikidata IDs, and scraped prequel and sequel IDs. The results were stored in a new Pandas DataFrame named "online_scraping" and saved to a CSV file, "sequels.csv," containing columns for WikipediaID, WikidataID, PrequelID, and SequelID. This comprehensive sequel data enrichment laid the foundation for subsequent analyses, enabling a thorough exploration of movie sequel success.

**1.2: Datasets Selection and Filtering:**
With the enriched dataset in place, we proceeded to categorize films based on the presence or absence of sequels. Two distinct datasets were created for analysis: one comprising films with sequels and the other with films without sequels. 

**1.3: Financial and Temporal Analysis:**
We explored the financial and temporal aspects of movies with and without sequels. Calculating mean and median revenues provided insights into the financial landscape, while mean and median durations revealed temporal dynamics. Histograms for both groups facilitate a comprehensive visual comparison, offering a nuanced understanding of the dataset.

**1.4: Release and Origin Analysis:**
To understand the temporal and geographical dimensions, we categorized films based on release year and month. For release month, we plotted the ratio of movies released per month, providing insights into monthly trends. For release year, a histogram was created to visualize the distribution of movies with sequels compared to all films each year. Additionally, films were categorized by their country of origin, contributing to a comprehensive understanding of the distribution of sequels across different regions.

**1.5: Genre Analysis:**
Delving into the intrinsic characteristics of films, we streamlined our genre analysis for practicality. Initially, we observed an abundance of subgenres in our dataset, which proved impractical for efficient analysis. Consequently, we refined our approach by selecting the top N most frequent genres across the dataset, providing a more general and manageable list of possible genres. Focusing on this subset, we identified the two main genres for each film, ensuring a concentrated exploration of genre dynamics.
To deepen our understanding, we created a heatmap for movies with and without sequels, comparing the combination of the two main genres per film for these categories. This visual exploration aims to unveil potential genre associations with movies that produce sequels, contributing to a comprehensive understanding of the role genres play in the success of movies with sequels. A statistical test explores these associations further.

**1.6: Character Analysis:**
Shifting focus to character attributes, we explored the median ages of actors. Further insights were gained by grouping actors into age bins and examining the ratio of male to female characters. This multifaceted analysis contributes to a better understanding of how character attributes influence the success of movies with and without sequels. 

#### Part 2: Comparison Between Original Films and Sequels

**2.1: Dataset Creation and Handling Saga Representation:**
To initiate the analysis, pairs of films (original; sequel) were created, forming datasets for all sequels and all original films. Special attention was given to addressing potential bias introduced by film sagas. Each pair of films was considered independently to ensure a fair comparison.

**2.2: Financial and Temporal Analysis: Revenue and Duration:**
Median annual revenues and mean or median durations were calculated for all original films and sequels. To assess the financial and temporal dynamics, histograms were created to visually compare the distribution of revenues and durations for original films and their sequels.

**2.3: Release Year Analysis and Origin Country Analysis:**
The release year and month were analyzed to understand the temporal dimensions of original films and sequels. Histograms were generated to compare the distribution of release years for original films and sequels. Additionally, films were categorized by their country of origin, contributing to a comprehensive understanding of the distribution of sequels across different regions, similar to Part 1.

**2.4: Genre Analysis:**
A heatmap was generated to compare the distribution of genres between all original films and their respective sequels, employing a methodology similar to that used in Part 1. The focus of this analysis was on understanding how genres evolve and change between the original film and its sequel.

**2.5: Character Analysis:**
To delve into the intricacies of character dynamics, the proportion of the cast returning for sequels was calculated. Additionally, the median ages of characters were compared between sequels and original films. Ratios of male to female characters were computed for both sequels and original films, with an in-depth analysis of changes in gender representation between the two. 

**2.6: Storyline Changes Analysis:**
To comprehend the evolution of the narrative, similarities between summaries of original films and their sequels were calculated, based on themes or overall content. Natural Language Processing (NLP) techniques, such as cosine similarity or Jaccard similarity, were employed for this analysis, providing a quantitative measure of storyline changes. The ratio of recurring characters between original films and sequels for each pair was computed, shedding light on the continuity of characters across movies.



### Executed timeline

_Step n - to be done for dd/mm/yyyy_

Step 0 - 17.11.2023 : **Deadline Milestone 2**

Step 1 - 05.12.2023 : Make adjustments based on feedback from Milestone 2 

Step 2 - 09.12.2023 : Collect / Scrape all missing information needed for Part 2

Step 3 - 12.12.2023 : Analysis of Parts 2.1 to 2.4

Step 4 - 16.12.2023 : Analysis of Parts 2.5 to 2.7

Step 5 - 20.12.2023 : Code cleanup + HTML Data Story

Step 6 - 22.12.2023 :  **Deadline Milestone 3**


### Organization within team

<table class="tg" style="table-layout: fixed; width: 342px">
<colgroup>
<col style="width: 16px">
<col style="width: 180px">
</colgroup>
<thead>
  <tr>
    <th class="tg-0lax">Teammate</th>
    <th class="tg-0lax">Contributions</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">Antoine </td>
    <td class="tg-0lax"> Website + help for part 2 </td>
  </tr>
  <tr>
    <td class="tg-0lax">Elisa </td>
    <td class="tg-0lax"> Website + Collect missing information</td>
  </tr>
  <tr>
    <td class="tg-0lax">Yosr</td>
    <td class="tg-0lax"> Data Story + milestone 2 feedback correction </td>
  </tr>
  <tr>
    <td class="tg-0lax">Willy</td>    
    <td class="tg-0lax"> In charge of Parts 2.1 to 2.4 + final code cleanup </td>
  </tr>
  <tr>
    <td class="tg-0lax">Lena</td>
    <td class="tg-0lax"> In charge of Parts 2.5 to 2.7 + in charge of final "submission" </td>
  </tr>
</tbody>
</table>
