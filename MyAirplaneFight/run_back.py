# -*- coding: utf-8 -*-


import pygame
import time
import random
from pygame.locals import *


# 背景图片
class Background(object):
    def __init__(self, window):
        # 设置要显示内容的窗口
        self.window = window

        # 背景图片名
        self.image_name = './images/background.jpg'

        # 根据名字生成背景图片
        self.image = pygame.image.load(self.image_name).convert()

    def display(self):
        self.window.blit(self.image, (0, 0))


# 背景音乐
class BackgroundMusic(object):
    def __init__(self):
        pass


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


# 英雄飞机类
class HeroPlane(Plane):
    def __init__(self, window):
        # 设置飞机默认的位置
        self.x = 230
        self.y = 590

        super(HeroPlane, self).__init__(self.x, self.y, window, './images/hero1.png')

        # # 设置要显示内容的窗口
        # self.window = window
        #
        # # 保存英雄飞机需要的图片名字
        # self.image_name = './images/hero1.png'
        #
        # # 根据名字生成飞机图片
        # self.image = pygame.image.load(self.image_name).convert()
        #
        # # 存储英雄飞机发射的所有子弹
        # self.bullet_list = []

    # # 显示飞机和移动的子弹
    # def display(self):
    #     self.window.blit(self.image, (self.x, self.y))
    #
    #     # 判断一下子弹的位置是否越界，如果是，那么就要删除这颗子弹
    #     # 用来存放需要删除的对象引用
    #     # need_del_item_list = []
    #
    #     # 保存需要删除的对象
    #     for i in self.bullet_list:
    #         if i.judge():
    #             # need_del_item_list.append(i)
    #             self.bullet_list.remove(i)
    #
    #     # # 删除self.bulletList中需要删除的对象
    #     # for i in need_del_item_list:
    #     #     self.bullet_list.remove(i)
    #
    #     # 因为needDelItemList也保存了刚刚删除的对象的引用，所以可以删除整个列表，那么
    #     # 整个列表中的引用就不存在了，也可以不调用下面的代码，因为needDelItemList是局部变量
    #     # 当这个方法的调用结束时，这个局部变量也就不存在了
    #     # del needDelItemList
    #
    #     for bullet in self.bullet_list:
    #         # 显示一个子弹的位置
    #         bullet.display()
    #         # 让这个子弹进行移动，下次再显示的时候就会看到子弹在修改后的位置
    #         bullet.move()

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

    def move_up(self):
        self.y -= 10

    def move_down(self):
        self.y += 10

    def she_bullet(self):
        # new_bullet = Bullet(self.x, self.y, self.window, 'hero')
        new_bullet = HeroBullet(self.x, self.y, self.window, './images/bullet.png')
        self.bullet_list.append(new_bullet)


# 敌人飞机
class EnemyPlane(Plane):
    def __init__(self, window):
        self.x = 0
        self.y = 0

        super(EnemyPlane, self).__init__(self.x, self.y, window, './images/enemy1.png')

        self.direction = 'right'

        # # 设置要显示内容的窗口
        # self.window = window
        #
        # self.image_name = './images/enemy1.png'
        # self.image = pygame.image.load(self.image_name).convert()
        #
        # # 存储敌人飞机发射的所有子弹
        # self.bullet_list = []

    # def display(self):
    #     self.window.blit(self.image, (self.x, self.y))
    #     # 判断一下子弹的位置是否越界，如果是，那么就要删除这颗子弹
    #     for i in self.bullet_list:
    #         if i.judge():
    #             self.bullet_list.remove(i)
    #
    #     # 更新及这架飞机发射出的所有子弹的位置
    #     for bullet in self.bullet_list:
    #         bullet.display()
    #         bullet.move()

    def move(self):
        # 如果碰到了右边的边界，那么就往左走，如果碰到了左边的边界，那么就往右走
        if self.direction == 'right':
            self.x += 4
        elif self.direction == 'left':
            self.x -= 4

        if self.x > 500 - 50:
            self.direction = 'left'
        elif self.x < 10:
            self.direction = 'right'

    def the_bullet(self):
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


# 敌人飞机子弹
class EnemyBullet(Bullet):
    def __init__(self, x, y, window, image_name):
        # self.image_name = image_name
        super(EnemyBullet, self).__init__(x, y, 30, 30, window, image_name)

    def move(self, direction='down'):
        # Bullet.move(self)
        super(EnemyBullet, self).move(direction)
        self.y += 4

    # def display(self):
    #     self.window.blit(self.image, (self.x, self.y))
    #
    # def judge(self):
    #     if self.y > 667:
    #         return True
    #     else:
    #         return False


def key_control(hero_plane):
    # 获取事件，比如按键等
    for event in pygame.event.get():
        # 判断是否是点击了退出按钮
        # print(event.type)
        if event.type == QUIT:
            print('exit')
            exit()
        # 判断是否是按下了键
        elif event.type == KEYDOWN:
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
                hero_plane.she_bullet()


def main():
    """
    搭建界面，主要完成窗口和背景图的显示
    """
    # 1.创建窗口用来显示内容
    window = pygame.display.set_mode((500, 667), 0, 32)

    # 2.创建一个和窗口大小的图片，用来充当背景
    background = Background(window)

    # 3.创建一个玩家飞机的图片
    hero_plane = HeroPlane(window)

    # 4.创建一个敌人飞机
    enemy_plane = EnemyPlane(window)

    # .把背景图片放到窗口中显示
    while True:
        # 设定需要显示的背景图
        background.display()

        # 设定需要显示的飞机图片
        hero_plane.display()

        enemy_plane.move()
        enemy_plane.display()
        enemy_plane.the_bullet()

        key_control(hero_plane)

        # 更新需要显示的内容
        pygame.display.update()

        # 通过延时的方式，来降低这个while循环的循环速度，从而降低了cpu占用率
        time.sleep(0.01)


if __name__ == "__main__":
    main()

