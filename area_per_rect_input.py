# !/user/bin/env python3

# Created by Kevin Csiffary
# Date: Sep. 22, 2022
# This program calculates the area and perimeter of a rectangle with user specified side lengths


def main():
    # ask the user the length and width of the rectangle
    length = input("What is the length of your rectangle? ")
    width = input("What is the width of your rectangle? ")

    # calculate and print the results
    print("if a rectangle has the dimensions:")
    print(f"{length}units * {width}units")
    print("")
    print("Then its area should be:")
    print(f"{int(length)*int(width)}units²")
    print("")
    print("and its perimeter should be:")
    print(f"{2*(int(length)+int(width))}units")


if __name__ == "__main__":
    main()
