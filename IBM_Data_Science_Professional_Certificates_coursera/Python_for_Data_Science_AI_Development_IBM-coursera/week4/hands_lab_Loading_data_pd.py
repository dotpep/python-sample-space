import pandas as pd

data = {
    'Artist': ['Michael Jackson', 'AC/DC', 'Pink Floyd', 'Whitney Houston', 'Meat Loaf', 'Eagles', 'Bee Gees', 'Fleetwood Mac'],
    'Album': ['Thriller', 'Back in Black', 'The Dark Side of the Moon', 'The Bodyguard', 'Bat Out of Hell', 'Their Greatest Hits (1971-1975)', 'Saturday Night Fever', 'Rumours'],
    'Released': ['1982', '1980', '1973', '1992', '1977', '1976', '1977', '1977'],
    'Length': ['00:42:19', '00:42:11', '00:42:49', '00:57:44', '00:46:33', '00:43:08', '1:15:54', '00:40:01'],
    'Genre': ['Pop, rock, R&B', 'Hard rock', 'Progressive rock', 'Soundtrack/R&B, soul, pop', 'Hard rock, progressive rock', 'Rock, soft rock, folk rock', 'Disco', 'Soft rock'],
    'Music recording sales (millions)': [46, 26.1, 24.2, 26.1, 20.6, 32.2, 20.6, 27.9],
    'Claimed sales (millions)': [65, 50, 45, 50, 43, 42, 40, 40],
    'Released, Soundtrack': ['30-Nov-82', '25-Jul-80', '01-Mar-73', '25-Jul-80', '21-Oct-77', '17-Feb-76', '15-Nov-77', '04-Feb-77'],
    'Rating (friends)': [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5]
}

# Read data from CSV file

csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)

# Print first five rows of the dataframe
df.head()


# Read data from Excel File and print the first five rows
xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'

df = pd.read_excel(xlsx_path)
df.head()

# Access to the column Length
x = df[['Length']]
x

# Get the column as a series
x = df['Length']
x

# Get the column as a dataframe
x = df[['Artist']]
type(x)

# Access to multiple columns
y = df[['Artist','Length','Genre']]
y

# Access the value on the first row and the first column
df.iloc[0, 0]

# Access the value on the second row and the first column
df.iloc[1,0]

# Access the value on the first row and the third column
df.iloc[0,2]

# Access the value on the second row and the third column
df.iloc[1,2]


df = pd.DataFrame(data)
print(df.iloc[6, 'genre'])
