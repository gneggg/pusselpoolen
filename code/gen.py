
import random as rd

def generate_puzzle_data():
    data = []
    for i in range(10):
        pieces = 0
        age = rd.randint(3, 19)
        if 3 <= age <= 7:
            pieces = rd.randint(10,50)
        elif 7 <= age <= 10:
            pieces = rd.randint(50,100)
        elif 10 <= age <= 13:
            pieces = rd.randint(100,200)
        elif 13 <= age <= 16:
            pieces = rd.randint(200,500)
        else:
            pieces = rd.randint(500,1000)
        data.append((age, pieces))
    return data 

def generate_boardgame_data():
    data = []

    return data

print(generate_puzzle_data())

'''
    name: 
    tags: list of things from names?)
    age: 7+ eg (should be parsed as int)
    pieces: int
    size: string of w*h (might be unnecessary)''' 