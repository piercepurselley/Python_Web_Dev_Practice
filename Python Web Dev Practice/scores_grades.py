def scores():
    arr = []
    for x in range(0,10):
        import random
        random_num = random.randint(60,100)
        arr.append(random_num)
        display_grade = "Scores and Grades" + "\n"
    for y in range(0, len(arr)):
        if arr[y] > 89:
            print "Score: " + str(arr[y]) + ";  Your grade is A" 
        elif arr[y] > 79 and arr[y] > 88:
            print "Score: " + str(arr[y]) + ";  Your grade is B"
        elif arr[y] > 69 and arr[y] > 78:
            print "Score: " + str(arr[y]) + ";  Your grade is C"
        elif arr[y] > 0 and arr[y] > 68:
            print "Score: " + str(arr[y]) + ";  Your grade is D"
scores()
    