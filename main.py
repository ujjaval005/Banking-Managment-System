import json
import random
import os
import string
from pathlib import Path

class Bank:
    database='data.json'
    Data=[]
    try:
        if Path(database).exists():
            with open(database) as fs:
                Data= json.loads(fs.read())
        else:
            print('No such file exist')
    except Exception as err:
        print(f'an error occur as {err}')

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(cls.Data))

    @staticmethod
    def __accountgenerate():
        alpha=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        spchar=random.choices('!@#$%^&*',k=1)
        id=alpha+num+spchar
        random.shuffle(id)
        return "".join(id)

    def create_account(self):
        info={
            'name':input('Enter your name : '),
            'age':int(input('Enter your age : ')),
            'email':input('Enter your email : '),
            'pin':int(input('enter you 4 digit pin: ')),
            'AccountNo.':Bank.__accountgenerate(),
            'balance':0
        }
        if info['age']<18 or len(str(info['pin'])) !=4:
            print('Your account cant be created check age(>18) or pin')
        else:
            print ('YOUR ACCOUNT CREATED SUCCESSFULLY!')
            
            for i in info:
                print(f'{i} : {info[i]}')
            print('Please note down your account number')    
            Bank.Data.append(info)
            Bank.__update()

    def depositemoney(self):
        accountno=input('Enter your account number :')
        pin=int(input('Enter your 4 digit pin :'))

        userdata=[i for i in Bank.Data if i['AccountNo.']==accountno and i['pin']==pin]

        if userdata== False:
            print('Sorry!,No data found')

        else:
            amount=int(input("Enter Amount : "))
            if amount>10000 or amount<0:
                print ('please deposite amount beetween 0 to 10000 ')
            
            else:
                userdata[0]['balance']+=amount
                Bank.__update()
                print('Amount Deposited Successfully!')

    def withdrawmoney(self):
        accountno=input('Enter your account number :')
        pin=int(input('Enter your 4 digit pin :'))

        userdata=[i for i in Bank.Data if i['AccountNo.']==accountno and i['pin']==pin]

        if userdata== False:
            print('Sorry!,No data found')

        else:
            amount=int(input("Enter Amount : "))
            if userdata[0]['balance'] < amount:
                print ('You dont have that much money')
            
            else:
                userdata[0]['balance']-=amount
                Bank.__update()
                print('Amount Withdrew Successfully!')
                print('Available Balance : ',userdata[0]['balance'])


    def showdetails(self):
        accountno=input('Enter your account number :')
        pin=int(input('Enter your 4 digit pin :'))

        userdata=[i for i in Bank.Data if i['AccountNo.']==accountno and i['pin']==pin]

        if userdata==False:
            print('No data Found!')

        else:
            for i in userdata[0]:
                print(f'{i} : {userdata[0][i]}')



    def updatedetail(self):
        accountno=input('Enter your account number :')
        pin=int(input('Enter your 4 digit pin :'))

        userdata=[i for i in Bank.Data if i['AccountNo.']==accountno and i['pin']==pin]

        if userdata==False:
            print('No data Found!')

        else:
            print('you cannot change the age, account number and balance')

            print('Fill the detail for change or leave empty if no change')

            newdata={
                'name':input('Fill the name or press enter to skip : '),
                'email':input('Enter the email or press enter for skip : '),
                'pin':input('enter pin or press enter for skip :')
            }

            if newdata['name']=="":
                newdata['name']=userdata[0]['name']
            
            if newdata['email']=="":
                newdata['email']=userdata[0]['email']

            
            if newdata['pin']=="":
                newdata['pin']=userdata[0]['pin']

            newdata['age']=userdata[0]['age']
            newdata['AccountNo.']=userdata[0]['AccountNo.']
            newdata['balance']=userdata[0]['balance']

            if type(newdata['pin'])==str:
                newdata['pin']=int(newdata['pin'])

            for i in newdata:
                if newdata[i]==userdata[0][i]:
                    continue
                else:
                    userdata[0][i]=newdata[i]

            Bank.__update()
            print('Detail updated successfully!')


    def Deleteaccount(self):
        accountno=input('Enter your account number :')
        pin=int(input('Enter your 4 digit pin :'))

        userdata=[i for i in Bank.Data if i['AccountNo.']==accountno and i['pin']==pin]
        print(userdata)
        if userdata==False:
            print('No data Found!')
        else:
            check = input('Enter y if you want to delete account else enter n: ')
            if check.lower() == 'n':
                print('Bypass!')
            elif check.lower() == 'y':
                index = Bank.Data.index(userdata[0])
                Bank.Data.pop(index)
                Bank.__update()
                print('Account Deleted Successfully!')
            else:
                print('Invalid choice. Account not deleted.')

 

user=Bank()
print(F'WELCOME TO THE BANK')
print('Press 1 for Creating a account')
print('Press 2 for depositing money')
print('Press 3 for withdrawing money')
print('Press 4 for details')
print('Press 5 for updating details')
print('Press 6 for deleting account')

check = int(input('Enter your choice: '))

match check:
    case 1:
        user.create_account()
    case 2:
        user.depositemoney()
    case 3:
        user.withdrawmoney()
    case 4:
        user.showdetails()
    case 5:
        user.updatedetail()
    case 6:
        user.Deleteaccount()
    case _:
        print('Invalid choice')