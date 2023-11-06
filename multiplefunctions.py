class multiplefunctions():
    def BMI():
        BMI=int(input("Enter the BMI Index:"))
        if(BMI<18.5):
            print("under weight")
            message="under weight"
        elif(BMI<24.9):
            print("normal")
            message="normal"
        elif(BMI<29.9):
            print("over weight")
            message="over weight"
        else:
            print("very over weight")
            message="very over weight"
        return message
    
    def oddEven():
        num=int(input("enter the number:"))
        if((num%2)==1):
            print("odd number")
            message="odd number"
        else:
            print("even number")
            message="even number"
        return message
    