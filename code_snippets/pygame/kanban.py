import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)   
GREY = (200, 200, 200)
FONT_SIZE = 30
COLUMN_WIDTH = 200

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kanban Board")
font = pygame.font.Font(None, FONT_SIZE)

class Task:
    def __init__(self, text, position):
        self.text = text
        self.rect= pygame.Rect(position[0],position[1], COLUMN_WIDTH-20, FONT_SIZE+10)
        self.draging = False

    def draw(self, screen):
        pygame.draw.rect(screen, GREY, self.rect)
        text_surface = font.render(self.text, True, BLACK)
        screen.blit(text_surface, (self.rect.x+5, self.rect.y+5 ))


columns = ["To Do", "In Progress", "Done"]
tasks =  [Task("Task 1", (10, 10)), Task("Task 2", (10, 50)), Task("Task 3", (10, 90)),]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for task in tasks:
                if task.rect.collidepoint(event.pos):
                    task.draging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            for task in tasks:
                task.draging = False
        elif event.type == pygame.MOUSEMOTION:
            for task in tasks:
                if task.draging:
                    task.rect.x = event.pos[0] - task.rect.width//2
                    task.rect.y = event.pos[1] - task.rect.height//2
    screen.fill(WHITE)
    for i, column in enumerate(columns):
        x = i * COLUMN_WIDTH
        pygame.draw.rect(screen, BLACK, (x, 0, COLUMN_WIDTH, HEIGHT),2)
        text_surface = font.render(column, True, BLACK)
        screen.blit(text_surface, (x+10, 10))
    
    for task in tasks:
        task.draw(screen)



    pygame.display.flip()

pygame.quit()
sys.exit()
