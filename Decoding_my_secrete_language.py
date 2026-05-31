a=input("Enter your code word: ")
if len(a)>=9:
    a1=a[3:-4]
    a2=a[-4] + a2
    print(f"Your decoded word is: {a2}")
else:
    a=a[::-1]
    a=a[3:-3]
    print(f"Your decoded word is: {a}")
