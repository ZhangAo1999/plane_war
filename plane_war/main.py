from pygame.locals import *
from plane import *


def key_down(hero_plane):
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
        hero_plane.move_left()
    if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
        hero_plane.move_right()
    if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
        hero_plane.move_up()
    if key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
        hero_plane.move_down()
    if key_pressed[pygame.K_SPACE]:
        hero_plane.launch_bullet()


def wenzi(screen, string, time=50):
    font = pygame.font.Font("./ziti/zi_ti.ttf", 20)
    x = 30
    y = 500
    for i in str(string):
        font_fmt = font.render(i, 1, (0, 0, 0), (255, 255, 255))
        screen.blit(font_fmt, (x, y))
        x += 25
        if x > 370:
            y += 40
            x = 30
        pygame.display.update()
        pygame.time.delay(time)


def juqing1(screen, background):
    i = 0
    words = ["天亮了。。。", "要出去狩猎了啊？", "咦？", "你是被他们，那群村民找来送死的吗？", "你这样的冒险者我见多了，不过他们都死了。我送你去陪他们吧！"]
    need_view = [True, True, True, True, True]
    while True:
        screen.blit(background, (0, 0))
        lihui_enymy_path = "./feiji/enemy_3D.gif"
        lihui_enymy = pygame.image.load(lihui_enymy_path).convert()
        borad_path = "./feiji/white.png"
        borad = pygame.image.load(borad_path).convert()
        # 在第几行输出相应文字。
        screen.blit(lihui_enymy, (10, 340))
        screen.blit(borad, (10, 480))
        if need_view[i]:
            wenzi(screen, words[i])
            need_view[i] = False
        else:
            wenzi(screen, words[i], 0)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                i = i + 1
            elif event.type == QUIT:
                print("exit")
                exit()
        if i > 4:
            break
        pygame.time.delay(200)
        pygame.display.update()


def juqing2(screen, background, hero_plane):
    background_error_path = "./feiji/background_error.png"
    background_error = pygame.image.load(background_error_path).convert()
    image_name = "./feiji/hero.gif"
    hero_plane_image = pygame.image.load(image_name).convert()
    shock_path = "./feiji/shock.gif"
    shock = pygame.image.load(shock_path).convert()
    screen.blit(background_error, (0, 0))
    screen.blit(hero_plane_image, (hero_plane.x, hero_plane.y))
    screen.blit(shock, (hero_plane.x + 60, hero_plane.y - 40))
    pygame.display.update()
    pygame.time.delay(2000)
    while True:
        flag = False
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                flag = True
            elif event.type == QUIT:
                print("exit")
                exit()
        if flag:
            break
        pygame.time.delay(200)
    i = 0
    words = ["今天的黑夜，来得格外的早啊。。。", "是你灭掉了那个种族吗？", "这样这个世界就会一直被黑夜笼罩了啊，你连这个都不懂吗？！", "空有这么强大的力量，不知道要保持生态的平衡吗？", "那就感受绝望吧！！"]
    need_view = [True, True, True, True, True]
    while True:
        screen.blit(background, (0, 0))
        lihui_enymy_path = "./feiji/enemy1_3D.gif"
        lihui_enymy = pygame.image.load(lihui_enymy_path).convert()
        borad_path = "./feiji/white.png"
        borad = pygame.image.load(borad_path).convert()
        # 在第几行输出相应文字。
        screen.blit(lihui_enymy, (10, 340))
        screen.blit(borad, (10, 480))
        if need_view[i]:
            wenzi(screen, words[i])
            need_view[i] = False
        else:
            wenzi(screen, words[i], 0)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                i = i + 1
            elif event.type == QUIT:
                print("exit")
                exit()
        if i > 4:
            break
        pygame.time.delay(200)
        pygame.display.update()


