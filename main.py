import pygame
pygame.init()
player = None
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
tile_width = tile_height = 25
tile_images = {
    'wall': pygame.image.load('box.png'),
    'empty': pygame.image.load('grass.jpg')
}
player_image = pygame.image.load('character.png')
def load_level(filename):
    filename = filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: list(x.ljust(max_width, '.')), level_map))
def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    return new_player, x, y
class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * pos_x+10, tile_height * pos_y+5)
        print(tile_width * pos_x)
        print(tile_height * pos_y)
    def update(self, pos_x, pos_y):
        self.rect = self.image.get_rect().move(tile_width * pos_x+10 , tile_height * pos_y+5)
        print(tile_width * pos_x)
        print(tile_height * pos_y)
player, x, y = generate_level(load_level('map.txt'))
print(x, y)
map = load_level("map.txt")
print(map)
running = True
size = (275, 275)
x-=6
y-=6
screen = pygame.display.set_mode(size)
flag = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                flag = 'UP'
                if y - 1 >=0 and map[x][y - 1] != '#':
                     y = y -1
                     player.update(x, y)
            if event.key == pygame.K_DOWN:
                flag = 'DOWN'
                if y + 1 <= 10 and map[x][y + 1] != '#':
                    y += 1
                    player.update(x, y)
            if event.key == pygame.K_RIGHT:
                flag = 'RIGHT'
                if x + 1 <= 10 and map[x + 1 ][y] != '#':
                    x+=1
                    player.update(x, y)
            if event.key == pygame.K_LEFT:
                flag = "LEFT"
                if x - 1 >= 0 and map[x - 1][y] != '#':
                    x -= 1
                    player.update(x, y)
            if event.key == pygame.K_SPACE:
                if flag == 'UP' and  y - 1 >=0 and map[x][y - 1] == '#':
                    Tile('empty', x, y-1)
                    print(map[x][y-1])
                    map[x][y-1] = '.'
                if flag == 'DOWN' and y + 1 <= 10 and map[x][y + 1] == '#':
                    Tile('empty', x, y+1)
                    print(map[x][y+1])
                    map[x][y+1] = '.'
                if flag == 'RIGHT' and x + 1 <= 10 and map[x + 1 ][y] == '#':
                    Tile('empty', x + 1, y)
                    print(map[x + 1][y])
                    map[x + 1][y] = '.'
                if flag == 'LEFT' and  x - 1 >= 0 and map[x - 1][y] == '#':
                    Tile('empty', x - 1, y)
                    print(map[x - 1][y])
                    map[x - 1][y] = '.'
    tiles_group.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()