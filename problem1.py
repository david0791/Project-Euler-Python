def multiplesOf3And5(n) :
    sum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0 :
            sum += i
    return sum

print(multiplesOf3And5(1000))