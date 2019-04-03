name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(name, favorite_animal):
    new_tuple = zip(name,favorite_animal)
    news = dict(new_tuple)
    print news

make_dict(name,favorite_animal)
