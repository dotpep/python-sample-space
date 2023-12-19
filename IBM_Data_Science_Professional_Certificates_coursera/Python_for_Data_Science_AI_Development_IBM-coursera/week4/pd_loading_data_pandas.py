import pandas as pd

# read csv & print head 5 rows & columns of dataframe
csv_path = "train2.csv"
df = pd.read_csv(csv_path)
df.head()

# process loading an Excel file or xlsx
xlsx_path = "train3.xlsx"
df = pd.read_excel(xlsx_path)
df.head()

# create data frame out of a dictionary
# pip install openpyxl - library for reading and writing Excel (.xlsx) files.
songs = {'Album': ['Thriller', 'Back in Black', 'The Dark Side of the Moon', 'The Bodyguard', 'Bat Out of Hell', 'Their Greatest Hits (1971-1975)', 'Saturday Night Fever', 'Rumours'],
 'Released': ['1982', '1980', '1973', '1992', '1977', '1976', '1977', '1977'],
 'Length': ['00:42:19', '00:42:11', '00:42:49', '00:57:44', '00:46:33', '00:43:08', '1:15:54', '00:40:01']}

songs_frame = pd.DataFrame(songs)
df = songs_frame

# create a new data frame consisting of one column.
x = df[['Length']]
y = df[['Album', 'Released']]


# access using method ix
"""
The method ix is deprecated in newer versions of Pandas. You can use .iloc or .loc instead to access the first row and first column of the dataframe.

Here's how you can use .iloc:
df.iloc[0, 0]
And here's how you can use .loc:

df.loc[0, df.columns[0]]
Both methods will return the value at the first row and first column of the dataframe.
"""

df.iloc[1]
print(df.loc[2, df.columns[0]])
