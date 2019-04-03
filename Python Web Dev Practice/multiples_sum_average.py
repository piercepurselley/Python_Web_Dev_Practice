# #Multiples
for x in range(1,1001):
    if x % 2 != 0:
        print x

for x in range(0,1000001,5):
    print x

# #Sum List
a = [1,2,5,10,255,3]
sum = 0
for x in range(0,len(a)):
    sum = sum + a[x]
print sum

#Average List
a = [1,2,5,10,255,3]
sum = 0
for x in range(0,len(a)):
    sum = sum + a[x]
print sum/len(a)