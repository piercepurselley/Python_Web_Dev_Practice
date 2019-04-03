patrick_info = {'name' : 'Patrick', 'age' : 'immortal', 'origin' : 'Dojo Temple', 'language' : 'ALL'}

patrick_two = {}

patrick_two["name"] = "Patrick"
patrick_two["age"] = "immortal"
patrick_two["origin"] = "Dojo Temple"
patrick_two["language"] = "ALL"

print patrick_two

def dic_function(patrick_info):
    for key, data in patrick_info.items():
        # for value in data:
        for value in data:
            print "My name is ", value["name"]
            print "My age is ", value["age"]
            print "My country of birth is ", value["origin"]
            print "My favorite language is ", value["language"]

dic_function(patrick_info)