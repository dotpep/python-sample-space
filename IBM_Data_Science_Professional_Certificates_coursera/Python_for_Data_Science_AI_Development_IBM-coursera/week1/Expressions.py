number = 'operands'
math_symbols = 'operators'
print(number, '="50" + "40" + "60"')
print(math_symbols, '=50 "+" 40 "+" 60')

print(50 + 40 + 60, "= 50 + 40 + 60 - arithmetic")
print(50 - 60, "=50 - 60")
print(5 * 5, "=5 * 5")
print(25 / 5, "=25 / 5")
print(25 / 6, "=25 / 6")
print(25 // 6, "=25 // 6")
print(int(25 / 6), "=int(25 / 5) - (typecasting)")
print(bool(50 - 60), "=bool(50 - 60) - bool minus")

minus = "50 - 60"
x = bool(minus)
print(f"{type(x)}: \n50 - 60: \nusing minus.")
