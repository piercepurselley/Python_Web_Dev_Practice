l = ['magical',12,[1,2,3],'poop']
sum = 0
new_str = ''
for x in range(0,len(l)):
    if type(l[x]) is str:
        print "This mutha fucka is a string"
        new_str += l[x]
    elif type(l[x]) is int:
        sum += l[x]
    elif type(l[x]) is list:
        print "This ole gal is a list"
    elif type(l[x]) is dict:
        print "... yo... it's a big Dict"

print sum
print new_str