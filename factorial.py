def main():
    print("Hello welcome to a factorial program")
    factor = input("Input a number that will be factorialed: ")
    x = 1
    for factor in range(factor, 1, -1):
        x = x*factor
    print(x)


main()
