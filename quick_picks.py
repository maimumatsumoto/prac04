import random



def main():

    picklist=[]

    pick = int(input("How many quick picks"))

    while pick<0:
        print("Invalid number.")
        pick=int(input("How many quick picks?"))


    for i in range(pick):
        picklist = []
        for x in range(6):
            number=random.randint(1,45)
            while number in picklist:
                number=random.randint(1,45)
            picklist.append(number)

        picklist.sort()

        print(" ".join("{:3}".format(number) for number in picklist))

main()