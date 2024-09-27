import pygame, sys
import player_data
import Sprites
import time
from pygame.locals import *

def main():

	screen.fill(color)
	screen.blit(bg, (0, 0))
	moving_sprites.draw(screen)
	moving_enemy_sprites.draw(screen)
	conditions(enemy)
	moving_sprites.update(player_speed,hold,key)
	moving_enemy_sprites.update(enemy_speed)
	blood_sprites.update(1.0)

	player.heath(screen,player_data.player_pos[0],player_data.player_pos[1])
	enemy.enemy_heath(screen, player_data.enemy_pos[0],player_data.enemy_pos[1])
	actions()
	pygame.display.flip()


def draw_game_won_screen():
   screen.fill((0, 0, 0))
   font = pygame.font.SysFont('arial', 40)
   title = font.render('Game won', True, (255, 255, 255))

   quit_button = font.render('Q - Quit', True, (255, 255, 255))
   screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/3))

   screen.blit(quit_button, (screen_width/2 - quit_button.get_width()/2, screen_height/2 + quit_button.get_height()/2))
   pygame.display.update()
   event = pygame.event.wait()
   while True:
	   event = pygame.event.wait()
	   if event.type == QUIT:
		   pygame.quit()
		   sys.exit()
	   elif event.type == KEYDOWN:
		   if event.key == pygame.K_q:
			   pygame.quit()
			   quit()

def draw_game_over_screen():
   screen.fill((0, 0, 0))
   font = pygame.font.SysFont('arial', 40)
   title = font.render('Game Over', True, (255, 255, 255))

   quit_button = font.render('Q - Quit', True, (255, 255, 255))
   screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/3))

   screen.blit(quit_button, (screen_width/2 - quit_button.get_width()/2, screen_height/2 + quit_button.get_height()/2))
   pygame.display.update()
   event = pygame.event.wait()
   while True:
	   event = pygame.event.wait()
	   if event.type == QUIT:
		   pygame.quit()
		   sys.exit()
	   elif event.type == KEYDOWN:
		   if event.key == pygame.K_q:
			   pygame.quit()
			   quit()




class Player(pygame.sprite.Sprite):
	def __init__(self):
		pass
	def heath(self,screen,x,y):
		color=player_data.player_hp()
		pygame.draw.rect(screen,color , pygame.Rect((x+150), (y+40), 100, 20))
		pass
	def current_running_animation(self,cur_anim):
		super().__init__()

		cur_anim=player_data.cur_animation
		self.pos_x=player_data.player_pos[0]
		self.pos_y=player_data.player_pos[1]

		self.animation = True
		if cur_anim=='idle':
			self.sprites = Sprites.idle()
		if cur_anim=='jump':

			self.sprites = Sprites.jump()
		if cur_anim=='die':
			self.sprites = Sprites.die()
		if cur_anim=='run':
			self.sprites = Sprites.run()

		if cur_anim=='back':
			self.sprites=Sprites.back()
		if cur_anim=='slash':

			self.sprites = Sprites.slash()
		if cur_anim=='hurt':
			self.sprites=Sprites.hurt()
			player_data.Player_hp=player_data.Player_hp-20
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [self.pos_x,self.pos_y]

	def animation_stop(self):
		self.animation= False
	def attack(self):
		self.animation = True
	def update(self,speed,hold,key):
		if player_data.cur_animation=="die":
			speed=0.5
		if player_data.cur_animation=="idle":
			speed=0.5
		self.pos_x=player_data.player_pos[0]
		self.pos_y=player_data.player_pos[1]
		if self.animation == True:
			self.current_sprite += speed
			if key=="d":
				self.pos_x+=5
				self.rect.topleft = [self.pos_x+2, self.pos_y]
				player_data.player_pos_(self.pos_x,self.pos_y)
			if key=="a" and player_data.cur_animation=="back":
				self.pos_x-=5
				self.rect.topleft = [self.pos_x, self.pos_y]
				player_data.player_pos_(self.pos_x,self.pos_y)

			if int(self.current_sprite) >= len(self.sprites):
				if player_data.cur_animation=="slash":
					player_data.cur_animation="idle"
				if player_data.cur_animation == "hurt":
					player_data.cur_animation = "idle"
				if player_data.cur_animation=="die":
					pygame.time.wait(1500)
					draw_game_over_screen()
				if key=="a" and int(self.current_sprite) == len(self.sprites) :
					player_data.cur_animation = "idle"
					self.current_sprite = 0
					self.sprites = Sprites.idle()
					self.animation = True
				else:
					self.current_sprite = 0
					self.animation = True
				if hold==False:
					self.sprites = Sprites.idle()
			if player_data.cur_animation!="idle" and self.current_sprite>=len(self.sprites):
				player_data.cur_animation="idle"
		self.image = self.sprites[int(self.current_sprite)]

		#self.image = pygame.transform.scale(self.image, (180, 500))


