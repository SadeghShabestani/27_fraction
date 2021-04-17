import termcolor2

print(termcolor2.colored("Fraction Sum: ", color="green"))


def total():
    s1 = int(input("Enter S1: "))
    m1 = int(input("Enter m1: "))
    s2 = int(input("Enter S2: "))
    m2 = int(input("Enter m2: "))
    result = {"s": ((s1 * m2) + (s2 * m1)), "m": m1 * m2}
    return result


res = total()
print(res["s"], "/", res["m"])

print(termcolor2.colored("Fraction Multiplication: ", color="green"))


def multi():
    s1 = int(input("Enter S1: "))
    m1 = int(input("Enter m1: "))
    s2 = int(input("Enter S2: "))
    m2 = int(input("Enter m2: "))
    result = {"s": s1 * s2, "m": m1 * m2}
    return result


res = multi()
print(res["s"], "/", res["m"])

print(termcolor2.colored("Fraction Minus: ", color="green"))


def minus():
    s1 = int(input("Enter S1: "))
    m1 = int(input("Enter m1: "))
    s2 = int(input("Enter S2: "))
    m2 = int(input("Enter m2: "))
    m = m1 * m2
    result = {"s": (m // m1) * s1 - (m / m2) * s2, "m": m}
    return result


res = minus()
print(res["s"], "/", res["m"])

print(termcolor2.colored("Fraction Divide: ", color="green"))


def divide():
    s1 = int(input("Enter S1: "))
    m1 = int(input("Enter m1: "))
    s2 = int(input("Enter S2: "))
    m2 = int(input("Enter m2: "))
    result = {"s": s1 * m2, "m": s2 * m1}
    return result


res = divide()
print(res["s"], "/", res["m"])
