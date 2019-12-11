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
            while number in picklist:  #for when there is a same number in the line
                number=random.randint(1,45) #get the number again
            picklist.append(number) #add onto the list

        picklist.sort() #make the numbers in order (small to big)

        print(" ".join("{:3}".format(number) for number in picklist))
                        #3 spacing
main()