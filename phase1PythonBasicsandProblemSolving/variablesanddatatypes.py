#data types
age = 25
name = "ram"
pen = "cello"
price = 10.5
is_loggedin = True
haspermission = False
results = None

print(type(age))
print(type(name))
print(type(pen))
print(type(price))
print(type(is_loggedin))
print(type(haspermission))
print(type(results))

#isinstance() checks whether an object belongs to a particular type or class.
print(isinstance(age , float))
print(isinstance(age , int))
print(isinstance(haspermission , bool))
print(isinstance(results , type(None)))

#Type conversion 
age = "32"
age = int(age)
print(age)
print(type(age))

#Integer to float: float()

price = 20
price = float(price)
print(price)
print(type(price))

#Number to string: str()
age = 29
#message = "my age is " + age => wrong cant concatenate str and int so convert int to str
message = "my age is " + str(age)
print(message)

#Convert to Boolean: bool()

print(bool(1))       # True
print(bool(0))       # False
print(bool(""))      # False
print(bool("Hello")) # True
print(bool(None))    # False

#any non-empty string is truthy, including "False".

print(bool("False"))
# True

#Convert to float or integer from text

price = float("58.5")
quantity = int(3)
total = price * quantity

print(total)