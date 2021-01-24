'''for x in range(1, 101):
    if x%7 == 0 or x%10 == 7 or x//10 == 7:
        continue
    print(x)
'''
x = 0
while x < 100:
    x += 1
    if x%7 == 0 or x%10 == 7 or x//10 == 7:
        continue
    else:
        print(x)
