import turtle as t
import random

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color= (r, g, b)
    return random_color



for _ in range(200):
    t.color(random_color())
    t.right(29)
    t.speed(100)
    r = 50
    t.circle(r)