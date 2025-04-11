import re
import calendar 
#Name
x = True
while x:
    pattern = re.compile(r'^[A-Za-z ]+$')
    text = input("Enter Your Name: ")
    res = pattern.fullmatch(text)
    if res != None:
        name = res.group()
        break
    else:
        print("Enter Name in Correct Format !")
#Date of Birth
while True:
    pattern = re.compile(r'(\d{2})-(\d{2})-(\d{4})')
    text = input("Enter Date of Birth (dd-mm-yyyy): ")
    res = pattern.fullmatch(text)
    if res is not None:
        day = res.group(1)
        month_num = int(res.group(2))
        year = res.group(3)
        month_name = calendar.month_name[month_num]  # Converts 1 → 'January'
        break
    else:
        print("Enter DOB in Correct Format!")
#Email id
while True:
    pattern = re.compile(r'[a-z0-9]+@gmail.com\Z')
    text = input("Enter Email id: ")
    res = pattern.fullmatch(text)
    if res != None:
        mailid = res.group()
        break
    else:
        print("Enter Mail id in correct format !")
#Mobile Number
while True:
    pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
    text = input("Enter Mobile Number: ")
    res = pattern.fullmatch(text)
    if res != None:
        mobile = res.group()
        result = re.sub(r'-', '', text)
        break
    else:
        print("Enter Mobile Number in correct Format !")
print(f"Name : {name}")
print(f"Date of Birth : {day} {month_name} {year}")
print(f"Mail id: {mailid}")
print(f"Mobile : {result}")
