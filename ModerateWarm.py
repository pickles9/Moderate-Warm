#GAME MODIFIERS
speed = 9
distance = 20 #distance sprites moves on each game tick
score = 0 #player's score
enemy_count = 10 #number of enemies spawned

#imports
import turtle as trtl
import random as rand #for random relocating

#configures player turtle
player = trtl.Turtle() #makes player turtle
player.pu()
player.speed(speed)
player.shape("square")
player.fillcolor("green")
player.goto(0,-60)

#configures score printer
scoreBot = trtl.Turtle()
scoreBot.ht()
scoreBot.pu()
scoreBot.color("white")
scoreBot.goto(-270,270)
font = ("Arial", 20, "normal")

#configures window
wn = trtl.Screen() #makes screen variable
wn.bgcolor("black")
wn.title("Try and Survive") #renames window
screen_border = 260


#variable definitions
ready = True #signals when game has made all calculations
gameactive = True #prevents players from scoring points after game ends
enemies = [] #list of enemies


#sets up movement controls for player
def up():
    if (player.ycor() <= screen_border) and ready:
        player.sety(player.ycor()+distance)
        game_update()
def right():
    if (player.xcor() <= screen_border) and ready:
        player.setx(player.xcor()+distance)
        game_update()
def down():
    if (player.ycor() >= -screen_border) and ready:
        player.sety(player.ycor()-distance)
        game_update()
def left():
    if (player.xcor() >= -screen_border) and ready:
        player.setx(player.xcor()-distance)
        game_update()

def game_update(): #runs each time player moves
    global ready
    ready = False
    for enemy in enemies: #itterates through each enemy and moves them forward
        enemy.forward(distance)
        hit_detection(enemy)
    update_score()
    ready = True

def hit_detection(enemy): #checks to see if sprite is touching player or wall
    if (enemy.distance(player.xcor(), player.ycor()) < 20):
        print("collision")
        end_game()
    if (enemy.xcor() > screen_border) or (enemy.xcor() < -screen_border) or (enemy.ycor() > screen_border) or (enemy.ycor() < -screen_border):
        #if enemy is on the screen edge, relocate enemy
        relocate(enemy)
        
def relocate(sprite): #moves sprite to new location on the border of the screen
    new_side = rand.randint(0,3) #chooses side that sprite will enter from
    new_loc = distance*(rand.randint(-int(screen_border/distance), int(screen_border/distance))) #chooses where on that side the sprite will enter
    sprite.speed(0)

    if new_side == 0:
        sprite.goto(new_loc, screen_border)
        sprite.setheading(270)

    elif new_side == 1:
        sprite.goto(screen_border, new_loc)
        sprite.setheading(180)

    elif new_side == 2:
        sprite.goto(new_loc, -screen_border)
        sprite.setheading(90)

    else:
        sprite.goto(-screen_border, new_loc)
        sprite.setheading(0)
    sprite.speed(speed)

def end_game():
    global gameactive
    gameactive = False
    #Disables player movement
    wn.onkey(None, "Up") 
    wn.onkey(None,"Right")
    wn.onkey(None,"Down")
    wn.onkey(None,"Left")
    player.ht()
    player.goto(500, 500)
    for enemy in enemies:
        enemy.ht()
        enemy.goto(500, 550)

print(0/0 add game over screen
def update_score():
    global score
    if gameactive:
        score += 1
        scoreBot.clear()
        scoreBot.write(score,font=font,align="center")

#Enemy Spawner
for i in range(0,enemy_count): #moves all enemies into a list for easy management
    enemies.append(trtl.Turtle()) 

for enemy in enemies: #Configures enemy and moves in somewhere on the map
    enemy.pu()
    enemy.shape("square")
    #enemy.right(90)
    enemy.fillcolor("red")
    enemy.speed(speed)
    relocate(enemy)

#controls for player
wn.onkey(up, "Up")
wn.onkey(right,"Right")
wn.onkey(down,"Down")
wn.onkey(left,"Left")
wn.listen() 
wn.mainloop()