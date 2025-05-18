import pygame as pg
WIN = pg.display.set_mode((1920,1080))
car1i = pg.image.load('img/car1.png')
car1i = pg.transform.scale(car1i, (50,50))
car2i = pg.image.load('img/car2.png')
car2i = pg.transform.scale(car2i, (50,50))
car3i = pg.image.load('img/car3.png')
car3i = pg.transform.scale(car3i, (50,50))
car4i = pg.image.load('img/car4.png')
car4i = pg.transform.scale(car4i, (50,50))
class Carrot:
    def __init__(self):
        self.planted = 0
        self.x = x_global
        self.y = y_global
        self.count = 0
        self.count = 0
        self.img = car1i

    def update(self):

        if self.count == 120:
            self.img = car2i
        if self.count == 240:
            self.img = car3i
        if self.count == 360 and self.planted:
            self.img = car4i
            self.x -= 5
            self.y -= 5
        if self.planted:
            self.count += 1

            WIN.blit(self.img, (self.x, self.y))

pg.font.init()
WIN = pg.display.set_mode((1920,1080))
pg.display.set_caption("Постапокалиптическая ферма")
clock = pg.time.Clock()
money = 0
carrot = 5
bg = pg.image.load("img/bg.png")
bg = pg.transform.scale(bg,(1920,1080))
spritel = pg.image.load("img/sprite.png")
spritel2 = pg.image.load("img/spritel2.png")
spriter = pg.image.load("img/spriter.png")
spriter2 = pg.image.load("img/spriter2.png")
spritel = pg.transform.scale(spritel, (150,150))
spritel2 = pg.transform.scale(spritel2, (150,150))
spriter = pg.transform.scale(spriter, (150,150))
spriter2 = pg.transform.scale(spriter2, (150,150))
sprite = spritel
rabbit = pg.image.load("img/rabbit.png")
rabbit = pg.transform.scale(rabbit, (100,100))
f1 = pg.font.Font('DreiFraktur.ttf', 36)
text1 = f1.render('Баланс: ' + str(money), 1, (100, 0, 150))
text2 = f1.render('Морковь: '+str(carrot), 1,(100,0,150))
text3 = f1.render('Стань на грядку!', 1,(255,0,0))
sell_count = 0


run = 1
count = 0
need_count = 0
need = 0
car_need = 0
move = 0
animationl_count = 0
animationr_count = 0
direction = 'r'
x_global = 960
y_global = 540
car1 = Carrot()
car2 = Carrot()
car3 = Carrot()
car4 = Carrot()
car5 = Carrot()

while run:
    text1 = f1.render('Баланс: ' + str(money), 1, (100, 0, 150))
    text2 = f1.render('Морковь: '+str(carrot), 1,(100,0,150))
    sell_count += 1

    keys = pg.key.get_pressed()

    if keys[pg.K_w]:
        y_global-= 3
        move = 1
    if keys[pg.K_s]:
        y_global += 3
        move = 1
    if keys[pg.K_a]:
        direction = 'l'
        x_global-= 3
        move = 1
    if keys[pg.K_d]:
        direction = 'r'
        x_global+= 3
        move = 1
    if not (keys[pg.K_w] or keys[pg.K_s] or keys[pg.K_a] or keys[pg.K_d]):
        move = 0
        print('a')

    if direction == 'r':
        if animationr_count == 0:
            sprite = spriter
        elif animationr_count == 5:
            sprite = spriter2
        elif animationr_count == 10:
            animationr_count = -1
        if move:
            animationr_count += 1
        else:
            sprite = spriter
    if direction == 'l':
        if animationl_count == 0:
            sprite = spritel
        elif animationl_count == 5:
            sprite = spritel2
        elif animationl_count == 10:
            animationl_count = -1
        if move:
            animationl_count += 1
        else:
            sprite = spritel

    if keys[pg.K_p] and carrot > 0 and count > 45:
        if x_global > 108 and x_global<573 and y_global >153 and y_global<321:
            if not car1.planted:
                car1.img = car1i
                car1.x = x_global + 40
                car1.y = y_global + 40
                carrot -= 1
                car1.planted = 1
                count = 0
            elif not car2.planted:
                car2.img = car1i
                car2.x = x_global + 40
                car2.y = y_global + 40
                carrot -= 1
                car2.planted = 1
                count = 0
            elif not car3.planted:
                car3.img = car1i
                car3.x = x_global + 40
                car3.y = y_global + 40
                carrot -= 1
                car3.planted = 1
                count = 0
            elif not car4.planted:
                car4.img = car1i
                car4.x = x_global + 40
                car4.y = y_global + 40
                carrot -= 1
                car4.planted = 1
                count = 0
            elif not car5.planted:
                car5.img = car1i
                car5.x = x_global + 40
                car5.y = y_global + 40
                carrot -= 1
                car5.planted = 1
                count = 0
        else:
            need = 1
            print('стань на грядку')

    if keys[pg.K_q]:
        if car1.planted and car1.size == 10:
            car1.planted = 0
            carrot += 1
        if car2.planted and car2.size == 10:
            car2.planted = 0
            carrot += 1
        if car3.planted and car3.size == 10:
            car3.planted = 0
            carrot += 1
        if car4.planted and car4.size == 10:
            car4.planted = 0
            carrot += 1
        if car5.planted and car5.size == 10:
            car5.planted = 0
            carrot += 1


    if keys[pg.K_r] and car1.count >= 360:
        car1.count = 0
        carrot += 3
        car1.planted = 0
        count = 0
    if keys[pg.K_r] and car2.count >= 360:
        carrot += 3
        car2.planted = 0
        car2.count = 0
        count = 0
    if keys[pg.K_r] and car3.count >= 360:
        carrot += 3
        car3.planted = 0
        car3.count = 0
        count = 0
    if keys[pg.K_r] and car4.count >= 360:
        carrot += 3
        car4.planted = 0
        car4.count = 0
        count = 0
    if keys[pg.K_r] and car5.count >= 360:
        carrot += 3
        car5.planted = 0
        car5.count = 0
        count = 0



    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = 0
        

    if keys[pg.K_v] and sell_count > 10 and x_global > 1617 and x_global < 1797 and y_global > 807 and y_global < 924:
        if carrot > 1:
            money += 5
            carrot -= 1
            sell_count = 0



    if need_count == 120:
        need = 0
        need_count = 0
    count+=1
    WIN.blit(bg, (0,0))
    if need:
        need_count += 1
        WIN.blit(text3, (760, 20))
    car1.update()
    car2.update()
    car3.update()
    car4.update()
    car5.update()
    WIN.blit(rabbit, (1700,900))
    WIN.blit(sprite, (x_global,y_global))
    WIN.blit(text1, (10, 900))
    WIN.blit(text2, (10, 950))
    pg.display.flip()
    print(x_global,y_global)




    #1617,807
    #1797,924

pg.quit()
