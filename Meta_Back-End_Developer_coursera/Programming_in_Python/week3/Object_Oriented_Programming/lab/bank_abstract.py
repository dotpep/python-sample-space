from abc import ABC, abstractmethod


class Bank(ABC):
    """ An abstract bank class"""
    def basicinfo(self) -> str:
        print("This is a generic bank.")
        return "Generic bank: 0$."

    @abstractmethod
    def withdraw(self, amount) -> int:
        pass


class Swiss(Bank):
    """ A specific type of bank that derives from class Bank"""
    balance: int = 1000

    def basicinfo(self) -> str:
        print("This is the Swiss Bank.")
        return f"Swiss Bank: {self.balance}$"

    def withdraw(self, amount: int) -> int:
        if self.balance >= amount:
            self.balance = self.balance - amount
            print(f"Withdrawn amount: {amount}$.")
            print(f"\tNew Balance: {self.balance}$.")
        else:
            print(f"Insufficient funds. \n\tWithdraw: {amount}$. \n\tCurrent Balance: {self.balance}$.")
        return self.balance


# Manager Function
def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    assert issubclass(Swiss, Bank)

    s = Swiss()
    print(s.basicinfo())

    assert isinstance(s, Swiss)
    s.withdraw(30)
    s.withdraw(90)
    s.withdraw(700)
    s.withdraw(190)


if __name__ == "__main__":
    main()
