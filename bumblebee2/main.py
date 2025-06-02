import pgzrun
from random import randint
HEIGHT=600
WIDTH=600

score = 0
game_over = False


wasp=Actor('bee')
wasp.pos=100,100

flower=Actor('flower')
flower.pos=100,300

def draw():
    screen.fill('white')
    wasp.draw()
    flower.draw()
    screen.draw.text('score: '+ str(score),color = 'black',topleft= (10,10))

if game_over:
        screen.fill('pink')
        screen.draw.text('Game over, your final score is:    '+str(score),fontsize=30, color='black',midtop=(WIDTH/2,10))

def place_flower():
    flower.x=randint(70, (WIDTH-70))
    flower.y=randint(70, (HEIGHT-70))
def time_out():
    global game_over
    game_over= True
def update():
    global score
    if keyboard.left:
        wasp.x=wasp.x-5
    if keyboard.right:
        wasp.x=wasp.x+5
    if keyboard.up:
        wasp.y=wasp.y-5
    if keyboard.down:
        wasp.y=wasp.y+5
    
    flower_collected= wasp.colliderect(flower)
    if flower_collected:
        score+=10
        place_flower()
clock.schedule(time_out,60.0)
pgzrun.go()

