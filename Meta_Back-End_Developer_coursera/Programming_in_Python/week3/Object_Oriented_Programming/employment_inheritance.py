class Employees:
    def __init__(self, name: str, last: str):
        self.name = name
        self.last = last


class Supervisors(Employees):
    def __init__(self, name: str, last: str, password: str):
        super().__init__(name, last)
        self.password = password


class Chefs(Employees):
    def leave_request(self, days: int):
        return "May I take a leave for " + str(days) + " days"


adrian = Supervisors("Adian", "A", "apple")

emily = Chefs("Emily", "E")
juno = Chefs("Juno", "J")

print(emily.leave_request(3))
print(adrian.password)
print(emily.name)

# adrian = Employees("Adian", "A")
# adrian_s = Supervisors("Adian", "A", "apple")
# print(adrian.name, adrian.last, adrian_s.password)
#
# john = Supervisors("John", "Jakob", "jhjk")
# print(john.name, john.password)