with open('newfile.txt', 'r') as file:
    number_of_chars = 40

    data_read = file.read(number_of_chars)
    data_readline = file.readline()
    data_iter_readline = file.readlines()

    get_possible_method = dir(file)

    get_type = type(data_iter_readline)
    get_by_index = data_iter_readline[0]
    get_len = len(data_iter_readline)

    new_list = [line for line in data_iter_readline]

    print(data_iter_readline)
