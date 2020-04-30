import random
def randInt(min=0, max=100):
    num = round(random.random() * (max - min) + min)
    
    print(round(num))
randInt(min=5, max=10)
randInt(min=5)
randInt(max=10)
randInt()

