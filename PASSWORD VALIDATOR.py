'''
Write aprogram that takes in a string as a password minimum 2 numbers , 2 special symbols and length of password less
than 7 characters
'''
def isvalid(passwd):
    if(len(passwd)<7):
        return 'Weak'
    count = specialchar = 0
    for char in passwd:
        if char.isdigit():
            count += 1
        elif char in ('!','@','#','$','%','&','*'):
            specialchar += 1
    if count >= 2 and specialchar >= 2:
        return 'Strong'
    else:
        return 'Weak'
s = input()
res = isvalid(s)
print(res)







































































