Que=["What is the capital of India?","National animal of India is?","National flower of India is?"]
Ans=["delhi","tiger","lotus"]
i=0
j=0
print("Welcome to KBC.Mai Aditya aapka is adbhut khel me swagat krta hu")
print("Here is the first question on your computer screen:")
while(i<3):
    print(Que[i])
    print("(Give your answer in samll letters only with correct spelling)")
    a=input()
    if(a==Ans[i]):
        j=500000+ (i*1000000)
        print("Congratulations your answer is correct")
        print("Here you won",j, "rupees")
        if(i==len(Que)-1):
            print("Your final winning amount is:", j, "rupees")
            print("Thank you very much for playing")
            print("Waqt aa chuka hai aapse vida lene ka")
            print("Jude rahiye hamare sath milte hai agle episode me")
            print("NAMASKAR")
        i=i+1
        while(i<=2):
            print("Do you want to continue the game(yes/no)?")
            b=input()
            k='yes'
            if(b==k):
                print("Here is your next question: ")
                break
            else:
                print("Ok, so let's end this game")
                print("Your final winning amount is",j,"rupees")
                print("Thank you very much for playing")
                print("Waqt aa chuka hai aapse vida lene ka")
                print("Jude rahiye hamare sath milte hai agle episode me")
                print("NAMASKAR")
                i=i+2
                continue
    else:
        print("Unfortunately, your answer is incorrect.")
        print("Better luck next time")
        print("Your final winning amount is",j,"rupees")
        print("Thank you very much for playing")
        print("Waqt aa chuka hai aapse vida lene ka")
        print("Jude rahiye hamare sath milte hai agle episode me")
        print("NAMASKAR")
        break
