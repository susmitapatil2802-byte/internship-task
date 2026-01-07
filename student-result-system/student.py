# Student Result Management System

def main():
    print("---- Student Result System ----")

    name = input("Enter student name: ")
    roll_no = int(input("Enter roll number: "))

    m1 = int(input("Enter marks of Subject 1: "))
    m2 = int(input("Enter marks of Subject 2: "))
    m3 = int(input("Enter marks of Subject 3: "))

    total = m1 + m2 + m3
    percentage = total / 3

    print("\n---- Result ----")
    print("Name:", name)
    print("Roll No:", roll_no)
    print("Total Marks:", total)
    print("Percentage:", percentage)

    if m1 >= 40 and m2 >= 40 and m3 >= 40:
        print("Result: PASS")
    else:
        print("Result: FAIL")


main()
