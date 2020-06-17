print("This is a simple program to average two exam scores together")


def main():
    score1, score2 = eval(input("Enter two scores seperated by a comma"))
    average = (score1+score2)/2
    print("You got a ", score1, " on your first exam")
    print("You got a ", score2, " on your second exam")
    print("The average between two exams are", average)


main()
