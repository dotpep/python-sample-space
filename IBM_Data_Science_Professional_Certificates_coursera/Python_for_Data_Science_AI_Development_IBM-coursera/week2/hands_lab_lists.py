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
    L1 = ["Michael Jackson", 10.1, 1982]

    def list_1():
        L = ["Michael Jackson", 10.1, 1982]
        return L

    def list_slicing():
        L = ["Michael Jackson", 10.1, 1982, "MJ", 1]
        return L[3:5]

    def list_contain():
        L = ["Michael Jackson", 10.1, 1982, [1, 2], ("A", 1)]
        return f"list full view: {L}; \n contain + slicing view: {L[3:5][0]}; \n third level: {L[3:5][0][0]}."

    def list_index_print(L):
        print('the same element using negative and positive indexing:\n Postive:', L[0],
              '\n Negative:', L[-3])
        print('the same element using negative and positive indexing:\n Postive:', L[1],
              '\n Negative:', L[-2])
        print('the same element using negative and positive indexing:\n Postive:', L[2],
              '\n Negative:', L[-1])

    # Create a list
    print("This is: Create a list")
    print(list_1())

    # Print the elements on each index
    print("This is: Print the elements on each index")
    list_index_print(list_1())

    # Sample List
    print("This is: Sample List")
    print(list_slicing())

    print("This is: Contain in list int, float, str & etc. Data")
    print(list_contain())

    # Extend (method) - add new elements to the list
    print("This is: Extend add new elements to list")
    L1.extend(['pop', 10])
    print(L1)

    # create new top of list (L1) To look at change without last Extend update list
    L1 = ["Michael Jackson", 10.1, 1982]

    # Append (method) - add one element to the list (like a new list in list or add one/another container/box in list)
    # If we append the list we have one new element consisting of a nested list
    print("This is: Append - add one element to the list")
    L1.append(['pop', 10])
    print(L1)

    # As lists are mutable, we can change them.
    print("This is: Lists are mutable, change them example")
    A = list_1()
    print('Before change:', A)
    A[0] = 'dot pep'
    print('After change:', A)

    # Delete the element based on the index
    print("This is: del the element based on the index")
    print('Before change:', A)
    del (A[0])
    print('After change:', A)

    # Split the string, default is by space
    print("This is: Split the string, default is by space")
    print('hard rock'.split())

    # Split the string by comma
    print("This is: Split the string by comma")
    print('A,B,C,D'.split(','))

    # Copy (copy by reference) the list A
    print("This is: copy by reference - the list A")
    A = ["hard rock", 10, 1.2]
    B = A
    print('A:', A)
    print('B:', B)

    # Examine the copy by reference
    print("This is: Examine the copy by reference")
    print('B[0]:', B[0])
    A[0] = "banana"
    print('B[0]:', B[0])

    # Clone (clone by value) the list A
    print("This is: clone by value - the list A")
    B = A[:]
    print(B)
    print(A)


print(dataset[0])


def test_method():
    print('This is method called "Extend"')
    L1 = ["Michael Jackson", 10.1, 1982]
    L1.extend(['pop', 10])
    print(L1)

    print('This is method called "Extend"')
    L1 = ["Michael Jackson", 10.1, 1982]
    L1.extend([('pop', 10)])
    print(L1)

    print('This is method called "Extend"')
    L1 = ["Michael Jackson", 10.1, 1982]
    L1.extend([['pop', 10]])
    print(L1)

    print('This is method called "Extend"')
    L1 = ["Michael Jackson", 10.1, 1982]
    L1.extend([['pop', 10]])
    print(L1[-1])

    print('This is method called "Extend"')
    L1 = ["Michael Jackson", 10.1, 1982]
    L1.extend([['pop', 10]])
    print(L1[-1][0])

    print('This is method called "Append"')
    L1 = ["Michael Jackson", 10.1, 1982]
    L1.append(['pop', 10])
    print(L1)


print(test_method())
