
# arr[x]
# head = 0
# tails = 1
# var side
# head_count = 0
# tail_count = 1
# for x in range(0,5000)

# "Attempt #" + arr[x] + "Throwing a coin... It's a " + head/tail + "! ... Got " + count + head/tail + " so far and " + count + head/tail + " so far"

# coin_toss()
import random

def coin_toss():
    # arr = []
    count_heads = 0
    count_tails = 0
    count_flips = 0
    heads_tails = ''
    coin = random.randint(0,1)
    # for x in range(0,5001):
    #     import random
    #     coin = randomint(0,1)
    #     if random_num > 0:
    #         side = True:

    while count_flips <= 5000:
        if coin == 1:
            heads_tails = "heads"
            count_heads += 1
            count_flips += 1
        elif coin != 1:
            heads_tails = "tails"
            count_tails += 1
            count_flips += 1
        print ("Attempt #" + str(count_flips) + " Throwing a coin... It's a " + str(heads_tails) + "! ... Got " + str(heads_tails) + str(heads_tails) + " so far and " + str(count_flips) + " " + str(heads_tails) + " so far")

coin_toss()

