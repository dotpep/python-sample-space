menu = {
    1: {
        "name": 'espresso',
        "price": 1.99
    },
    2: {
        "name": 'coffee',
        "price": 2.50
    },
    3: {
        "name": 'cake',
        "price": 2.79
    },
    4: {
        "name": 'soup',
        "price": 4.50
    },
    5: {
        "name": 'sandwich',
        "price": 4.99
    }
}


def calculate_subtotal(order):
    print('Calculating bill subtotal...')
    global sum_of
    sum_of = 0
    for item in order:
        sum_of += item["price"]

    return round(sum_of, 2)


def calculate_tax(subtotal):
    print('Calculating tax from subtotal...')

    tax_rate = 15

    global tax
    tax = subtotal * (tax_rate / 100)
    return round(tax, 2)


def summarize_order(order):  # def summarize_order(order, subtotal, tax):

    print_order(order)

    # subtotal = sum(item["price"] for item in order)
    #
    # tax_rate = 15
    # tax = subtotal * (tax_rate / 100)

    subtotal = sum_of

    total = round(subtotal + tax, 2)
    names = [item["name"] for item in order]

    # print(subtotal)
    # print(tax)
    # print(total)

    return names, total


def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order


def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()


def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order


def main():
    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))

    tax = calculate_tax(subtotal)
    print("Tax for the order is: " + str(tax))

    items, total = summarize_order(order)
    # items, total = summarize_order(order, subtotal, tax)

    print(total)


if __name__ == "__main__":
    main()
