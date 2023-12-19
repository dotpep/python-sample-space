# Downloading And Scraping The Contents Of A Web Page
import requests
from bs4 import BeautifulSoup

# We Download the contents of the web page:
url = "http://www.ibm.com"

# We Download the contents of the web page:
data = requests.get(url).text
# We create a BeautifulSoup object using the BeautifulSoup constructor
soup = BeautifulSoup(data, "html.parser") # create a soup object using the variable 'data'

# Scrape all links
def scrap_links():
    for link in soup.find_all('a', href=True):  # in html anchor/link is represented by the tag <a>
        print(link.get('href'))


# Scrape all images Tags
def scrap_images():
    for img in soup.find_all('img', src=True): # in html image is represented by the tag <img>
        print(img)
        print(img.get('src'))

    """
    for link in soup.find_all('img'):# in html image is represented by the tag <img>
        print(link)
        print(link.get('src'))
    """



# Scrape data from HTML tables

# The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

# get the contents of the webpage in text format and store in a variable called data
data = requests.get(url).text
soup = BeautifulSoup(data, "html.parser")

# find a html table in the web page
table = soup.find('table') # in html table is represented by the tag <table>
# aws: table = soup.find('table', attrs={'class': 'table'})

# Get all rows from the table
def scrap_data_tables():
    for row in table.find_all('tr'): # in htmml table row represented by the tag <tr>
        # Get all columns in each row.
        cols = row.find_all('td') # in html a column is represented by the tag <td>
        color_name = cols[2].string # store the value in column 3 as color_name
        color_code = cols[3].string # store the value in column 4 as color_code
        print("{}--->{}".format(color_name, color_code))


def test1_format():
    a = "pepel"
    b = "dot pep"
    print("{} to {}".format(a, b))



# Scrape data from HTML tables into a DataFrame using BeautifulSoup and Pandas
import pandas as pd

#The below url contains html tables with data about world population.
url = "https://en.wikipedia.org/wiki/World_population"

data = requests.get(url).text
soup = BeautifulSoup(data, "html.parser")

#find all html tables in the web page
tables = soup.find_all('table') # in html table is represented by the tag <table>

# we can see how many tables were found by checking the length of the tables list
len(tables) # 29

"""
Assume that we are looking for the 10 most densly populated countries table, we can look through the tables list and find the right one we are look for based on the data in each table or we can search for the table name if it is in the table but this option might not always work.
"""
for index, table in enumerate(tables):
    if "10 most densely populated countries" in str(table):
        table_index = index


table_index # 5

# See if you can locate the table name of the table, 10 most densly populated countries, below.
tables[table_index].prettify()


population_data = pd.DataFrame()

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if col != []:
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = pd.concat([population_data, pd.DataFrame({
            "Rank": [rank],
            "Country": [country],
            "Population": [population],
            "Area": [area],
            "Density": [density]
        })])

population_data

"""python 3.10 
AttributeError: 'DataFrame' object has no attribute 'append'. Did you mean: '_append'?
jupyter notebook: hands on lab - webscraping (IBM course - Python for Data Science - week5)
setup: python 3.7
Working!


population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

population_data

"""

"""explain
population_data = pd.DataFrame()

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if col != []:
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = pd.concat([population_data, pd.DataFrame({
            "Rank": [rank],
            "Country": [country],
            "Population": [population],
            "Area": [area],
            "Density": [density]
        })])

print(population_data)


1. The `population_data` DataFrame is initialized as an empty DataFrame using `pd.DataFrame()`.
2. The loop iterates over each row (`tr`) found within the table identified by `tables[table_index]`.
3. For each row, the loop finds all the cells (`td`) within that row.
4. If the `col` list is not empty (i.e., if cells are found in the row), the code proceeds to extract the relevant data.
5. The variables `rank`, `country`, `population`, `area`, and `density` are assigned the respective values extracted from the cells.
6. A new DataFrame is created using `pd.DataFrame()` with a dictionary containing the extracted data. Each value is placed in a list (`[rank]`, `[country]`, etc.) to ensure compatibility with concatenation.
7. `pd.concat()` is used to concatenate the new DataFrame with the `population_data` DataFrame. This creates a new DataFrame with the newly scraped row appended to it.
8. The `population_data` DataFrame is updated with the concatenated DataFrame.
9. After the loop completes, the final `population_data` DataFrame contains all the scraped data.
10. Finally, the `population_data` DataFrame is printed using `print(population_data)`.
This approach iteratively constructs the DataFrame by concatenating newly scraped rows to the existing DataFrame. It ensures that the `population_data` DataFrame grows dynamically as each row is appended.

"""



# Scrape data from HTML tables into a DataFrame using BeautifulSoup and read_html
"""
Using the same url, data, soup, and tables object as in the last section we can use the read_html function to create a DataFrame.

Remember the table we need is located in tables[table_index]

We can now use the pandas function read_html and give it the string version of the table as well as the flavor which is the parsing engine bs4.
"""

pd.read_html(str(tables[7]), flavor='bs4')

# The function read_html always returns a list of DataFrames so we must pick the one we want out of the list.
population_data_read_html = pd.read_html(str(tables[4]), flavor='bs4')[0]
population_data_read_html


# Scrape data from HTML tables into a DataFrame using read_html
# We can also use the read_html function to directly get DataFrames from a url.
dataframe_list = pd.read_html(url, flavor='bs4')
len(dataframe_list)

dataframe_list[4]
print(pd.read_html(url, match="10 most densely populated countries", flavor='bs4')[0])

