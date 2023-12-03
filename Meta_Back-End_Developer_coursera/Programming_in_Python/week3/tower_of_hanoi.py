# Recursive function for Tower of Hanoi
def hanoi(disks, source, helper, destination):
    # Base Condition
    if disks == 1:
        print("Disk {} moves from tower {} to tower {}".format(disks, source, destination))
        return 1

    # Recursive calls in which function calls itself
    hanoi(disks - 1, source, destination, helper)
    print("Disk {} moves from tower {} to tower {}".format(disks, source, destination))
    hanoi(disks - 1, helper, destination, source)


disks = int(input("Number of disks to be displaced: "))

hanoi(disks, "A:source", "B:helper", "C:destination")
