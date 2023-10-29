'''for i in range(1,10):
    print(i*i)'''
no = int(input("Enter the number:"))
for i in range(10):
    if no%2 !=0 and no%3 !=0 and no%5!=5:
        print("NOT")
        break
        # if no%5 !=0:
        #     print("The given number is not divisible by 2,3,5")
        #     break
    else:
        print("The number is divisible by 2,3,5")
        break




