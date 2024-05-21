import pygame as pg
class Pipe(pg.sprite.Sprite):
    def __init__(self, root, inverted: bool, x_pos: int, y_pos: int) -> None:
        # наследуем спрайты
        super().__init__()
        self.game = root  # поле игры

        # грузим картинку
        self.image = pg.image.load('pipe.png').convert_alpha()

        # подгоняем картинку под размеры трубы
        self.image = pg.transform.scale(self.image,
                                        (self.game.pipe_w, self.game.pipe_h))

        # получаем хитбокс и ставим его на определённую точку x
        self.rect = self.image.get_rect(x=x_pos)

        if inverted:  # если нужна труба перевёрнутая
            # делаем отражение картинки по оси Y
            self.image = pg.transform.flip(self.image, False, True)
            # высчитываем позицию Y инвертированной трубы
            self.rect.y = - (self.rect.height - y_pos)
        else:  # иначе высчитываем позицию Y обычной трубы
            self.rect.y = self.game.screen_h - y_pos

        # создаём маску
        self.mask = pg.mask.from_surface(self.image)

    def update(self) -> None:
        # двигаем трубу налево
        self.rect.x -= self.game.speed
