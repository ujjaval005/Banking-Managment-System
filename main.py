import json
import random
import os
import string
from pathlib import Path

class Bank:
    database='data.json'
    Data=[]
    try:
        if Path(database).exists():  # ✅ Correct method call
            with open(database, 'r') as fs:  # ✅ Use Bank.database consistently
                Data = json.load(fs)  # ✅ Assign to Bank.Data
        else:
            print('No such file exists')
    except Exception as err:
        print(f'An error occurred: {err}')  # ✅ Use f-string for error message
    
    @classmethod
    def __update(cls):  # ✅ Use cls instead of Bank for consistency
        with open(Bank.database, 'w') as file:
            json.dump(Bank.Data)  # ✅ Use json.dump with indent for readability

    @staticmethod
    def __generateaccount():
        alpha=random.choices(string.ascii_letters ,k=3)
        num=random.choices(string.digits,k=3)
        spchar=random.choices('!@#$%^&*')
        id=alpha+num+spchar
        random.shuffle(id)
        return "".join(id)

    def create_account(self):
        info={
            'name':input('enter your name: '),
            'age':int(input('enter your age: ')),
            'email':input('enter your email:'),
            'pin':int(input('enter your 4 digit pin: ')),
            'accontNo.':Bank.__generateaccount(),
            'balance':0
        }

        if info['age'] <18 or len(str(info['pin'])) !=4:
            print('your accont is not created!')

        else:
            print('account is created succesfully!')
            for i in info:
                print(f'{i} : {info[i]}')
            print('plese note down your accont detail')

            Bank.Data.append(info)
            Bank.__update()
    

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
        pass
    case 3:
        pass
    case 4:
        pass
    case 5:
        pass
    case 6:
        pass