class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		pass
	def enemy_heath(self,screen,x,y):
		color=player_data.enemy_hp()
		pygame.draw.rect(screen,color , pygame.Rect((x+40), (y-40), 100, 20))
	def current_enemy_animation(self):
		super().__init__()
		self.e_pos_x = player_data.enemy_pos[0]
		self.e_pos_y = player_data.enemy_pos[1]
		self.enemy_cur_anim=player_data.cur_enemy_animation
		if self.enemy_cur_anim=='idle':
			self.enemy_sprite=Sprites.enemy_idle()
		if self.enemy_cur_anim == 'hurt':
			self.enemy_sprite = Sprites.enemy_hurt()
			player_data.Enemy_hp = player_data.Enemy_hp - 20
		if self.enemy_cur_anim=="shoot":
			self.enemy_sprite=Sprites.enemy_shoot()
		if self.enemy_cur_anim=="die":
			self.enemy_sprite=Sprites.enemy_die()

		self.enemy_current_sprite = 0
		self.image = self.enemy_sprite[self.enemy_current_sprite]
		self.image=pygame.transform.flip(self.image, True, False)
		self.image = pygame.transform.scale(self.image, (180, 280))
		self.rect = self.image.get_rect()
		self.rect.topleft = [self.e_pos_x, self.e_pos_y]
	def update(self,speed):
		self.enemy_current_sprite += speed
		player_data.sword_pos = player_data.player_pos[0] + 350
		if int(self.enemy_current_sprite) >= len(self.enemy_sprite):
			if player_data.cur_enemy_animation=="die":
				pygame.time.wait(1500)
				player_data.game_won=1
				draw_game_won_screen()
			if player_data.Enemy_hp<=0:
				pygame.time.wait(1500)
				player_data.game_won = 1
				draw_game_won_screen()


			else:
				player_data.cur_enemy_animation = "idle"
				self.enemy_sprite = Sprites.enemy_idle()
				self.enemy_current_sprite = 0


			self.animation = True
		self.image = self.enemy_sprite[int(self.enemy_current_sprite)]
		self.image = pygame.transform.flip(self.image, True, False)
		self.image = pygame.transform.scale(self.image, (180, 280))

class Sfx(pygame.sprite.Sprite):
	def __init__(self):
		pass
	def blood_animation(self):
		super().__init__()
		self.b_pos_x = player_data.enemy_pos[0]
		self.b_pos_y = player_data.enemy_pos[1]

		self.blood_sprite=Sprites._blood_()


		self.blood_current_sprite = 0
		self.image = self.blood_sprite[self.blood_current_sprite]
		self.image=pygame.transform.flip(self.image, True, False)
		self.rect = self.image.get_rect()
		self.rect.topleft = [self.b_pos_x, self.b_pos_y]
	def update(self,speed):
		if player_data.cur_animation=="slash" :

			self.blood_current_sprite += speed
			if int(self.blood_current_sprite) >= len(self.blood_sprite) :
				self.blood_current_sprite = 0
				self.animation = True
			self.image = self.blood_sprite[int(self.blood_current_sprite)]
			self.image = pygame.transform.flip(self.image, True, False)
			self.image = pygame.transform.scale(self.image, (180, 280))