def start():
    pygame.init()
    fen_l = []
    fen_list = []
    screen = pygame.display.set_mode((400, 700), 0, 32)
    for i in range(10):
        fen_l.append("./feiji/score"+str(i)+".gif")
        fen_list.append(pygame.image.load(fen_l[i]).convert())
    fen_list.append(pygame.image.load("./feiji/add.gif").convert())
    image_file_path = './feiji/background.png'
    image_file_path1 = './feiji/background_night.png'
    image_file_path2 = './feiji/background_beach.png'
    image_file_path3 = './feiji/game_over.gif'
    image_file_path4 = './feiji/start.gif'
    background = pygame.image.load(image_file_path).convert()
    background_night = pygame.image.load(image_file_path1).convert()
    background_beach = pygame.image.load(image_file_path2).convert()
    game_over = pygame.image.load(image_file_path3).convert()
    sta = pygame.image.load(image_file_path4).convert()
    hero_plane = HeroPlane(screen)
    enemy_plane_list = []
    fen_dict = [[], [], [], [], [], [], []]
    i = 0
    juqing = [False, False]
    dead = False
    score = 0
    while True:
        screen.blit(background, (0, 0))
        screen.blit(sta, (30, 280))
        pygame.time.delay(200)
        pygame.display.update()
        st = False
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                st = True
            elif event.type == QUIT:
                print("exit")
                exit()
        if st:
            break
    while True:
        bad_bullet_list = []
        if dead:
            screen.blit(background_beach, (0, 0))
            screen.blit(game_over, (30, 340))
            fenshu = pygame.font.Font("./ziti/zi_ti.ttf", 36)
            fenshu = fenshu.render("分数：" + str(score), 1, (0, 0, 0))
            screen.blit(fenshu, (60, 280))
            for event in pygame.event.get():
                # 重开
                if event.type == KEYDOWN:
                    score = 0
                    hero_plane = HeroPlane(screen)
                    enemy_plane_list = []
                    i = 0
                    dead = False
                elif event.type == QUIT:
                    print("exit")
                    exit()
            pygame.display.update()
            pygame.time.delay(200)
            continue
        i += 1
        if i % 43 == 1:
            enemy_plane = EnemyPlane(screen)
            enemy_plane_list.append(enemy_plane)
        if score < 1000000:
            if not juqing[0]:
                juqing1(screen, background)
                juqing[0] = True
            screen.blit(background, (0, 0))
            for enemy_plane in enemy_plane_list:
                enemy_plane.display()
                bad_bullet_list.extend(enemy_plane.bullet_list)
        else:
            if not juqing[1]:
                juqing2(screen, background_night, hero_plane)
                juqing[1] = True
            screen.blit(background_night, (0, 0))
            for enemy_plane in enemy_plane_list:
                enemy_plane.display1()
                bad_bullet_list.extend(enemy_plane.bullet_list)
        dead_enemy_list = []
        for enemy_plane in enemy_plane_list:
            del_bullet_list = []
            for hero_bullet in hero_plane.bullet_list:
                win = enemy_plane.is_hurt(hero_bullet)
                if win[0] == 0:
                    continue
                if win[0] == 1:
                    del_bullet_list.append(win[1][1])
                    if win[1][0] not in dead_enemy_list:
                        dead_enemy_list.append(win[1][0])
                    score += win[2]
                    fen_dict[6].append((win[2], win[1][0].x, win[1][0].y))
                if win[0] == 2:
                    del_bullet_list.append(win[1])
            for del_bullet in del_bullet_list:
                hero_plane.bullet_list.remove(del_bullet)
        for j in fen_dict[0]:
            screen.blit(fen_list[10], (j[1], j[2] - 1))
            x = 30
            for fen in str(j[0]):
                screen.blit(fen_list[int(fen)], (j[1] + x, j[2] - 1))
                x += 18
        fen_dict[0] = []
        for k in range(1, 7):
            for j in fen_dict[k]:
                screen.blit(fen_list[10], (j[1], j[2] + 20 - (7-k) * 3))
                x = 30
                for fen in str(j[0]):
                    screen.blit(fen_list[int(fen)], (j[1] + x, j[2] + 20 - (7-k) * 3))
                    x += 18
                fen_dict[k-1].append(j)
            fen_dict[k] = []
        for dead_enemy in dead_enemy_list:
            enemy_plane_list.remove(dead_enemy)
        for enemy_plane in enemy_plane_list:
            enemy_plane.launch_bullet()
            enemy_plane.move()
        hero_hurt = hero_plane.is_hurt(bad_bullet_list)
        if hero_hurt:
            if hero_hurt == "game over":
                dead = True
            else:
                for enemy_plane in enemy_plane_list:
                    if hero_hurt in enemy_plane.bullet_list:
                        enemy_plane.bullet_list.remove(hero_hurt)
        hero_plane.display()
        x = 0
        for fen in str(score):
            screen.blit(fen_list[int(fen)], (x, 0))
            x += 18
        key_down(hero_plane)
        pygame.time.delay(50)
        pygame.display.update()


start()


