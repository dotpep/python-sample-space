try:
    write_mode = 'w'
    append_mode = 'a'

    with open('sample/newfile.txt', append_mode) as file:
        write_file = file.write("This is new file created!")
        writelines_file = file.writelines(["\nThis is a new file created!", "\nThis is another line to be added."])
except FileNotFoundError as e:
    print("ERROR", e)
