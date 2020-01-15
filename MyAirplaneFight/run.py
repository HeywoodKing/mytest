# -*- coding: utf-8 -*-


import pygame
# import time
import random
from pygame.locals import *


running = True


# 背景图片
class Background(object):
    def __init__(self, window):
        # 设置要显示内容的窗口
        self.window = window

        # 背景图片名
        self.image_name = './images/background.png'

        # 根据名字生成背景图片
        self.image = pygame.image.load(self.image_name).convert()

    def display(self):
        self.window.blit(self.image, (0, 0))


# 背景音乐
class BackgroundMusic(object):
    def __init__(self):
        pass

    def play(self):
        pygame.mixer.init()
        pygame.mixer.music.load('./music/m1.mp3')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def stop(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(1)
        else:
            pygame.mixer.music.stop()


class Plane(object):
    def __init__(self, x, y, window, image_name):
        self.x = x
        self.y = y
        # 设置要显示内容的窗口
        self.window = window
        self.image = pygame.image.load(image_name).convert()

        # 用来存储飞机发射的所有子弹
        self.bullet_list = []

    def display(self):
        self.window.blit(self.image, (self.x, self.y))

        for i in self.bullet_list:
            if i.judge():
                self.bullet_list.remove(i)

        for bullet in self.bullet_list:
            # 显示一个子弹的位置
            bullet.display()
            # 让这个子弹进行移动，下次再显示的时候就会看到子弹在修改后的位置
            bullet.move()

    def shoot(self):
        pass


# 英雄飞机
class HeroPlane(Plane):
    def __init__(self, window):
        # 设置飞机默认的位置
        self.w, self.h = window.get_size()
        self.x = self.w / 2 - 20
        self.y = self.h - 80

        super(HeroPlane, self).__init__(self.x, self.y, window, './images/hero1.png')

    def move_left(self):
        self.x -= 10
        if self.x <= 0:
            self.x = 0

    def move_right(self):
        self.x += 10
        if self.x >= self.w - 60:
            self.x = self.w - 60

    def move_up(self):
        self.y -= 10
        if self.y <= 0:
            self.y = 0

    def move_down(self):
        self.y += 10
        if self.y >= self.h - 50:
            self.y = self.h - 50

    def shoot(self):
        # new_bullet = Bullet(self.x, self.y, self.window, 'hero')
        new_bullet = HeroBullet(self.x, self.y, self.window, './images/bullet.png')
        self.bullet_list.append(new_bullet)


# 敌人飞机
class EnemyPlane(Plane):
    def __init__(self, window):
        self.w, self.h = window.get_size()
        self.x = 0
        self.y = 0

        super(EnemyPlane, self).__init__(self.x, self.y, window, './images/enemy1.png')

        self.direction = 'right'

    def move(self):
        # 如果碰到了右边的边界，那么就往左走，如果碰到了左边的边界，那么就往右走
        if self.direction == 'right':
            self.x += 4
        elif self.direction == 'left':
            self.x -= 4

        if self.x > self.w - 50:
            self.direction = 'left'
        elif self.x < 10:
            self.direction = 'right'

    def shoot(self):
        num = random.randint(1, 100)
        if num == 88:
            # new_bullet = Bullet(self.x, self.y, self.window, 'enemy')
            new_bullet = EnemyBullet(self.x, self.y, self.window, './images/bullet.png')
            self.bullet_list.append(new_bullet)


# 子弹类
class Bullet(object):
    def __init__(self, x, y, x_speed, y_speed, window, image_name):
        # self.name = image_name
        self.window = window

        self.x = x + x_speed
        self.y = y + y_speed

        if not image_name:
            image_name = './images/bullet.png'

        self.image = pygame.image.load(image_name).convert()

    def move(self, direction):
        if direction == 'up':
            self.y -= 5
        elif direction == 'down':
            self.y += 5

    def display(self):
        self.window.blit(self.image, (self.x, self.y))

    def judge(self):
        if self.y < 0 or self.y > 667:
            return True
        else:
            return False


# 英雄飞机子弹
class HeroBullet(Bullet):
    def __init__(self, x, y, window, image_name):
        # self.image_name = image_name
        super(HeroBullet, self).__init__(x, y, 20, -10, window, image_name)

    def move(self, direction='up'):
        # Bullet.move(self)
        super(HeroBullet, self).move(direction)
        self.y -= 5

        # 碰撞检测，碰撞之后敌机爆炸消失


# 敌人飞机子弹
class EnemyBullet(Bullet):
    def __init__(self, x, y, window, image_name):
        # self.image_name = image_name
        super(EnemyBullet, self).__init__(x, y, 30, 30, window, image_name)

    def move(self, direction='down'):
        # Bullet.move(self)
        super(EnemyBullet, self).move(direction)
        self.y += 4

        # 碰撞检测，碰撞之后英雄飞机爆炸消失，然后出现下一个英雄飞机


def key_control(hero_plane):
    pygame.key.set_repeat(0, 1)
    # 获取事件，比如按键等
    for event in pygame.event.get():
        # 判断是否是点击了退出按钮
        # print(event.type)
        if event.type == QUIT:
            print('exit')
            global running
            running = False
            exit()
        # 判断是否是按下了键
        elif event.type == KEYDOWN:
            # key_pressed = pygame.key.get_pressed()
            # if key_pressed[K_a] or key_pressed[K_LEFT]:
            #     print('left')
            #     # 控制飞机让其向左移动
            #     hero_plane.move_left()

            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                # 控制飞机让其向左移动
                hero_plane.move_left()

            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                # 控制飞机让其向右移动
                hero_plane.move_right()

            # 检测按键是否是w或者up
            elif event.key == K_w or event.key == K_UP:
                print('up')
                # 控制飞机让其向前移动
                hero_plane.move_up()

            # 检测按键是否是s或者down
            elif event.key == K_s or event.key == K_DOWN:
                print('down')
                # 控制飞机让其向后移动
                hero_plane.move_down()

            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_plane.shoot()

            elif event.key == K_ESCAPE:
                print('exit')
                running = False
                exit()


def main():
    """
    搭建界面，主要完成窗口和背景图的显示
    """
    pygame.init()
    # 1.创建窗口用来显示内容
    window = pygame.display.set_mode((471, 727), 0, 32)
    pygame.display.set_caption('Airplane Fight v1.0')
    # screen = pygame.display.get_surface()
    # my_font = pygame.font.SysFont("Times New Roman", 25)
    # driver = pygame.display.get_driver()
    # print(window.get_size(), window.get_width(), window.get_height())
    # print(window.get_view())

    # 2.创建一个和窗口大小的图片，用来充当背景
    background = Background(window)

    background_music = BackgroundMusic()
    background_music.play()

    # 3.创建一个玩家飞机的图片
    hero_plane = HeroPlane(window)

    # 4.创建一个敌人飞机
    enemy_plane = EnemyPlane(window)

    # .把背景图片放到窗口中显示
    while running:
        # 设定需要显示的背景图
        background.display()

        # 设定需要显示的飞机图片
        hero_plane.display()

        enemy_plane.move()
        enemy_plane.display()
        enemy_plane.shoot()

        key_control(hero_plane)

        # 更新需要显示的内容
        # pygame.display.update()
        # 刷新当前窗口，渲染窗口，将绘制的图像呈现出来
        pygame.display.flip()

        # 通过延时的方式，来降低这个while循环的循环速度，从而降低了cpu占用率
        # time.sleep(0.01)
        # 每隔50毫秒再刷新窗口
        pygame.time.delay(20)


if __name__ == "__main__":
    main()


"""
1.键盘按下时没有一直起作用，不左右移动，子弹也不连续发射，切换子弹
2.敌方飞机不仅左右移动，加上上下移动
3.打中敌方飞机后爆炸效果
4.打中敌方飞机10架次之后出现一次boss
5.打中boss后进入下一关
6.添加背景音乐
7.增加得分
8.积累能量放大招
9.吃掉系统随机释放的能量，让英雄飞机升级
10.联网对战，排名，
11.增加损伤修复功能，生命值功能
12.空中战机之后出现地面部队
13.更换地图更加有趣
14.增加海战
15.海陆空一体战
16.天体作战部队联网对战
17.星空宇宙混战
18.新秩序诞生
19.
"""
