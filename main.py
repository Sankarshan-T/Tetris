import pygame, sys, time
from game import Game
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 40)

score_surface = title_font.render("Score", True, Colors.white)
score_rect = pygame.Rect(320, 55, 170, 60)

next_surface = title_font.render("Next", True, Colors.white)
next_rect = pygame.Rect(320, 215, 170, 180)

game_over_surface = title_font.render("GAME OVER", True, Colors.white)
game_over_time = time.time()

small_font = pygame.font.Font(None, 20)
re_line1 = small_font.render("Press 'R' key to restart", True, Colors.white)
re_line2 = small_font.render("after 10 seconds", True, Colors.white)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over and game_over_time and time.time() - game_over_time > 10:
                 if event.key == pygame.K_r:
                    if game.game_over == True:
                        game.game_over = False
                        game_over_time = None
                        game.reset()
                        
            else:
                if event.key == pygame.K_LEFT and game.game_over == False:
                    game.move_left()
                if event.key == pygame.K_RIGHT and game.game_over == False:
                    game.move_right() 
                if event.key == pygame.K_DOWN and game.game_over == False:
                    game.move_down() 
                if event.key == pygame.K_UP and game.game_over == False:
                    game.rotate() 
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
                
    
    #Drawing:

    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.fill(Colors.darkBlue)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    if game.game_over:
        if game_over_time is None:
            game_over_time = time.time()    
        screen.blit(game_over_surface, (320, 450))
        screen.blit(re_line1, (340, 490))
        screen.blit(re_line2, (350, 510))

    pygame.draw.rect(screen, Colors.lightBlue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx,
                                                                centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.lightBlue, next_rect, 0, 10)

    game.draw(screen)
    pygame.display.update()
    clock.tick(60)