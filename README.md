# Identifying topics/pages to be included in Hindi Wikipedia

<summary><h2>Table of Contents</h2></summary><p>

- [1. Project](#project)
    - [1.1. Problem Statement](#problem-statement)
	- [1.2. Methodology](#methodology)
- [2. Code](#code)
    - [2.1. Scraping](#scraping)
	- [2.2. Named Entity Recognition](#named-entity-recognition)
    - [2.3 Topic Identification](#topic-identification)
- [3. Results](#results)

</p><p></p>

## Project

### Problem Statement

Use Indian language news papers, text books and current affairs content as a set of sources to identify the new topics to be added to any indian language wikipedia. In order to qualify to be a wikipedia page, there has to be enough evidence or set of references - what are the topics that has these kinds of evidences/references but does not have a wikipedia page

### Methodology

We have proposed 3 different ways to expand Hindi Wikipedia:
* Improving breadth of topics by adding new topics of emerging interest. This can be done by scraping Hindi newspapers and identify important events. BBC Hindi was used.
* Improving depth by expansion in categories that are present in the Indian domain. This was done by identifying several articles belonging to broad domains.
* Improving interconnectivity of present topics by adding topics related to a previously existing Wikipedia article.

After collecting resources, named entity recognition is performed, resulting topics are checked if they already exist and then presented.

## Code

The source code for each of the three types of expansions are in the src/ directory:

### Scraping

* Domain_Expansion/ contains the code for improving breadth of topics. scrape.py scrapes content of various articles. It can be run by:
```
$ python3 scrape.py
```
The scraped data can be found in the data/ folder in main directory. It has been divided into many categories like health, politics etc.

* News_Expansion/ contains code for scraping BBC news articles in BBC_Scraper/ subdirectory. It can be run by:
```
$ scrapy crawl bbcScraper
```

To export the results from MongoDB to CSV, run the following:
```
$ mongoexport --db bbc --collection news_items --type=csv --fields _id,url,title,content --out output.csv
``` 

The scraped data can be found [here](https://iiitaphyd-my.sharepoint.com/:f:/g/personal/sathviksanjeev_b_research_iiit_ac_in/EqYL0iNQzFdAiclzs9uN474BZHlJa8NXPOW1h4_UdATwpQ?e=AT7xGg).

* Wiki_Expansion/ contains the code for improving interconnectivity by scraping random Wikipedia articles. To scrape and later run named entity recognition, it will require ```wikipedia``` module to be installed.
```
$ pip3 install -r requirements.txt
```

### Named Entity Recognition

Each of the three subdirectories described above in src/ folder have a ner.py file. It can be run as follows:
```
python3 ner.py
```

It reads data corresponding to how it was scraped and performs named entity recognition using the code present in hindi-part-of-speech-tagger/ subdirectory. Each of these output a file called ner_list.txt that stores the pickled form of a list of lists which contains named entities for each sentence.

### Topic Identification

After the named entities are identified, topic identification is done, by checking if the probable topics are already part of existing Hindi Wikipedia. The code for this is present in src/check_topic_wiki.py. It can be run as follows:
```
python3 check_topic_wiki.py -i <input file> -o <output file> -p True
```

The -p argument is true if the input file contains pickled list of lists, else false.

## Results

All the possible new topics for Hindi Wikipedia are stored in the results/ folder. nonwiki.txt contains results of scraping news and Wikipedia articles and nonwiki_1.txt contains results of scraping domain articles.
