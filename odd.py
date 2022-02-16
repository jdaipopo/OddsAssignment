import re 

def A(X):
    a = str(X)
    k1 = ''
    for i in range(len(a)):
        if (int(a[i]) % 2 == 0):
            k1 = k1 + ("Even"+a[i])
        else:
            k1 = k1 + ("Odd"+a[i])
    return k1

def B(X):
    k2 = ''
    result = ''
    for i in X :
        if (i.isdigit()) :
            result = result + k2.upper()[::-1] + i
            k2 = ''
        else :
            k2 = k2 + i 
    return result

def C(X):
    k3 = ''
    result = ''
    for i in X :
        if (i.isdigit()) :
            result = result + i
        else :
            result = result + str(ord(i))
    return result  

def D(X):
    #k4 = ''
    result = ''
    i = 0
    while True :
        if(X[i] == '6') :
            result = result + 'DDO' + X[i+6]
            i += 7
        else :
            result = result + 'NEVE' + X[i+8]
            i += 9
        if (i >= len(X)) : 
            break
    return result

def E(X):
    k5 = ''
    result = ''
    result2 = ''
    for i in X :
        if (i.isdigit()) :
            result = result + k5.lower()[::-1] + i
            k5 = ''
        else :
            k5 = k5 + i 
    e = str(result)
    for i in range(len(result)) :
        if (result[i]=='o') :
            result2 += result[i].upper()
        elif (result[i]=='e' and result[i:i+2]=='ev') :
            result2 += result[i].upper()
        else :
            result2 += result[i]
    return result2

def F(X):
    k6 = ''
    result = ''
    for i in X :
        if (i.isdigit()) :
            result = result + i
    return result

X = int(input('Enter Number --> '))

result = A(X)
print(result)

result = B(result)
print(result)

result = C(result)
print(result)

result = D(result)
print(result)

result = E(result)
print(result)

result = F(result)
print(result)