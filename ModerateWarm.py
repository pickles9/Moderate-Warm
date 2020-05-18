#GAME MODIFIERS
speed = 0 #speed the turtles are set to
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
scoreBot.speed(0)
scoreBot.ht()
scoreBot.pu()
scoreBot.color("white")
scoreBot.goto(-270,270)
font = ("Arial", 20, "normal") #creates font variable for text

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
    if (player.ycor() <= screen_border) and ready: #checks if player is within screen borders and the game currently isn't moving enemies
        player.sety(player.ycor()+distance) #moves player
        game_update() #moves all enemies
def right():
    if (player.xcor() <= screen_border) and ready: #checks if player is within screen borders and the game currently isn't moving enemies
        player.setx(player.xcor()+distance) #moves player
        game_update() #moves all enemies
def down():
    if (player.ycor() >= -screen_border) and ready: #checks if player is within screen borders and the game currently isn't moving enemies
        player.sety(player.ycor()-distance) #moves player
        game_update() #moves all enemies
def left():
    if (player.xcor() >= -screen_border) and ready: #checks if player is within screen borders and the game currently isn't moving enemies
        player.setx(player.xcor()-distance) #moves player
        game_update() #moves all enemies

def game_update(): #runs each time player moves
    global ready #gets global variable used to show if game is moving enemies
    ready = False #disables player input
    for enemy in enemies: #itterates through each enemy and moves them forward
        enemy.forward(distance) #moves enemy
        hit_detection(enemy) #checks to see if enemy is touching player
    update_score() #updates the player's score
    ready = True #re-enables player controls

def hit_detection(enemy): #checks to see if sprite is touching player or wall
    if (enemy.distance(player.xcor(), player.ycor()) < 20): #ends game if player is touching enemy
        end_game()
    if (enemy.xcor() > screen_border) or (enemy.xcor() < -screen_border) or (enemy.ycor() > screen_border) or (enemy.ycor() < -screen_border):
        #^if enemy is on the screen edge, relocate enemy
        relocate(enemy)
        
def relocate(sprite): #moves sprite to new location on the border of the screen
    new_side = rand.randint(0,3) #chooses side that sprite will enter from
    new_loc = distance*(rand.randint(-int(screen_border/distance), int(screen_border/distance))) #chooses where on that side the sprite will enter
    sprite.speed(0) #speeds up sprite
    #Uses the random number to choose which screen edge the enemy spawns at
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

def end_game(): #ends game
    global gameactive #gets global variable
    gameactive = False #disables score updating

    #Disables player movement
    wn.onkey(None, "Up") 
    wn.onkey(None,"Right")
    wn.onkey(None,"Down")
    wn.onkey(None,"Left")

    #moves score printer and prints "game over" and the player's score
    scoreBot.clear()
    scoreBot.goto(0,50)
    scoreBot.write("Game over", font=font, align="center")

    player.ht()
    player.goto(500, 500)

    scoreBot.goto(0,-50)
    scoreBot.write("You survived for " + str(score) + " turns", font=font, align="center")

    for enemy in enemies:
        enemy.ht()
        enemy.goto(500, 550)
    
def update_score(): #changes score
    global score #gets score variable
    if gameactive: #Checks to see if the game is over
        score += 1 #updates score
        scoreBot.clear() #clears any writing the turtle has writen
        scoreBot.write(score,font=font,align="center") #writes new score

#Enemy Spawner
for i in range(0,enemy_count): #moves all enemies into a list for easy management
    enemies.append(trtl.Turtle()) #adds each enemy to the list enemies

#Enemy mover
for enemy in enemies: #Configures enemy settings and moves it somewhere on the map
    enemy.pu()
    enemy.shape("square")
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