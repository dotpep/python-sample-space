class Payslips:
    def __init__(self, name: str, payment: str, amount: int):
        self.name: str = name
        self.payment: str = payment
        self._amount: int = amount

    def pay(self):
        self.payment = "yes"

    def status(self):
        if self.payment == "yes":
            return self.name + " is paid " + str(self._amount)
        else:
            return self.name + " is not paid yet"


nathan = Payslips("Nathan", "no", 1000)
roger = Payslips("Roger", "no", 1000)

print(nathan.status())
print(roger.status())

nathan.pay()
print("After payment")
print(nathan.status())
print(roger.status())
