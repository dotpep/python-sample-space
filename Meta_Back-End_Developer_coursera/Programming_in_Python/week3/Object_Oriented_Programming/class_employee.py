class Employee:
    def __init__(self, position, status):
        self.position = position
        self._status = status

    def intro(self):
        return f"I am a {self.position}"

    def info_status(self):
        return f"I am in status {self._status}"


emp1 = Employee("Shift Lead", "FT")
print(emp1.position)
print(emp1._status)
print(emp1.intro())
print(emp1.info_status())

