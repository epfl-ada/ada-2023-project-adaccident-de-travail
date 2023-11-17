# Beyond Originals: A Deep Dive into Sequel Success

## Abstract

Making a sequel in the always changing face of filmmaking is a creative as well as a calculated decision. Our team aims to explore the multiple factors that play a role in the success of movie sequels, questioning whether these continuations achieve a comparable level of popularity to their original or follow a distinct pattern. 
We examine movie’s genre dynamics, looking into how changes either support or contradict a sequel's success. We also analyze the effects of cast changes, asking whether they resonate with audiences or break the established storyline. 
This project aims to reveal layers of complexity beneath the surface of popular entertainment, providing nuanced insights into the complex nature of movie sequels. Our goal is to demystify the decision-making process underlying the sequels and provide a deeper understanding of their dynamics.

## Research questions

To better understand the distinctions between sequels and their original films, our investigation focused on these five main research questions:

1. What is the comparative popularity of sequels in terms of box office grossing compared to their original films? How do the financial performances of sequels correlate with their respective original films?
2. Does the cast significant change between original films and their sequels?
3. Do the genres of movie vary greatly between sequels and original? Do genre changes significantly influence the success of a sequel?
4. Do storylines evolve or remain consistent between original films and their sequels?
5. What is the relative impact of critics' reviews or consumer reviews on the success of a film? (If relevant)

## Additional datasets
- Wikidata for meta-information about movies, such as sequels information
- IMDB and RottenTomatoes for reviews

### Methods

#### Part 1: Comparison Between Movies with and Without Sequels

**1.1: Datasets Selection and Filtering:**
   - Categorize films based on the presence or absence of sequels.
   - Create two datasets for analysis: films with sequels and films without sequels.

**1.2: Revenue and Duration Analysis:**
   - Compute mean and median revenues and durations for films with sequels and films without sequels.
   - Apply statistical tests to assess differences in revenue and duration distributions among films with sequels and films without sequels.

**1.3: Release and Origin Analysis:**
   - Categorize films by release year and month and analyze the distribution for films with sequels and films without sequels.
   - Compute the ratio of films with sequels to all films for each year and analyze trends.
   - Categorize films by their country of origin and analyze the distribution for films with sequels and films without sequels.

**1.4: Genre and Character Analysis:**
   - Identify the N most frequent genres and determine the two main genres per film for all films.
   - Create heatmaps to visualize the relationship between the two main genres and compare the popularity of genre pairs amongst films with sequels and films without sequels.
   - Calculate median ages of actors and group actors into age bins for films with sequels and films without sequels for further analysis.
   - Calculate the ratio of male to female characters for films with sequels and films without sequels.

#### Part 2: Comparison Between Original Films and Sequels

**2.1: Dataset Creation and Handling Saga Representation:**
   - Create pairs of films (original; sequel) and datasets for all sequels and all original films.
   - Acknowledge and address potential bias introduced by film sagas by considering each pair of films independently.

**2.2: Statistical Analysis on Revenues:**
   - Calculate median annual revenues for all original films and all sequels.
   - Compute the ratio of sequel revenue to original film revenue for each pair, possibly using cumulative distribution functions (CDF) or binning for analysis.

**2.3: Duration Analysis and Release Month Analysis:**
   - Calculate median or mean durations for all original films and all sequels.
   - Compute the ratio of sequel duration to original film duration for each pair, considering CDF or binning.
   - Create histograms to compare the distribution of release months for original films and their sequels.

**2.4: Release Year Analysis and Origin Country Analysis:**
   - Calculate the duration between the release of an original film and its sequel (in months or weeks).
   - Analyze the distribution of time gaps to understand how quickly sequels tend to follow the release of the original film.
   - Generate a heatmap to compare the distribution of genres between all original films and all sequels, similar to Part 1.
   - Analyze changes in the genre distribution between an original film and its sequel.

**2.5: Film Genre Analysis and Character Types Analysis:**
   - Compute distances between genres in original films and their sequels, exploring similarity or dissimilarity.
   - Examine the evolution of genres between original films and sequels to determine if there are significant changes.
   - Calculate the proportion of the cast that returns for sequels.
   - Compare median ages of characters between sequels and original films.
   - Compute the ratio of male to female characters for all sequels and all original films.
   - Analyze changes in gender representation between original films and their sequels.

**2.6: Storyline Changes Analysis and Data Visualization:**
   - Calculate similarity between synopses of original films and their sequels, possibly based on themes or overall content.
   - Compute the ratio of recurring characters between original films and sequels for each pair.
   - Generate visualizations, such as heatmaps, histograms, and comparative charts, to present the findings.

**2.7: Statistical Testing:**
   - Apply statistical tests to identify significant differences in revenues, durations, or other relevant metrics between original films and sequels.


### Executed timeline

_Step n - to be done for dd/mm/yyyy_

Step 0 - 17.11.2023: **Deadline Milestone 2**

Step 1 - 05.12.2023 : Make adjustements based on feedback from Milestone 2 

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
