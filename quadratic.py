import math


def main():

    print("Hello! Welcome to to a quadratic calculator")
    a, b, c = input("Please enter the coefficients(a,b,c):")
    start = (-1*b)
    root = math.sqrt((b*b) - 4 * a * c)
    divide = (2*a)

    first = (start + root) / divide
    second = (start - root) / divide
    print("The first solution is", first)
    print("The second solution is", second)


main()
