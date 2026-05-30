"""Simple quiz game: 5 questions with multiple choice options. Tracks winnings and allows continue/quit after each correct answer."""
Que=["What single word represents the tax regime that recorded its highest-ever single-month collection of ₹2.10 lakh crore?","Which specific metal saw its import duty slashed to 6% in the Union Budget, causing domestic prices to drop sharply?","As of the latest official figures provided in the Economic Survey, which country is the world's largest recipient of inward remittances, receiving an estimated $135.4 billion in FY25?","Driven by strong domestic investment and private consumption, what is the estimated real GDP growth rate for the Indian economy for the financial year FY26?(Give ans in %)","According to the Economic Survey 2025-26, what was India's Gross Fixed Capital Formation (GFCF) as a percentage of GDP in FY25?(Give ans in %)"]
Ans=["GST","Gold","India","7.4","30"]
i=0
j=0
print("""Welcome. Mai Amitabh Bachchan is adbhut khel me aapka swagat krta hu
So, let's start this amazing game
Here is the first question on your computer sucreen:""")
while(i<5):
    while(i>=4):
        print("This is your last question:")
        print(Que[i])
        break
    while(i<4):
        print(Que[i])
        break
    print("""Instruction: Any kind spelling mistake or indentation error may lead to deny the answer. So answer according to the given options.
Good luck""")
    if(i==0):
        print("""Your options are:
customs
excise
GST
VAT""") 
    elif(i==1):
        print("""Your options are:
Copper
Aluminium
Silver
Gold""") 
    elif(i==2):
        print("""Your options are:
China
Mexico
Philippines
India""")
    elif(i==3):
        print("""Your options are:
5.8
6.5
7.4
8""")
    elif(i==4): 
        print("""Your options are:
30
24.6
27
26""")
    else:
        break   
    a=input()
    if(a==Ans[i]):
        j=500000+ (i*1000000)
        print("Congratulations your answer is correct")
        print("Here you won",j, "rupees")
        if(i==len(Que)-1):
            print("Your final winning amount is:", j,"rupees")
            print("Thank you very much for playing")
            print("Have a nice day")
        i=i+1
        while(i<=len(Que)-1):
            print("Do you want to continue the game(yes/no)?")
            b=input()
            k='yes'
            l='no'
            if(b==k):
                print("Here is your next question: ")
                break
            if(b==l):
                print("Ok, so let's end this game")
                print("Your final winning amount is:",j,"rupees")
                print("Thank you very much for playing")
                print("Have a nice day")
                i=i+len(Que)
                continue                
            else:
                print("ERROR!!!")
                print("Please enter correct input as (yes) or (no)" )
    else:
        print("Unfortunately, your answer is incorrect.")
        print("Better luck next time")
        print("Your final winning amount is",j,"rupees")
        print("Thank you very much for playing")
        print("Have a nice day")
        break
