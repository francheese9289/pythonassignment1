#Exercise #1 - cube number test
list_num =[]
i = 1
x = 1

while x < 1000:
    x = i**3
    list_num.append(x)
    i += 1
    

print(list_num)


#Exercise #2 - prime numbers
prime = []

for num in range(2, 101):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        prime.append(num)
        
print(prime)

#Exercise #3 - age test
age = int(input ('How old are you? '))

if age < 18:
    print('kids')
elif age >= 18 and age <= 65:
    print ('adults')
else:
    print ('seniors')