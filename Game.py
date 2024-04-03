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