def dart_draw():
	imp = pygame.image.load("laser.png")

	imp=pygame.transform.scale(imp, (100, 25))
	# Using blit to copy content from one surface to other
	screen.blit(imp, (player_data.dart_location, 547))
	pygame.display.update()
def dart_update():

	if player_data.dart_location<player_data.player_pos[0]+200:

		player_data.dart_fired=0
		player_data.cur_animation="hurt"
		player.current_running_animation(player_data.cur_animation)

	else:
		player_data.dart_location=player_data.dart_location-10


def conditions(enemy):

	if player_data.Enemy_hp<=0and player_data.game_over==0:

		player_data.game_over = 1
		player_data.cur_enemy_animation="die"
		enemy.current_enemy_animation()
	if player_data.sword_pos==player_data.dart_location and player_data.cur_animation=="slash":
		player_data.dart_fired = 0
		player_data.slashed=0

	if player_data.Player_hp<=0  and player_data.game_over==0:
		player_data.game_over=1
		player_data.cur_animation="die"
		player_data.dart_fired=2
		player.current_running_animation(player_data.cur_animation)

	if player_data.dart_fired==1:
		dart_update()
		dart_draw()



	if player_data.sword_pos > player_data.enemy_pos[0] and player_data.cur_enemy_animation!='hurt' and player_data.cur_animation=='slash':

		player_data.cur_enemy_animation = 'hurt'
		enemy.current_enemy_animation()

		player_data.cur_animation="idle"
def actions():

	if player_data.enemy_shoot_tick+3000<pygame.time.get_ticks() and player_data.dart_fired!=2 and player_data.Enemy_hp>10:
		player_data.dart_fired=1
		player_data.dart_location = 950
		dart_draw()
		player_data.cur_enemy_animation="shoot"
		enemy.current_enemy_animation()
		player_data.enemy_shoot_tick=pygame.time.get_ticks()
		player_data.cur_enemy_animation="idle"

def shield():
	imp = pygame.image.load("shield.png")
	imp=pygame.transform.scale(imp, (400, 400))
	# Using blit to copy content from one surface to other
	screen.blit(imp, (player_data.enemy_pos[0]-100, 300))
	pygame.display.update()




# General setup
Sprites.create_sprites()
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 1456
screen_height = 816
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sprite Animation")
color = (255, 255, 0)

# Changing surface color
screen.fill(color)
pygame.display.flip()
# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
moving_enemy_sprites=pygame.sprite.Group()
blood_sprites=pygame.sprite.Group()
dart_sprite=pygame.sprite.Group()
player = Player()
enemy=Enemy()
sfx=Sfx()

player_pos_x=70
player_pos_y=420
player_data.player_pos_(player_pos_x,player_pos_y)

enemy_pos_x=1050
enemy_pos_y=420
player_data.enemy_pos_(enemy_pos_x,enemy_pos_y)

player.current_running_animation('idle')
enemy.current_enemy_animation()
sfx.blood_animation()
moving_sprites.add(player)
moving_enemy_sprites.add(enemy)
blood_sprites.add(sfx)

bg = pygame.image.load("bg3.png")
screen.blit(pygame.transform.scale(bg, (1456, 900)), (0, 0))
pygame.display.flip()
player_speed=0.5
enemy_speed =0.3
hold=False
key=""
while True:
	run=False

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_a:
				player_data.cur_animation="back"
				current_animation="back"
				key="a"
				player_speed=0.5
				player.current_running_animation('back')
			if event.key == pygame.K_w:
				player_data.cur_animation="jump"
				current_animation="jump"
				key="w"

				player.current_running_animation('jump')
			if event.key == pygame.K_d:
				player_data.cur_animation="run"
				hold=True
				current_animation="run"
				key="d"

				player.current_running_animation( 'run')
				player_speed=1
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_d:
				player_data.cur_animation="idle"
				current_animation="idle"
				hold=False
				player_speed=0.5
				key=""
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and player_data.Enemy_hp>0:

			player_data.cur_animation = "slash"
			player.current_running_animation('slash')

			player_data.slashed=1
			key="mouse_left"
			player_speed=1.3

	main()



	clock.tick(60)


