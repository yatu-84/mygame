import pygame  # pygameライブラリを取り込む
from pygame.locals import *  # pygameで使う定数を全て取り込む
import sys  # sys標準ライブラリを取り込む
from random import randint

pygame.init()  # pygameの初期化
#背景
screen = pygame.display.set_mode((1200, 675))
b = pygame.image.load("./images/b.png").convert_alpha()
b1 = pygame.image.load("./images/b1.png").convert_alpha()
b2 = pygame.image.load("./images/b2.png").convert_alpha()
b3 = pygame.image.load("./images/b3.png").convert_alpha()

#変数
hitstop=0
frame=0
p2AtFrame=0
p1AtFrame=0
p1x=-200
p2x=+200
camera=-(p1x+p2x)/2
up=0
right=0
left=0
w=0
a=0
d=0
v=0.5#基の速さ
off=7#攻め
dif=10#守り
at1=0#0:たち,1:接近,2:発生,3:成功,4:失敗
at2=0
chance1=3
chance2=3




#画像読み込み
p1wait0 = pygame.image.load("./images/wait-0.png").convert_alpha()
p1wait0 = pygame.transform.scale(p1wait0, (600*1.25, 675*1.25))
p1wait1= pygame.image.load("./images/wait-1.png").convert_alpha()
p1wait1 = pygame.transform.scale(p1wait1, (600*1.25, 675*1.25))
p1walk0 = pygame.image.load("./images/walk-0.png").convert_alpha()
p1walk0 = pygame.transform.scale(p1walk0, (600*1.25, 675*1.25))
p1walk1 = pygame.image.load("./images/walk-1.png").convert_alpha()
p1walk1 = pygame.transform.scale(p1walk1, (600*1.25, 675*1.25))
p1walk2 = pygame.image.load("./images/walk-2.png").convert_alpha()
p1walk2 = pygame.transform.scale(p1walk2, (600*1.25, 675*1.25))
p1walk3 = pygame.image.load("./images/walk-3.png").convert_alpha()
p1walk3 = pygame.transform.scale(p1walk3, (600*1.25, 675*1.25))
p1attack0 = pygame.image.load("./images/attack-0.png").convert_alpha()
p1attack0 = pygame.transform.scale(p1attack0, (600*1.25, 675*1.25))
p1attack1 = pygame.image.load("./images/attack-1.png").convert_alpha()
p1attack1 = pygame.transform.scale(p1attack1, (600*1.25, 675*1.25))
p1attack2 = pygame.image.load("./images/attack-2.png").convert_alpha()
p1attack2 = pygame.transform.scale(p1attack2, (600*1.25, 675*1.25))
p1attack3 = pygame.image.load("./images/attack-3.png").convert_alpha()
p1attack3 = pygame.transform.scale(p1attack3, (600*1.25, 675*1.25))
p1attack4 = pygame.image.load("./images/attack-4.png").convert_alpha()
p1attack4 = pygame.transform.scale(p1attack4, (600*1.25, 675*1.25))
p1gard = pygame.image.load("./images/gard.png").convert_alpha()
p1gard = pygame.transform.scale(p1gard, (600*1.25, 675*1.25))
p1hit = pygame.image.load("./images/hit.png").convert_alpha()
p1hit = pygame.transform.scale(p1hit, (600*1.25, 675*1.25))
p2wait0 = pygame.image.load("./images/2wait-0.png").convert_alpha()
p2wait0 = pygame.transform.scale(p2wait0, (600*1.25, 675*1.25))
p2wait1= pygame.image.load("./images/2wait-1.png").convert_alpha()
p2wait1 = pygame.transform.scale(p2wait1, (600*1.25, 675*1.25))
p2walk0 = pygame.image.load("./images/2walk-0.png").convert_alpha()
p2walk0 = pygame.transform.scale(p2walk0, (600*1.25, 675*1.25))
p2walk1 = pygame.image.load("./images/2walk-1.png").convert_alpha()
p2walk1 = pygame.transform.scale(p2walk1, (600*1.25, 675*1.25))
p2walk2 = pygame.image.load("./images/2walk-2.png").convert_alpha()
p2walk2 = pygame.transform.scale(p2walk2, (600*1.25, 675*1.25))
p2walk3 = pygame.image.load("./images/2walk-3.png").convert_alpha()
p2walk3 = pygame.transform.scale(p2walk3, (600*1.25, 675*1.25))
p2attack0 = pygame.image.load("./images/2attack-0.png").convert_alpha()
p2attack0 = pygame.transform.scale(p2attack0, (600*1.25, 675*1.25))
p2attack1 = pygame.image.load("./images/2attack-1.png").convert_alpha()
p2attack1 = pygame.transform.scale(p2attack1, (600*1.25, 675*1.25))
p2attack2 = pygame.image.load("./images/2attack-2.png").convert_alpha()
p2attack2 = pygame.transform.scale(p2attack2, (600*1.25, 675*1.25))
p2attack3 = pygame.image.load("./images/2attack-3.png").convert_alpha()
p2attack3 = pygame.transform.scale(p2attack3, (600*1.25, 675*1.25))
p2attack4 = pygame.image.load("./images/2attack-4.png").convert_alpha()
p2attack4 = pygame.transform.scale(p2attack4, (600*1.25, 675*1.25))
p2gard = pygame.image.load("./images/2gard.png").convert_alpha()
p2gard = pygame.transform.scale(p2gard, (600*1.25, 675*1.25))
p2hit = pygame.image.load("./images/2hit.png").convert_alpha()
p2hit = pygame.transform.scale(p2hit, (600*1.25, 675*1.25))
font = pygame.font.Font(None, 55)
win1 = pygame.image.load("./images/win1.png").convert_alpha()
win1 = pygame.transform.scale(win1, (600*1.25, 675*1.25))
win2 = pygame.image.load("./images/win2.png").convert_alpha()
win2 = pygame.transform.scale(win2, (600*1.25, 675*1.25))


