class MyFirstClass:
    print("Who wrote this?")
    index: str = "Author-Book"

    def hand_list(self, philosopher: str, book: str, year: str) -> None:
        # print(MyFirstClass.index)
        print(self.index)
        print(f"{philosopher} wrote the book: {book}, \nwas published in {year}")


who_dunn_it = MyFirstClass()
who_dunn_it.hand_list("Plato", "Republic", "c. 375 BC")
who_dunn_it.hand_list("Sun Tzu", "The Art of War", "5th century BC")
