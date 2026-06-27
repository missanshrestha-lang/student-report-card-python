z="yes"
while z=="yes":

    print()
    print()
    print()
    a=str(input("Enter your name: "))
    b=int(input("Enter your roll number: "))
    c=int(input("Enter your marks in English: "))
    d=int(input("Enter your marks in Math: "))
    e=int(input("Enter your marks in computer: "))
    print()
    print()
    total=c+d+e
    AVG=total/3
    print("====================================")
    print("Report Card".title().center(35))
    print("====================================")
    print()
    print("Name               :",a)
    print("Roll No            :",b)
    print()
    print("Marks in English   :",c)
    print("Marks in Math      :",d)
    print("Marks in Computer  :",e)
    print()
    print("------------------------------------")
    print("Total marks        :",total)
    print("Average marks      :",AVG)
    print()
    if 90<=AVG<=100:
        print("Result          : Pass")
        print("Grade           : A+")
    elif 80<=AVG<90:
        print("Result          : Pass")
        print("Grade           : A")
    elif 70<=AVG<80:
        print("Result          : Pass")
        print("Grade           : B")
    elif 60<=AVG<70:
        print("Result          : Pass")
        print("Grade           : C")
    else:
        print("Result          : Fail")
        print("Grade           : F")
    print()
    print("====================================")
    print()
    print() 
    z=str(input("Do you want to enter another student's marks?(yes/no): "))


    