def main():
    print("Change Counter")
    print(" ")

    pennies = input("Enter the number of pennies:")
    pennies *= 0.01
    print(" ")

    nickels = input("Enter the number of nickels:")
    nickels *= 0.05
    print(" ")

    dimes = input("Enter the number of dimes:")
    dimes *= 0.10
    print(" ")

    quarters = input("Enter the number of quarters:")
    quarters *= 0.25
    print(" ")

    total = pennies + dimes + nickels + quarters

    print("Your total is:", total)


main()
