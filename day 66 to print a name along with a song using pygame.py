import pygame
import random
from pygame import mixer
name = input("Enter Youe Name : ")

pygame.init()

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
clr = (r,g,b)
w = len(name) * 100 + 100
win = pygame.display.set_mode((w,500))
pygame.display.set_caption("NAME by Prachiii")

t = {}
t['a'] = pygame.image.load("a.png")
t['b'] = pygame.image.load("b.png")
t['c'] = pygame.image.load("c .png")
t['d'] = pygame.image.load("d.png")
t['e'] = pygame.image.load("e.png")
t['f'] = pygame.image.load("f.png")
t['g'] = pygame.image.load("g.png")
t['h'] = pygame.image.load("h.png")
t['i'] = pygame.image.load("i.png")
t['j'] = pygame.image.load("j.png")
t['k'] = pygame.image.load("k.png")
t['l'] = pygame.image.load("l.png")
t['m'] = pygame.image.load("m.png")
t['n'] = pygame.image.load("n.png")
t['o'] = pygame.image.load("o.png")
t['p'] = pygame.image.load("p.png")
t['q'] = pygame.image.load("q.png")
t['r'] = pygame.image.load("r.png")
t['s'] = pygame.image.load("s.png")
t['t'] = pygame.image.load("t.png")
t['u'] = pygame.image.load("u.png")
t['v'] = pygame.image.load("v.png")
t['w'] = pygame.image.load("w.png")
t['x'] = pygame.image.load("x.png")
t['y'] = pygame.image.load("y.png")
t['z'] = pygame.image.load("z.png")

img = []
for ch in name.lower():
    img.append(t[ch])

mixer.init()
mixer.music.load("ilahi.mp3")
mixer.music.set_volume(0.5)
mixer.music.play()
while True:
    win.fill(clr)
    x = 50
    for i in img:
        win.blit(i, (x, 50))
        x += 100

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
