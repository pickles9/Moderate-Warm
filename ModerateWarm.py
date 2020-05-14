import turtle as trtl
import random as rand
#configures player turtle
player = trtl.Turtle() #makes player turtle
player.pu()
player.speed(0)
player.shape("square")
player.fillcolor("green")
player.goto(0,-60)

#configures score tracker    ADD SCORE COUNTER
scoreBot = trtl.Turtle()
scoreBot.ht()
scoreBot.pu()

``````
#configures window
wn = trtl.Screen() #makes screen variable
wn.bgcolor("black")
wn.title("Try and Survive") #renames window
screen_border = 260
enemy_count = 9

#variable definitions
distance = 20 #distance sprites moves on each game tick
score = 0


enemies = []


#sets up movement controls for player
def up():
    if player.ycor() <= screen_border:
        player.sety(player.ycor()+distance)
        game_update()
def right():
    if player.xcor() <= screen_border:
        player.setx(player.xcor()+distance)
        game_update()
def down():
    if player.ycor() >= -screen_border:
        player.sety(player.ycor()-distance)
        game_update()
def left():
    if player.xcor() >= -screen_border:
        player.setx(player.xcor()-distance)
        game_update()

def game_update():
    for enemy in enemies:
        enemy.forward(distance)
        hit_detection(enemy)
    update_score()

def hit_detection(enemy):
    #print(enemy.distance(player.xcor(), player.ycor()))
    if (enemy.distance(player.xcor(), player.ycor()) < 20):
        print("collision")
        end_game()
    if (enemy.xcor() > screen_border) or (enemy.xcor() < -screen_border) or (enemy.ycor() > screen_border) or (enemy.ycor() < -screen_border):
        #if enemy is on the screen edge, relocate enemy
        relocate(enemy)
        
def relocate(sprite): #moves sprite to new location on the border of the screen
    new_side = rand.randint(0,3) #chooses side that sprite will enter from
    new_loc = distance*(rand.randint(-int(screen_border/distance), int(screen_border/distance))) #chooses where on that side the sprite will enter

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

def end_game():
    print(score)
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

print(0/0
def update_score():
    global score
    score += 1

#TESTING ENEMY COLLISION
for i in range(0,enemy_count):
    enemies.append(trtl.Turtle())
for enemy in enemies:
    enemy.pu()
    enemy.shape("square")
    enemy.right(90)
    enemy.fillcolor("red")
    enemy.speed(0)
    relocate(enemy)

#controls for player
wn.onkey(up, "Up")
wn.onkey(right,"Right")
wn.onkey(down,"Down")
wn.onkey(left,"Left")
wn.listen() 
wn.mainloop()