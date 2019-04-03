Part I

arr = [4,6,1,3,5,7,25]

def draw_stars(arr):
    for x in range(0,len(arr)):
        print arr[x]*"*"
        #as many times as at the index(x)

draw_stars(arr)

Part II

arr = [4,"Tom",1,"Michael",5,7,"Jimmy Smith"]
result = 0

def draw_stars(arr):
    for x in range(0,len(arr)):
        if isinstance(arr[x],int):
            print arr[x]*"*"
        elif isinstance(arr[x],str):
            for x in range(0,len(arr[x])):
                result += arr[0].lower
                print result
        #as many times as at the index(x)

draw_stars(arr)