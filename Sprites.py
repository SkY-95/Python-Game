import pygame
jump_sprite_list = []
die_sprite_list = []
idle_sprite_list = []
run_sprite_list=[]
back_sprite_list=[]
slash_sprite_list=[]
hurt_sprite_list=[]


#npc
enemy_idle_sprite_list = []
enemy_hurt_sprite_list = []
enemy_die_sprite_list=[]
enemy_shoot_sprite_list=[]

#sfx
blood_sprite_list=[]

def create_sprites():
    #jump
    for i in range(0,40):
        if i<=9:
            path='Stick Swordman/PNG/PNG Sequences/Medium/Jumping/Jumping_00'+str(i)+'.png'
        else:
            path = 'Stick Swordman/PNG/PNG Sequences/Medium/Jumping/Jumping_0' + str(i) + '.png'
        jump_sprite_list.append(pygame.image.load(path))
    #die
    for i in range(0, 20):
        if i <= 9:
            path = 'Stick Swordman/PNG/PNG Sequences/Medium/Dying/Dying_00' + str(i) + '.png'
        else:
            path = 'Stick Swordman/PNG/PNG Sequences/Medium/Dying/Dying_0' + str(i) + '.png'
        die_sprite_list.append(pygame.image.load(path))
    #idle
    for i in range(0,32):
        if i<=9:
            path='Stick Swordman/PNG/PNG Sequences/Medium/Idle/Idle_00'+str(i)+'.png'
        else:
            path = 'Stick Swordman/PNG/PNG Sequences/Medium/Idle/Idle_0' + str(i) + '.png'
        idle_sprite_list.append(pygame.image.load(path))
    # run
    for i in range(0, 13):
        if i <= 9:
            path = 'Stick Swordman/PNG/PNG Sequences/Medium/Running/Running_00' + str(i) + '.png'
        else:
            path = 'Stick Swordman/PNG/PNG Sequences/Medium/Running/Running_0' + str(i) + '.png'
        run_sprite_list.append(pygame.image.load(path))
    #back
    for i in range(10, -1,-1):
        if i <= 9:
            path = 'Stick Swordman/PNG/PNG Sequences/Medium/Back/Running_00' + str(i) + '.png'
        else:
            path = 'Stick Swordman/PNG/PNG Sequences/Medium/Back/Running_0' + str(i) + '.png'
        back_sprite_list.append(pygame.image.load(path))
    #slash
    for i in range(0, 20):
        if i <= 9:
            path = 'Stick Swordman/PNG/PNG Sequences/Medium/Slashing/Slashing_00' + str(i) + '.png'
        else:
            path = 'Stick Swordman/PNG/PNG Sequences/Medium/Slashing/Slashing_0' + str(i) + '.png'
        slash_sprite_list.append(pygame.image.load(path))

    #hurt
    for i in range(0, 16):
        if i <= 9:
            path = 'Stick Swordman/PNG/PNG Sequences/Medium/Hurt/Hurt_00' + str(i) + '.png'
        else:
            path = 'Stick Swordman/PNG/PNG Sequences/Medium/Hurt/Hurt_0' + str(i) + '.png'
        hurt_sprite_list.append(pygame.image.load(path))

    #enemy idle
    for i in range(0, 12):
        if i <= 9:
            path = 'Robot_Asset_Pack/Animations/IdleNew/idle_00' + str(i) + '.png'
        else:
            path = 'Robot_Asset_Pack/Animations/IdleNew/idle_0' + str(i) + '.png'
        enemy_idle_sprite_list.append(pygame.image.load(path))
    #enemy hurt
    for i in range(0, 12):
        if i <= 9:
            path = 'Robot_Asset_Pack/Animations/Damage/Damage_00'+ str(i) + '.png'
        else:
            path = 'Robot_Asset_Pack/Animations/Damage/Damage_0' + str(i) + '.png'
        enemy_hurt_sprite_list.append(pygame.image.load(path))

    for i in range(0, 30):
        if i <= 9:
            path = 'NEw pack blood/1/1_'+ str(i) + '.png'
        else:
            path = 'NEw pack blood/1/1_' + str(i) + '.png'
        blood_sprite_list.append(pygame.image.load(path))
    for i in range(0, 12):
        if i <= 9:
            path = 'Robot_Asset_Pack/Animations/Death/Death_00'+ str(i) + '.png'
        else:
            path = 'Robot_Asset_Pack/Animations/Death/Death_0' + str(i) + '.png'
        enemy_die_sprite_list.append(pygame.image.load(path))
    for i in range(0, 12):
        if i <= 9:
            path = 'Robot_Asset_Pack/Animations/shoot1/Shoot1_00' + str(i) + '.png'
        else:
            path = 'Robot_Asset_Pack/Animations/shoot1/Shoot1_0' + str(i) + '.png'
        enemy_shoot_sprite_list.append(pygame.image.load(path))


def jump():
    return jump_sprite_list
def die():
    return die_sprite_list
def idle():
    return idle_sprite_list
def run():
    return run_sprite_list
def back():
    return back_sprite_list
def slash():
    return slash_sprite_list
def enemy_idle():
    return  enemy_idle_sprite_list
def enemy_hurt():
    return  enemy_hurt_sprite_list
def _blood_():
    return blood_sprite_list
def enemy_die():
    return enemy_die_sprite_list
def enemy_shoot():
    return enemy_shoot_sprite_list
def hurt():
    return hurt_sprite_list