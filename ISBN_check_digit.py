ISBNCode = input("Enter the ISBN code here: ")
ISBNCode = list(ISBNCode)

oddPosTotal = 0
evenPosTotal = 0

for oddNum in range(0, 12, 2):
    oddPosTotal += int(ISBNCode[oddNum])
for evenNum in range(1, 12, 2):
    evenPosTotal += int(ISBNCode[evenNum]) 
evenPosTotal *= 3

if ((int(oddPosTotal + evenPosTotal) + int(ISBNCode[12])) % 10) != 0:
    print("Invalid")
else:
    print("Valid")