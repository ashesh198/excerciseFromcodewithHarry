import datetime


def gettime():
    return datetime.datetime.now()

print("health management system: ")
a = int(input("Press 1 for log the value and 2 for retrieve "))

if a == 1:
    b = int(input("Press 1 for ashesh 2 for rohan 3 for hammad "))
    if b == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("ashesh-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("ashesh-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (b == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("rohan-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("rohan-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (b == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("hammad-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("hammad-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("invalid number")
else:
    b = int(input("Press 1 for ashesh 2 for rohan 3 for hammad "))
    if b == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("ashesh-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("ashesh-food.txt") as op:
                for i in op:
                    print(i, end="")

    elif (b == 2):
                c = int(input("enter 1 for excersise and 2 for food"))
                if (c == 1):
                    with open("rohan-ex.txt") as op:
                        for i in op:
                            print(i, end="")
                elif (c == 2):
                    with open("rohan-food.txt") as op:
                        for i in op:
                            print(i, end="")
    elif (b == 3):
                c = int(input("enter 1 for excersise and 2 for food"))
                if (c == 1):
                    with open("hammad-ex.txt") as op:
                        for i in op:
                            print(i, end="")
                elif (c == 2):
                    with open("hammad-food.txt") as op:
                        for i in op:
                            print(i, end="")
    else:
        print("invalid number")

