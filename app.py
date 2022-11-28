
print("Tabular Analys !!!!")
print("______________________________")
#class parent
class Bank:
    cash=0
#class child
class access(Bank):
    name="......"
    email="...."
    phone="...."
    password="...."
    AccNo="...."
    def OpenAcc(self,nickname,gmail,phone,passw,SN):
        self.name=nickname
        self.email=gmail
        self.phone=phone
        self.password=passw
        self.AccNo=SN
    
    def GetEmail(self):
        return self.email

    def GetPass(self):
        return self.password    
    def deposit(self,amount):
        print("Your deposit  amount  recieved: ",amount)
        self.cash=self.cash+int(amount)
    
    def withdrew(self,amount):
        print("Your withdrawal  amount  paid: ",amount)
        self.cash=self.cash-int(amount)
    def loan(self,amount):
        print("Your loan  amount  passed: ",amount)
        self.cash=self.cash+int(amount)    
    def   History(self):
        print("\n\n....Your Acount Details.......")
        print("______________________________")
        print("Name: ",self.name)
        print("Email: ",self.email)
        print("Balance: ",self.cash)
        print("______________________________\n\n\n")

#user def
def login(t1,t2):
    print("Enter Email: ")
    temp1=input()
    print("Enter Password: ")
    temp2=input()
    if t1==temp1:

        print("\nYou are welcome!\n")



#mail function
n=100
ac=[]
S=1;
for i in range(n):
    print("\n\n\n")
    print(".......Press Any Key.........","1 for Account open","2 for Account Login","3 for Transection","4 for Account Balance","0 for Account logout",sep="\n")
    ac.append(access())
    press=int(input())
    if press==1:
        
        sam=i
        ac[i]=access()
        userName=input("Enter your name: ")
        userEmail=input("Enter your Egmail: ")
        userPhone=input("Enter your contact No.: ")
        userPass=input("Set Password: ")
        ac[i].OpenAcc(userName,userEmail,userName,userPass,sam)
        print("\nYour Account is Opened and S.No is: ",S)
        S=S+1

    elif press==2:
        SN=int(input("Enter Account S.No: "))
        ac[i]=access()
        
        t1=ac[SN-1].GetEmail()
        t2=ac[SN-1].GetPass()
        login(t1,t2)
    elif press==3:
        ac[i]=access()
        print("\nEnter your Acc S.No: ")
        print("\nPress 1 for Deposit, 2 for Withdral, 3 for Loan, 0 for Exit: ")
        p=int(input())
        if p==1:
            accN=int(input("Acc S.No.: "))
            dip=input("Deposit Tk: ")
            ac[accN-1].deposit(dip)
        elif p==2:
            accN=int(input("Acc S.No.: "))
            withd=input("Withdrawal Tk: ")
            ac[accN-1].withdrew(withd)
        elif p==3:
            accN=int(input("Acc S.No.: "))
            loan=input("Loan Amount: ")
            ac[accN-1].loan(loan)
        elif p==0:
            break            
        

    elif press==4:
        print("\n")
        SN=int(input("Enter Account S.No: "))
        ac[SN-1].History()
    elif press==0:
        break


