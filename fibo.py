a, b = 0, 1
count=0
n=int(input(' enter any any number : '))
if n <= 0:
   print('number is invalid')
elif n == 1:
   print('fibonacci numbers are : ',n,':')
   print(a)
else:
   print('fibanacci numbers are : ')
   while count <= 10:
       print('fiboancci numbers are : ', a)
       c=a+b
       a=b
       b=c
       count += 1
