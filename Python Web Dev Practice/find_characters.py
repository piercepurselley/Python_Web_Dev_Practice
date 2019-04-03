word_list = ['hello', 'world', 'my', 'name', 'is', 'Anna']
char = 'o'
new_list = []

#WE ARE GOING FOR...
# new_list = ['hello', 'world']

# print [s for s in list if sub in s]

# for x in range(0,len(word_list)):
#     if let in len(word_list) == char:
#         print "I did it!"

for x in word_list:
    if x.find('o') > -1:
        new_list.append(x)
print new_list

# for x in word_list:
#     x = "hello"


# for x in range(0, len(word_list)):
#     if x
#         print x

