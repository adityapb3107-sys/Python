a=input("Enter your string: ")
if len(a)>=3:
    a1=a[1:len(a)] 
    a1=a1+ a[0]
    while len(a)>=3:
        b=input("Enter any 3 random letters to append: ")
        if len(b)==3:
            a1=a1 + b
            break
        else: 
            print(f"Invalid input!!!\nPlease enter 3 letters only")
            continue
    while len(a)>=3:
        c=input("Enter any 3 random letters to add as prefix: ")
        if len(c)==3:
            a1=c+a1
            break
        else:
            print(f"Invalid input!!!\nPlease enter 3 letters only")
            continue
    print(f"Your code word is: {a1}")
else:
    while len(a)<3:
        b=input("Enter any 3 random letters to append: ")
        if len(b)==3:
            a=a+b
            break
        else:
            print("Invalid input!!!\nPlease enter 3 letters only!")
            continue
    while len(a)<6:
        c=input("Enter any 3 random letters to add as prefix: ")
        if len(c)==3:
            a=c+a
            break
        else:
            print("Invalid input!!!\nPlease enter 3 letters only!")
            continue
    a=a[::-1]
    print(f"Your code word is: {a}")