def drawFormation(rows,cols):
    for i in range(rows):
        print("O"*cols)
    print()

def generateFormations(num):
    found = False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            found = True
            rows = num // i
            print(str(i) + ' x ' + str(rows))
            drawFormation(i,rows)
            
    if not found:
        print("Cannot form complete box with "+ str(num) + " participants")
        


participants = int(input("Enter number of participants:"))
generateFormations(participants)