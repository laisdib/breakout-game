import pygame
import random

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

WIDTH = 893
HEIGHT = 800
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
GREY = (212, 210, 212)
BLACK = (0, 0, 0)
BLUE = (0, 97, 148)

RED = (162, 8, 0)
ORANGE = (183, 119, 8)
GREEN = (0, 127, 33)
YELLOW = (197, 199, 37)

game_score = 0
game_balls = 1
velocity = 5
ang = [2, 3, 4, 5, 6]

paddle_width = 50
paddle_height = 20

all_sprites_list = pygame.sprite.Group()

brick_sound = pygame.mixer.Sound('sounds_brick.wav')
paddle_sound = pygame.mixer.Sound('sounds_paddle.wav')
wall_sound = pygame.mixer.Sound('sounds_wall.wav')


class Brick(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()


class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def move_right(self, pixels):
        self.rect.x += pixels
        if self.rect.x > WIDTH - wall_width - paddle_width:
            self.rect.x = WIDTH - wall_width - paddle_width

    def move_left(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < wall_width:
            self.rect.x = wall_width


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.velocity = [velocity, velocity]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = self.velocity[0]
        self.velocity[1] = -self.velocity[1]


ball = Ball(WHITE, 10, 10)
ball.rect.x = WIDTH // 2 - 5
ball.rect.y = HEIGHT // 2 - 5

paddle = Paddle(BLUE, paddle_width, paddle_height)
paddle.rect.x = WIDTH // 2 - paddle_width // 2
paddle.rect.y = HEIGHT - 65

all_bricks = pygame.sprite.Group()

brick_width = 55
brick_height = 16
x_gap = 7
y_gap = 5
wall_width = 16


def bricks():
    for j in range(8):
        for i in range(14):
            if j < 2:
                if i == 0:
                    brick = Brick(RED, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + (j * (y_gap + brick_height))
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(RED, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = (215 + 0) + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
            if 1 < j < 4:
                if i == 0:
                    brick = Brick(ORANGE, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = (215 + (j * (y_gap + brick_height)))
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(ORANGE, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = (215 + j * (y_gap + brick_height))
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
            if 3 < j < 6:
                if i == 0:
                    brick = Brick(YELLOW, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + (j * (y_gap + brick_height))
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(YELLOW, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 215 + (j * (y_gap + brick_height))
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)

            if 5 < j < 8:
                if i == 0:
                    brick = Brick(GREEN, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(GREEN, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)


bricks()

all_sprites_list.add(paddle)
all_sprites_list.add(ball)


def main(score, balls):
    run = True
    flag = 1

    while run:

        def paused():

            pause = True
            p_font = pygame.font.Font('PressStart2P.ttf', 70)
            p_text = p_font.render('PAUSED', True, COLOR_WHITE, COLOR_BLACK)
            p_text_rect = aux_text.get_rect()
            p_text_rect.center = (HEIGHT // 2, WIDTH // 2)
            screen.blit(p_text, p_text_rect)
            pygame.display.flip()

            while pause:
                for p in pygame.event.get():
                    if p.type == pygame.QUIT:
                        pygame.quit()

                    if p.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            main(score, balls)

                        if p.key == pygame.K_ESCAPE:
                            pygame.quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.key == pygame.K_p:
                paused()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            flag = -1 * (ang[random.randint(0, 4)])
            paddle.move_left(10)
        if keys[pygame.K_RIGHT]:
            flag = 1 * (ang[random.randint(0, 4)])
            paddle.move_right(10)

        all_sprites_list.update()

        if ball.rect.y < 70:
            ball.velocity[1] = -ball.velocity[1]
            wall_sound.play()

        if ball.rect.x >= WIDTH - wall_width - 10:
            ball.velocity[0] = -ball.velocity[0]
            wall_sound.play()

        if ball.rect.x <= wall_width + 10:
            ball.velocity[0] = -ball.velocity[0]
            wall_sound.play()

        if ball.rect.y > HEIGHT:
            ball.rect.x = WIDTH // 2 - 5
            ball.rect.y = HEIGHT // 2 - 5
            ball.velocity[1] = ball.velocity[1]
            balls += 1
            if balls == 4:
                font = pygame.font.Font('PressStart2P.ttf', 70)
                text = font.render("GAME OVER", True, WHITE)
                text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
                screen.blit(text, text_rect)
                pygame.display.update()
                pygame.time.wait(2000)
                run = False

        if pygame.sprite.collide_mask(ball, paddle):
            ball.velocity[0] = flag
            ball.rect.x += ball.velocity[0]
            ball.rect.y -= ball.velocity[1]
            ball.bounce()
            paddle_sound.play()

        brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
        for brick in brick_collision_list:
            ball.bounce()
            brick_sound.play()

            if 380.5 > brick.rect.y > 338.5:
                score += 1
                brick.kill()

            elif 338.5 > brick.rect.y > 294:
                score += 3
                brick.kill()

            elif 294 > brick.rect.y > 254.5:
                score += 5
                brick.kill()

            else:
                score += 7
                brick.kill()

            if len(all_bricks) == 0:
                font = pygame.font.Font('PressStart2P.ttf', 70)
                text = font.render("FINISH!", True, WHITE)
                text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
                all_sprites_list.add(ball)
                screen.blit(text, text_rect)
                pygame.display.update()
                pygame.time.wait(2000)
                run = False

        screen.fill(BLACK)

        pygame.draw.line(screen, GREY, [0, 19], [WIDTH, 19], 40)
        pygame.draw.line(screen, GREY, [(wall_width / 2) - 1, 0], [(wall_width / 2) - 1, HEIGHT], wall_width)
        pygame.draw.line(screen, GREY, [(WIDTH - wall_width / 2) - 1, 0], [(WIDTH - wall_width / 2) - 1, HEIGHT],
                         wall_width)

        pygame.draw.line(screen, BLUE, [(wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2],
                         [(wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2 + 54], wall_width)
        pygame.draw.line(screen, BLUE, [(WIDTH - wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2],
                         [(WIDTH - wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2 + 54], wall_width)

        pygame.draw.line(screen, RED, [(wall_width / 2) - 1, 212.5],
                         [(wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap], wall_width)
        pygame.draw.line(screen, RED, [(WIDTH - wall_width / 2) - 1, 212.5],
                         [(WIDTH - wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap], wall_width)

        pygame.draw.line(screen, ORANGE, [(wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap],
                         [(wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap], wall_width)
        pygame.draw.line(screen, ORANGE, [(WIDTH - wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap],
                         [(WIDTH - wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap], wall_width)

        pygame.draw.line(screen, YELLOW, [(wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap],
                         [(wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap], wall_width)
        pygame.draw.line(screen, YELLOW, [(WIDTH - wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap],
                         [(WIDTH - wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap], wall_width)

        pygame.draw.line(screen, GREEN, [(wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap],
                         [(wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * y_gap], wall_width)
        pygame.draw.line(screen, GREEN, [(WIDTH - wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap],
                         [(WIDTH - wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * y_gap], wall_width)

        font = pygame.font.Font('PressStart2P.ttf', 70)
        text = font.render(str(f"{score:03}"), True, WHITE)
        screen.blit(text, (80, 120))
        text = font.render(str(balls), True, WHITE)
        screen.blit(text, (520, 41))
        text = font.render('000', True, WHITE)
        screen.blit(text, (580, 120))
        text = font.render('1', True, WHITE)
        screen.blit(text, (20, 40))

        all_sprites_list.draw(screen)

        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()


while True:

    for click in pygame.event.get():
        if click.type == pygame.KEYDOWN:
            if click.key == pygame.K_SPACE:
                main(game_score, game_balls)
            if click.key == pygame.K_ESCAPE:
                pygame.quit()
        elif click.type == pygame.QUIT:
            pygame.quit()
        else:
            t_font = pygame.font.Font('PressStart2P.ttf', 70)
            t_text = t_font.render('BREAKOUT', True, COLOR_WHITE, COLOR_BLACK)
            t_text_rect = t_text.get_rect()
            t_text_rect.center = (450, 150)
            initial_font = pygame.font.Font('PressStart2P.ttf', 16)
            aux_font = pygame.font.Font('PressStart2P.ttf', 12)
            initial_text = initial_font.render('Press SPACE to start the game', True, COLOR_WHITE, COLOR_BLACK)
            aux_text = aux_font.render('or Press ESC to exit', True, COLOR_WHITE, COLOR_BLACK)
            aux_text_rect = aux_text.get_rect()
            initial_text_rect = initial_text.get_rect()
            aux_text_rect.center = (450, 650)
            initial_text_rect.center = (450, 350)
            screen.fill(COLOR_BLACK)
            screen.blit(t_text, t_text_rect)
            screen.blit(initial_text, initial_text_rect)
            screen.blit(aux_text, aux_text_rect)
            pygame.display.flip()
