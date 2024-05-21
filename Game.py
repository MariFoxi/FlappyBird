import pygame as pg
from random import randint
from time import sleep
from Bird import *
from Pipe import *
from Ground import *

class Game:
    def __init__(self) -> None:
        pg.init()

        # размеры экрана
        self.screen_w = 400
        self.screen_h = 800

        # размеры труб
        self.pipe_w = 80
        self.pipe_h = 500

        self.pipe_gap = 180  # расстояние между трубами

        # размер земли
        self.ground_w = 2 * self.screen_w
        self.ground_h = 100

        self.speed = 10  # скорость птички
        self.gravity = 1  # гравитация

        # задаём окно и название
        self.screen = pg.display.set_mode((self.screen_w, self.screen_h))
        pg.display.set_caption('Flappy Bird')

        # грузим задний фон и подгоняем под размеры окна
        self.bg_image = pg.transform.scale(pg.image.load('bg.png'),
                                           (self.screen_w, self.screen_h))

        self.clock = pg.time.Clock()  # часы для FPS
        self.points = 0  # Количество очков

        # шрифт для рендеринга
        self.font = pg.font.Font(pg.font.get_default_font(), 30)

        # создаём группу спрайтов и заполняем группу 2-мя спрайтами земли.
        self.ground_group = pg.sprite.Group()
        self.ground_group.add(Ground(self, self.ground_w))
        self.ground_group.add(Ground(self, self.ground_w * 2))

        # создаём группу спрайтов птицы и заполняем
        self.bird_group = pg.sprite.Group()
        self.bird = Bird(self)
        self.bird_group.add(self.bird)

        self.pipe_group = pg.sprite.Group()
        for i in range(2):
            pipes = self.get_random_pipes(self.screen_w * i + 800)
            self.pipe_group.add(pipes[0])
            self.pipe_group.add(pipes[1])

    def get_random_pipes(self, xpos):
        size = randint(100, 500)

        pipe = Pipe(self, False, xpos, size)
        pipe_inverted = Pipe(self, True, xpos, self.screen_h - size - self.pipe_gap)
        return pipe, pipe_inverted

    @staticmethod
    def is_off_screen(sprite) -> bool:
        return sprite.rect.right < 0

    def check_events(self) -> bool:
        # закрытие окна
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False

            # нажатие на пробел
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.bird.jump()  # здесь
        return True

    def draw(self) -> None:
        self.screen.blit(self.bg_image, (0, 0))

        if self.is_off_screen(self.ground_group.sprites()[0]):
            self.ground_group.remove(self.ground_group.sprites()[0])
            new_ground = Ground(self, self.ground_w - 20)
            self.ground_group.add(new_ground)

        # если трубы ушли за левую стенку
        if self.is_off_screen(self.pipe_group.sprites()[0]):
            # удаляем старые трубы
            self.pipe_group.remove(self.pipe_group.sprites()[0])
            self.pipe_group.remove(self.pipe_group.sprites()[0])

            # создаём новые трубы
            pipes = self.get_random_pipes(self.screen_w * 2)

            # добавляем новые трубы в группу спрайтов
            self.pipe_group.add(pipes[0])
            self.pipe_group.add(pipes[1])
            # увеличиваем количество очков
            self.points += 1

        self.ground_group.draw(self.screen)
        self.pipe_group.draw(self.screen)  # здесь
        self.bird_group.draw(self.screen)

        points_text = self.font.render(f"Points: {self.points}",
                                       True,
                                       pg.Color('black'))
        self.screen.blit(points_text, points_text.get_rect(x=20, y=20))

    def update(self) -> None:
        self.clock.tick(30)
        self.bird_group.update()
        self.ground_group.update()
        self.pipe_group.update()  # здесь
        pg.display.flip()

    def check_game_over(self):
        # если группа спрайтов птички касается группы земли
        if (pg.sprite.groupcollide(self.bird_group,
                                   self.ground_group,
                                   False,
                                   False, pg.sprite.collide_mask) or
        # или группа птички касается группы труб
                pg.sprite.groupcollide(self.bird_group,
                                       self.pipe_group,
                                       False,
                                       False, pg.sprite.collide_mask)):

            # то создаём текст с хитбоксом по середине экрана, выводим его и ждём 3 секунды
            # потом приложение закрывается и в консоль пишется Game Over
            text = self.font.render(f'Game Over! Record: {self.points}', True, pg.Color('red'))
            self.screen.blit(text, text.get_rect(center=(self.screen_w // 2, self.screen_h // 2)))
            pg.display.flip()
            sleep(3)
            pg.quit()
            exit('Game Over')

    def run(self) -> None:
        while self.check_events():
            self.check_game_over() # Вызываем здесь
            self.draw()
            self.update()
        pg.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
