guestList = ['Luna', 'grandma', 'ty', 'feli']
message = "Come to dinner at my house "
print(message + guestList[0].title())
print(message + guestList[1].title())
print(message + guestList[2].title())
print(message + guestList[3].title())
#guest who cant make it challenge
print(guestList[2].title() + " cannot make it to dinner")
guestList[2] = 'Des'
print(message + guestList[2].title())
#using append
guestList.append('Bob')
print(message + guestList[4].title())
#using insert
guestList.insert(1, 'Steve')
print(message + guestList[1].title())
print(message + guestList[5].title())
#deleting guests
del guestList[1]
print(message + guestList[1].title())
print(guestList)
guestList.pop(3)
print(guestList)
guestList.pop()
print(guestList)
guestList.pop()
print(guestList)
guestList.pop()
print(guestList)
guestList.pop()
print(guestList)
print(3 ** 2) #testing exponents

