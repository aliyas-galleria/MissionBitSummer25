
import pygame
pygame.init()


# Screen setup
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Black Jack")


# Load menu assets
menu_background = pygame.image.load('menu.png').convert()
play_img = pygame.image.load('play.png').convert_alpha()
instruction_img = pygame.image.load('instrution.png').convert_alpha()
quit_img = pygame.image.load('quit.png').convert_alpha()
deal_img = pygame.image.load('deal.png').convert_alpha()
split_img = pygame.image.load('split.png').convert_alpha()


# Button class
class Button():
   def __init__(self, x, y, image, scale):
       width = image.get_width()
       height = image.get_height()
       self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
       self.rect = self.image.get_rect()
       self.rect.topleft = (x, y)
       self.clicked = False


   def draw(self, surface):
       action = False
       pos = pygame.mouse.get_pos()
       if self.rect.collidepoint(pos):
           if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
               self.clicked = True
               action = True
       if pygame.mouse.get_pressed()[0] == 0:
           self.clicked = False
       surface.blit(self.image, (self.rect.x, self.rect.y))
       return action


# Create menu buttons
play_button = Button(290, 350, play_img, 0.5)
instruction_button = Button(290, 380, instruction_img, 0.5)
quit_button = Button(290, 410, quit_img, 0.5)


# === Function to run Blackjack Game ===
def run_blackjack():
   # Load and scale background
   background_img = pygame.image.load('bjs.png').convert()
   scaled_background = pygame.transform.scale(background_img, (screen_width, screen_height))


   # Load card images for all members
   def load_cards(prefix):
       return [
           pygame.image.load(f'{prefix}.png').convert_alpha() for prefix in [
               f"Ace{prefix}", f"2{prefix}", f"3{prefix}", f"4{prefix}", f"5{prefix}",
               f"6{prefix}", f"7{prefix}", f"8{prefix}", f"9{prefix}", f"10{prefix}",
               f"j{prefix}", f"q{prefix}", f"k{prefix}"
           ]
       ]


   winter_cards = load_cards("")
   giselle_cards = load_cards("g")
   ningning_cards = load_cards("n")
   karina_cards = load_cards("k")


   # Create card buttons
   def create_buttons(card_list, y):
       buttons = []
       x = 300
       for img in card_list:
           btn = Button(x, y, img, 0.1)
           buttons.append(btn)
           x += 20
       return buttons


   winter_buttons = create_buttons(winter_cards, 370)
   giselle_buttons = create_buttons(giselle_cards, 250)
   ningning_buttons = create_buttons(ningning_cards, 120)
   karina_buttons = create_buttons(karina_cards, 20)
  


   # Back button (using quit image as a placeholder)
   back_button = Button(20, 450, quit_img, 0.3)
   deal_button = Button(675,300, deal_img, 1)
   split_button = Button(675,350, split_img, 1)


   # Blackjack loop
   running = True
   while running:
       screen.fill((0, 0, 0))  # CLEAR screen to prevent menu leak
       screen.blit(scaled_background, (0, 0))  # Draw blackjack background


       # Draw all card buttons
       for i, btn in enumerate(winter_buttons):
           if btn.draw(screen):
               print(f"Winter card: {i + 1}")
       for i, btn in enumerate(giselle_buttons):
           if btn.draw(screen):
               print(f"Giselle card: {i + 1}")
       for i, btn in enumerate(ningning_buttons):
           if btn.draw(screen):
               print(f"NingNing card: {i + 1}")
       for i, btn in enumerate(karina_buttons):
           if btn.draw(screen):
               print(f"Karina card: {i + 1}")
  




       # Back to menu
       if back_button.draw(screen):
           return  # Exit blackjack screen
       if deal_button.draw(screen):
           print()


       if split_button.draw(screen):
           print()


       pygame.display.update()


       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               exit()


# === Main Game Loop ===
game_state = "menu"
running = True


while running:
   if game_state == "menu":
       screen.blit(menu_background, (0, 0))


       if play_button.draw(screen):
           game_state = "blackjack"
       if instruction_button.draw(screen):
           print("praise winter")
       if quit_button.draw(screen):
           running = False


       pygame.display.update()


       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False


   elif game_state == "blackjack":
       run_blackjack()
       game_state = "menu"  # Return to menu after blackjack


pygame.quit()