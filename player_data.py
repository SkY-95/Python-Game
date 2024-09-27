global player_pos
global enemy_pos
global Enemy_hp
player_pos=[0,0]
enemy_pos=[1050,420]
sword_pos = player_pos[0]
game_over=0
game_wom=0
slashed=0
shield=1

dart_fired=0
dart_location=950

cur_animation="idle"
cur_enemy_animation="idle"

Player_hp = 100
Enemy_hp=100
enemy_shoot_tick=0
hp_color="green"
def player_pos_(x,y):

    if x > 1200:
        x = 1200
    if x<0:
        x=0
    if (x+300) >enemy_pos[0]:

        x=enemy_pos[0]-300


    player_pos[0]=x
    player_pos[1]=y
def enemy_pos_(x,y):
    if x > 1200:
        x = 1200
    if x<0:
        x=0
    enemy_pos[0]=x
    enemy_pos[1]=y
def player_hp():
    if Player_hp>=80:
        hp_color='green'
    elif 50<=Player_hp<80:
        hp_color="yellow"
    elif 20<=Player_hp<50:
        hp_color="orange"
    elif Player_hp<20:
        hp_color="red"
    else:
        hp_color="black"
    return hp_color

def enemy_hp():
    if Enemy_hp>=80:
        hp_color='green'
    elif 50<=Enemy_hp<80:
        hp_color="yellow"
    elif 20<=Enemy_hp<50:
        hp_color="orange"
    elif Enemy_hp<20:
        hp_color="red"
    else:
        hp_color="black"
    return hp_color
def reset():
    player_pos = [0, 0]
    enemy_pos = [1050, 420]
    sword_pos = player_pos[0]
    game_over = 0

    cur_animation = "idle"
    cur_enemy_animation = "idle"

    Player_hp = 100
    Enemy_hp = 100
    hp_color = "green"
