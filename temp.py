# hyeondu
# branch test
# plus
number =int(0)
number2 = int(0)
while ((number < 100) or (number2 < 100)):
    number = int(input("첫번째수 입력"))
    number2 = int(input("첫번째수 입력"))
hun=(int(number2 / 100) * 100)
ten=(int((number2/10)-int(number2/100)*10)*10)
one=(int(number2-(int(number2/100)*100))-int((number2/10)-int(number2/100)*10)*10)
print(number*one)
print(int(number*ten/10))
print(int(number*hun/100))


print(number*number2)

