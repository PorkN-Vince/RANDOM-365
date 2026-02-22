#Multiplication Table Program

#Multiplication Table Function
def multiplication_table(number):

    #Loop from 1 to 10
    for i in range(1, 11):

        #print table line
        print(f"{number} x {i} = {number * i}")
              
              
#Ask user for a number
num = int(input("Enter a number to see its multiplication table: "))
multiplication_table(num)
