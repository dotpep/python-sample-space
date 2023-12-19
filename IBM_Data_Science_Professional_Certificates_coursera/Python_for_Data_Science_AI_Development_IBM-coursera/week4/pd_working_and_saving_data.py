import pandas as pd

songs = {'Album': ['Thriller', 'Back in Black', 'The Dark Side of the Moon', 'The Bodyguard', 'Bat Out of Hell', 'Their Greatest Hits (1971-1975)', 'Saturday Night Fever', 'Rumours'],
 'Released': ['1982', '1980', '1973', '1992', '1977', '1976', '1977', '1977'],
 'Length': ['00:42:19', '00:42:11', '00:42:49', '00:57:44', '00:46:33', '00:43:08', '1:15:54', '00:40:01']}

df = pd.DataFrame(songs)

# List Unique Values
df['Released'].unique()

# Create new database consisting of songs from the 1980s and after 1979.
df['Released'] >= str(1980)

df1 = df[df['Released'] >= str(1980)]

# Save as CSV
df1.to_csv('new_songes.csv')
print(df1)
