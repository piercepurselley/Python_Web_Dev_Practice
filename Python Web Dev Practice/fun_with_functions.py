# def multiply(arr,num):
#     for x in arr:
#         x *= num
#     return arr
# a = [2,4,10,16]
# b = multiply(a,5)
# print b

# def odd_even(num):
for x in range(0,2001):
    if x % 2 == 0:
        print "Number is " + str(x) + "." + "  This is an even number."
    elif x % 2 !=0:
        print "Number is " + str(x) + "." + "  This is an odd number."



def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
ran_list = [2,4,10,16]
num = multiply(ran_list,5)

print num

# def layered_multiples(arr):
#   # your code here
#   return new_array
# x = layered_multiples(multiply([2,4,5],3))
# print x
# # output
# >>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
layered_multiples[2,2,2]
def layered_multiples(arr):
    new_list = []
    for x in range(0,len(arr)):
        new_array = []
        for j in range(0,arr[x]):
            array.append(1)
        new_list.append(array)
    print new_list
    

