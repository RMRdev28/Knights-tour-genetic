import pygame
import random
class Visualize:
    def __init__(self):
        self.square_size = 90 
        self.visited_squares = [[None for _ in range(8)] for _ in range(8)]

    def update_board(self, screen, font, knight_image, knight_position, move_number,light_assets,dark_assets,color):
        light_square_image_im = pygame.image.load(light_assets)
        dark_square_image_im = pygame.image.load(dark_assets)
        light_square_image = pygame.transform.scale(light_square_image_im, (self.square_size, self.square_size))
        dark_square_image = pygame.transform.scale(dark_square_image_im, (self.square_size, self.square_size))

        x, y = knight_position
        self.visited_squares[x][y] = move_number

        for row in range(8):
            for col in range(8):
                image = light_square_image if (row + col) % 2 == 0 else dark_square_image
                screen.blit(image, (col * self.square_size, row * self.square_size))
                if self.visited_squares[row][col] is not None:
                    number_text = font.render(str(self.visited_squares[row][col]), True, color)
                    screen.blit(number_text, (col * self.square_size + 20, row * self.square_size + 15))

        screen.blit(knight_image, (y * self.square_size + 5, x * self.square_size + 5))
        
        
    def display_game(self,bestSolution):
        pygame.init()
        screen = pygame.display.set_mode((720, 720))
        pygame.display.set_caption("Knight's Tour")
        font = pygame.font.Font(None, 36)
        colors = [(0, 0, 0), (255, 255, 255)]
        light_assets = ["visualization/assets/board_green_light.png", "visualization/assets/board_brown_light.png"]
        dark_assets = ["visualization/assets/board_green_dark.png", "visualization/assets/board_brown_dark.png"]
        knight_images = ["visualization/assets/knight_white.png", "visualization/assets/knight_black.png"]
        i = random.randint(0, 1)
        knight_image = pygame.image.load(knight_images[i])
        knight_image = pygame.transform.scale(knight_image, (80, 80))
        running = True
        index = 0
        clock = pygame.time.Clock()

        while running:
            if index < len(bestSolution.path):
                self.update_board(screen, font, knight_image, bestSolution.path[index], index + 1,light_assets[i],dark_assets[i],colors[i])
                index += 1
                pygame.display.flip()
                clock.tick(2) 
            

