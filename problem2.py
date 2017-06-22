def fibonnaci(n):
    list = [1, 1]
    for i in range(2,n+1):
        list.append(list[i-1] + list[i-2])
    return list[len(list)-1]

sum = 0
n = 0

while (fibonnaci(n) < 4000000):
    if fibonnaci(n) % 2 != 0:
        n += 1
    else:
        sum += fibonnaci(n)
        n += 1

print("The sum of even fibonnaci numbers lower than 4.000.000 is: ", sum)