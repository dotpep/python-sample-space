# dataset:
# index: 0
# elements: Artist, Album, Released, Length, Genre, Music recording sales (millions), Claimed sales (millions), Released	Soundtrack, Rating (friends)
"""
1. artist - Name of the artist
2. album - Name of the album
3. released_year - Year the album was released
4. length_min_sec - Length of the album (hours,minutes,seconds)
5. genre - Genre of the album
6. music_recording_sales_millions - Music recording sales (millions in USD) on SONG://DATABASE
7. claimed_sales_millions - Album's claimed sales (millions in USD) on SONG://DATABASE
8. date_released - Date on which the album was released
9. soundtrack - Indicates if the album is the movie soundtrack (Y) or (N)
10. rating_of_friends - Indicates the rating from your friends from 1 to 10
"""
"""
    (0, "Artist", "Album", "Released", "Length", "Genre", "Music recording sales (millions)", "Claimed sales (millions)", "Released Soundtrack", "Rating (friends)"),
"""
dataset = [
    (1, 'Michael Jackson', 'Thriller', '1982', '00:42:19', 'Pop, rock, R&B', 46, 65, '30-Nov-82', 'N', 10.0),
    (2, 'AC/DC', 'Back in Black', '1980', '00:42:11', 'Hard rock', 26.1, 50, '25-Jul-80', 'N', 8.5),
    (3, 'Pink Floyd', 'The Dark Side of the Moon', '1973', '00:42:49', 'Progressive rock', 24.2, 45, '01-Mar-73', 'N',
     9.5),
    (4, 'Whitney Houston', 'The Bodyguard', '1992', '00:57:44', 'Soundtrack/R&B, soul, pop', 26.1, 50, '25-Jul-80', 'Y',
     7.0),
    (5, 'Meat Loaf', 'Bat Out of Hell', '1977', '00:46:33', 'Hard rock, progressive rock', 20.6, 43, '21-Oct-77', 'N',
     7.0),
    (6, 'Eagles', 'Their Greatest Hits (1971-1975)', '1976', '00:43:08', 'Rock, soft rock, folk rock', 32.2, 42,
     '17-Feb-76', 'N', 9.5),
    (7, 'Bee Gees', 'Saturday Night Fever', '1977', '1:15:54', 'Disco', 20.6, 40, '15-Nov-77', 'Y', 9.0),
    (8, 'Fleetwood Mac', 'Rumours', '1977', '00:40:01', 'Soft rock', 27.9, 40, '04-Feb-77', 'N', 9.5)
]


def test1():
    tuple1 = ("disco", 10, 1.2)

    # Print the type of the tuple you created
    print("Print the type of the tuple you created: ")
    print(type(tuple1))

    # Print the variable on each index
    print("Print the variable on each index: ")
    print(tuple1[0])
    print(tuple1[1])
    print(tuple1[2])

    # Print the type of value on each index
    print("Print the type of value on each index: ")
    print(type(tuple1[0]))
    print(type(tuple1[1]))
    print(type(tuple1[2]))

    # Use negative index to get the value of the last element
    print("Use negative index to get the value of the last element:")
    print(tuple1[-1])
    print(tuple1[-2])
    print(tuple1[-3])

    # Concatenate two tuples
    print("Concatenate two tuples: ")
    tuple2 = tuple1 + ("hard rock", 10)
    print(tuple2)

    # Slice from index 0 to index 2
    print("Slice from index 0 to index 2: ")
    print(tuple2[0:3])

    # Slice from index 3 to index 4
    print("Slice from index 3 to index 4: ")
    print(tuple2[3:5])

    # Get the length of tuple
    print("Get the length of tuple: ")
    print(len(tuple2))

    # A sample tuple
    Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)

    # Sort the tuple
    print("Sort the tuple: ")
    RatingsSorted = sorted(Ratings)
    print(RatingsSorted)

    # Create a nest tuple
    NestedT = (1, 2, ("pop", "rock"), (3, 4), ("disco", (1, 2)))

    # Print element on each index
    print("Print element on each index: ")
    print("Element 0 of Tuple: ", NestedT[0])
    print("Element 1 of Tuple: ", NestedT[1])
    print("Element 2 of Tuple: ", NestedT[2])
    print("Element 3 of Tuple: ", NestedT[3])
    print("Element 4 of Tuple: ", NestedT[4])

    # Print element on each index, including nest indexes
    print("Print element on each index, including nest indexes: ")
    print("Element 2, 0 of Tuple: ", NestedT[2][0])
    print("Element 2, 1 of Tuple: ", NestedT[2][1])
    print("Element 3, 0 of Tuple: ", NestedT[3][0])
    print("Element 3, 1 of Tuple: ", NestedT[3][1])
    print("Element 4, 0 of Tuple: ", NestedT[4][0])
    print("Element 4, 1 of Tuple: ", NestedT[4][1])

    # Print the first element in the second nested tuples
    print("Print the first element in the second nested tuples")
    print(NestedT[4][1][0])

    # Print the second element in the second nested tuples
    print("Print the second element in the second nested tuples: ")
    print(NestedT[4][1][1])


def test2():
    genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                    "R&B", "progressive rock", "disco")

    id = genres_tuple.index("disco")
    print(id)
    print(genres_tuple[7])


def find_in_dataset():
    get_id = input("Find name or words in data: ")
    id = dataset.index(f"{get_id}")

    # если успешно нашлось написать - если нет то ошибка
    if get_id:
        print("index: ", id)
    else:
        print("ErrorName - dataset not include this name or words")


print(test2())

###

print(dataset[0])

for i in range(8):
    print(dataset[i][1], "| released_year:", dataset[i][3])

A=(1,2,3,4,5)
print(len(A))