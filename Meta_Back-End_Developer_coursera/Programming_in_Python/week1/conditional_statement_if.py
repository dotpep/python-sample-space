# bill_total = 210
# discount1 = 10
# discount2 = 20
#
#
# if bill_total > 100 and bill_total < 200:
#     print(f"Bill is greater than 100! discount: {discount1}")
#     bill_total = bill_total - discount1
# elif bill_total > 200:
#     print(f"Bill is greater than 200! discount: {discount2}")
#     bill_total = bill_total - discount2
# else:
#     print("Bill is less than 100!")
#
# print("Total bill: " + str(bill_total))


###

# temperature = 30
# humidity = 70
#
# if temperature > 25:
#     print("It's hot today!")
#
# if humidity > 60:
#     print("It's humid today!")
#
# if temperature > 25 and humidity > 60:
#     print("It's a hot and humid day!")



###

# Initialize the current state of the light
current = False

# Ask the user for the initial state of the light
current_input = input("On or Off: ")
if current_input == "On":
    current = True
elif current_input == "Off":
    current = False
else:
    print("Please write only 'On' or 'Off'.")

# Initialize the count variable
count = 0

# Start a loop that will run until count reaches 10
while count < 10:
    count += 1
    print("Count: ", count)

    # If the light is currently on, turn it off
    if current:
        current = False
        print('Turning light off')

    # If the light is currently off, turn it on
    elif not current:
        current = True
        print('Turning light on')

    # If count reaches 10, break the loop and print a message
    if count == 10:
        print("Light is broken!")

