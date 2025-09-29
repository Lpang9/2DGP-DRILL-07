from pico2d import *
import random

class Grass:
    # 생성자함수 초기화 수행
    def __init__(self):
        # grass 객체의 속성을 정의하고 초기화
        self.image = load_image('grass.png')
    pass

    def draw(self):
        self.image.draw(400, 30)
        pass

    def update(self):
        # 비워놓더라도 함수 제작!
        pass

class Zombie:
    def __init__(self):
        self.x, self.y = 100, 170
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x +=5

    def draw(self):
        frame_width = self.image.w //10
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width, 0, frame_width, frame_height,
                             self.x, self.y, frame_width // 2, frame_height // 2)


# class Grass:
#     pass   -> 기본 정의

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()


class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, 90)
    pass

    def update(self):
        self.x += 5
        self.frame = (self.frame+1) % 8
        pass


class Ball_1:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(100, 700), 599

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if self.y > 60:
            self.y -= random.randint(5, 50)
            if self.y < 60:
                self.y = 60
    pass


class Ball_2:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(100, 700), 599

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if self.y > 70:
            self.y -= random.randint(5, 50)
            if self.y < 70:
                self.y = 70
    pass


def balls():
    if random.randint(0, 1) == 0:
        return Ball_1()
    else:
        return Ball_2()
    pass


def reset_world():
    global running
    global world
    # world list : 몸든 객체들을 갖고있는 리스트

    running = True
    world = []
    # 객체가 하나도 없는 월드

    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(11)]
    world += team

    team_ball = [balls() for i in range(20)]
    world += team_ball


    pass

# 게임 로직
def update_world():
    for game_object in world:
        game_object.update()
    pass

def render_world():
    # 월드에 객체들을 그린다.
    clear_canvas()

    for game_object in world:
        game_object.draw()


    update_canvas()
    pass


reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)


close_canvas()