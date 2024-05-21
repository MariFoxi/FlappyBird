import pygame as pg
class Bird(pg.sprite.Sprite):
    def __init__(self, root) -> None:
        # наследуем спрайты
        super().__init__()

        self.game = root  # поле игры

        # кортеж всех картинок птички
        # в них отличается взмах крыла
        self.images = (
            pg.image.load('bird-up.png').convert_alpha(),
            pg.image.load('bird-middle.png').convert_alpha(),
            pg.image.load('bird-down.png').convert_alpha()
        )

        # текущая скорость птички (делаем копию)
        self.speed = self.game.speed

        self.current_image = 0 # номер текущей фотки
        self.image = self.images[0]  # получаем изначально 1 фотку как спрайт
        self.mask = pg.mask.from_surface(self.image)  # создаём маску

        # создаём хитбокс слева экрана по середине высоты
        self.rect = self.image.get_rect(x=50, y=self.game.screen_h // 2)

    def update(self) -> None:
        # получаем текущую картинку и запоминаем её
        # % 3 чтобы не выйти за границы кортежа
        self.current_image = (self.current_image + 1) % 3

        # получаем текущий спрайт и поворачиваем его в зависимости от скорости птицы
        self.image = pg.transform.rotate(self.images[self.current_image], -self.speed * 2)
        # прибавляем гравитацию
        self.speed += self.game.gravity
        # применяем скорость к хитбоксу
        self.rect.y += self.speed

    def jump(self) -> None:
        # при прыжке меняем скорость на обратную
        # чтобы взлететь
        self.speed = -self.game.speed
