a = int(input())
b = int(input())
c = int(input())
grade = a + b + c
if grade >= 80 and grade <= 100:
    print('A')
elif grade >= 75 and grade <= 79:
    print('B+')
elif grade >= 70 and grade <= 74:
    print('B')
elif grade >= 65 and grade <= 69:
    print('C+')
elif grade >= 60 and grade <= 64:
    print('C')
elif grade >= 55 and grade <= 59:
    print('D+')
elif grade >= 50 and grade <= 54:
    print('D')
else:
    print('F')
    