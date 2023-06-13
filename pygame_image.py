import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)
    KK_img = pg.image.load("ex01/fig/3.png")
    KK_img2 = pg.transform.flip(KK_img,True,False)
    KK_img3 = pg.transform.rotozoom(KK_img2, 10, 1.0)
    KK_imgs = [KK_img2,KK_img3]
    tmr = 0
    x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-x,0])
        screen.blit(bg_img2, [1600-x,0])
        screen.blit(bg_img,[3200-x,0])
        screen.blit(KK_imgs[tmr//100%2],[300,200])
        pg.display.update()
        tmr += 1  
        x += 1
        clock.tick(100)
        if x > 1599:
            x = 0

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()