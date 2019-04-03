#Part I
# output:
# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel

students = [
    {'first_name': 'Michael', 'last_name' : 'Jordan'},
    {'first_name': 'John', 'last_name' : 'Rosales'},
    {'first_name': 'Mark', 'last_name' : 'Guillen'},
    {'first_name': 'KB', 'last_name' : 'Tonel'},
]

def function(students):
    for x in range(0, len(students)):
        print students[x]

function(students)