#オブジェクト


clock = pygame.time.Clock()

while(True):
    clock.tick(60)
    if  0<=frame & frame<59:
        frame=frame+1
    else:
        frame=0
    camera=-(p1x+p2x)/2

    #表示
    screen.blit(b1, [camera/10-600, 0])
    screen.blit(b2, [camera/4-600, 0])
    screen.blit(b3, [camera/1.5-600, 0])
    screen.blit(b, [camera-600, 0])
    #screen.blit(p1, [p1x+camera+225, 50])
    #screen.blit(p2, [p2x+camera+225, 50])
    #プレイヤー1
    if (at2==0) or (at2==1):
        if w==0:
            if  0<=frame & frame<15:
                if a==1:
                    screen.blit(p1walk3, [p1x+camera+225, 50])
                elif d==1:
                    screen.blit(p1walk0, [p1x+camera+225, 50])
                else:
                    screen.blit(p1wait0, [p1x+camera+225, 50])

            if 15<=frame & frame<30:
                if a==1:
                    screen.blit(p1walk2, [p1x+camera+225, 50])
                elif d==1:
                    screen.blit(p1walk1, [p1x+camera+225, 50])
                else:
                    screen.blit(p1wait0, [p1x+camera+225, 50])

            if 30<=frame & frame<45:
                if a==1:
                    screen.blit(p1walk1, [p1x+camera+225, 50])
                elif d==1:
                    screen.blit(p1walk2, [p1x+camera+225, 50])
                else:
                    screen.blit(p1wait1, [p1x+camera+225, 50])

            if 45<=frame & frame<60:
                if a==1:
                    screen.blit(p1walk0, [p1x+camera+225, 50])
                elif d==1:
                    screen.blit(p1walk3, [p1x+camera+225, 50])
                else:
                    screen.blit(p1wait1, [p1x+camera+225, 50])
            #座標
            p1v=0
            if (a==1)&(p2x<p1x+1200):
                p1v=-dif*v+p1v*(1-v)
                p1x=p1x+p1v
            if (d==1)&(p2x>p1x+250):
                p1v=off*v+p1v*(1-v)
                p1x=p1x+p1v
        #攻撃
        if w==1:
            if (p1x<=p2x-250)&(at1==0):
                p1AtFrame=0
                screen.blit(p1attack0, [p1x+camera+225, 50])
                p1x=p1x+25
            elif p1AtFrame<5:
                if at1==0:
                    at1=1
                p1AtFrame=p1AtFrame+1
                screen.blit(p1attack1, [p1x+camera+225, 50])
            elif p1AtFrame<20+hitstop:
                if at1==1:
                    at1=2
                if at1==3:
                    hitstop=75
                p1AtFrame=p1AtFrame+1
                screen.blit(p1attack2, [p1x+camera+225, 50])
            elif p1AtFrame<25+hitstop:
                p1AtFrame=p1AtFrame+1
                screen.blit(p1attack3, [p1x+camera+225, 50])
            elif p1AtFrame<30+hitstop:
                p1AtFrame=p1AtFrame+1
                screen.blit(p1attack3, [p1x+camera+225, 50])
            elif p1AtFrame<35+hitstop:
                p1AtFrame=p1AtFrame+1
                screen.blit(p1attack4, [p1x+camera+225, 50])
            else:
                w=0
                p1AtFrame=0
                if at1==4:
                    at1=0
                    chance1=chance1-1

    if at1==2:
        if (right==1):
            at1=4
        elif (at2==1)|(at2==2):
            at1=0
            at2=0
        else:
            at1=3

    if at2==4:
        screen.blit(p1gard, [p1x+camera+225, 50])
        p1x=p1x-2

    if (p1x<-1200)|((chance1<=0)&(p2x<1200)):
        at2=3
    #プレイヤー2

    if (at1==0) or (at1==1):
        if up==0:
            if  0<=frame & frame<15:
                if right==1:
                    screen.blit(p2walk0, [p2x+camera+225, 50])
                elif left==1:
                    screen.blit(p2walk3, [p2x+camera+225, 50])
                else:
                    screen.blit(p2wait0, [p2x+camera+225, 50])

            if 15<=frame & frame<30:
                if right==1:
                    screen.blit(p2walk1, [p2x+camera+225, 50])
                elif left==1:
                    screen.blit(p2walk2, [p2x+camera+225, 50])
                else:
                    screen.blit(p2wait0, [p2x+camera+225, 50])

            if 30<=frame & frame<45:
                if right==1:
                    screen.blit(p2walk2, [p2x+camera+225, 50])
                elif left==1:
                    screen.blit(p2walk1, [p2x+camera+225, 50])
                else:
                    screen.blit(p2wait1, [p2x+camera+225, 50])

            if 45<=frame & frame<60:
                if right==1:
                    screen.blit(p2walk3, [p2x+camera+225, 50])
                elif left==1:
                    screen.blit(p2walk0, [p2x+camera+225, 50])
                else:
                    screen.blit(p2wait1, [p2x+camera+225, 50])
            #座標
            p2v=0
            if (right==1)&(p2x<p1x+1200):
                p2v=dif*v+p2v*(1-v)
                p2x=p2x+p2v
            if (left==1)&(p2x>p1x+250):
                p2v=-off*v+p2v*(1-v)
                p2x=p2x+p2v
        #攻撃
        if up==1:
            if (p1x<=p2x-250)&(at2==0):
                p2AtFrame=0
                screen.blit(p2attack0, [p2x+camera+225, 50])
                p2x=p2x-25
            elif p2AtFrame<5:
                if at2==0:
                    at2=1
                p2AtFrame=p2AtFrame+1
                screen.blit(p2attack1, [p2x+camera+225, 50])
            elif p2AtFrame<20+hitstop:
                if at2==1:
                    at2=2
                if at2==3:
                    hitstop=75
                p2AtFrame=p2AtFrame+1
                screen.blit(p2attack2, [p2x+camera+225, 50])
            elif p2AtFrame<25+hitstop:
                p2AtFrame=p2AtFrame+1
                screen.blit(p2attack3, [p2x+camera+225, 50])
            elif p2AtFrame<30+hitstop:
                p2AtFrame=p2AtFrame+1
                screen.blit(p2attack3, [p2x+camera+225, 50])
            elif p2AtFrame<35+hitstop:
                p2AtFrame=p2AtFrame+1
                screen.blit(p2attack4, [p2x+camera+225, 50])
            else:
                up=0
                p2AtFrame=0
                if at2==4:
                    chance2=chance2-1
                    at2=0

        if at2==2:
            if (a ==1):
                at2=4
            elif (at1==1) | (at1==2):
                at1=0
                at2=0
            else:
                at2=3

    if at1==4:
        screen.blit(p2gard, [p2x+camera+225, 50])
        p2x=p2x+2
    if at1==3:
        p2AtFrame=p2AtFrame+1
        if p2AtFrame<30/2:
            screen.blit(p2hit, [p2x+camera+225, 50])
        elif p2AtFrame<60/2:
            p2AtFrame=p2AtFrame
        elif p2AtFrame<90/2:
            screen.blit(p2hit, [p2x+camera+225, 50])
        elif p2AtFrame<120/2:
            p2AtFrame=p2AtFrame
        elif p2AtFrame<150/2:
            screen.blit(p2hit, [p2x+camera+225, 50])
        else:
            screen.blit(win1, [180, -50])
    if (p2x>1200)|((chance2<=0)&(p1x>-1200)):
        at1=3

    if at2==3:
        p1AtFrame=p1AtFrame+1
        if p1AtFrame<30/2:
            screen.blit(p1hit, [p1x+camera+225, 50])
        elif p1AtFrame<60/2:
            p2AtFrame=p2AtFrame
        elif p1AtFrame<90/2:
            screen.blit(p1hit, [p1x+camera+225, 50])
        elif p1AtFrame<120/2:
            p2AtFrame=p2AtFrame
        elif p1AtFrame<150/2:
            screen.blit(p1hit, [p1x+camera+225, 50])
        else:
            screen.blit(win2, [200, -50])

    #text = font.render("Gorilla!", True, (255,255,255))
    #screen.blit(text, [20, 20])
    pygame.display.update()  # 画面の更新
    print('up',up,'right',right,'left',left,'w',w,'d',d,'a',a,'at1',at1,'at2',at2)


    #操作
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if (up==0)&(at2!=3)&(at1!=3):
                if at1!=3:
                    if event.key == K_UP:
                        up=1
                        right=0
                        left=0
                    if event.key == K_LEFT:
                        right=0
                        left=1
                    if (event.key == K_RIGHT):
                        right=1
                        left=0
            if (w==0)&(at2!=3)&(at1!=3):
                if at2!=3:
                    if event.key == K_w:
                        w=1
                        d=0
                        a=0
                    if event.key == K_d:
                        d=1
                        a=0
                    if event.key == K_a:
                        d=0
                        a=1
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    if event.type == KEYUP:
        if event.key == K_LEFT:
            left=0
        if event.key == K_RIGHT:
            right=0
        if event.key == K_d:
            d=0
        if event.key == K_a:
            a=0
