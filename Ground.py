import pygame as pg
class Ground(pg.sprite.Sprite):
    def __init__(self, root, x_pos: int) -> None:
        # инициализируем Sprite
        super().__init__()
        self.game = root  # поле игры

        # грузим и растягиваем изображение
        self.image = pg.transform.scale(pg.image.load('base.png'),
                                        (self.game.ground_w, self.game.ground_h))
        # конвертируем изображение
        self.image = self.image.convert_alpha()

        # создаём маску по картинке
        self.mask = pg.mask.from_surface(self.image)

        # создаём хитбокс, который расположем в точке x_pos и по y внизу экрана
        self.rect = self.image.get_rect(x=x_pos,
                                        y=self.game.screen_h - self.game.ground_h)

    def update(self) -> None:
        self.rect.x -= self.game.speed
