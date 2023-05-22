def drawFormation(rows,cols):
    for i in range(rows):
        print("O"*cols)
    print()

def generateFormations(num):
    for i in range(2,num):
        if num % i == 0:
            rows = num // i
            print(str(i) + ' x ' + str(rows))
            drawFormation(i,rows)

participants = int(input("Enter number of participants:  "))
generateFormations(participants)