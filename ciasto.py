from math import pi

def get_baking_mold_shape(prompt):
    is_shape_valid = False
    while not is_shape_valid:
        shape = input(prompt + ' (o - okrągła, p - prostokątna): ')
        is_shape_valid = shape in ['o', 'p']
    return shape


def get_baking_mold_area(shape, is_ori):
    suffix = ' wyjściowej: ' if is_ori else ' docelowej: '
    if shape == 'o':
        r = float(input('Podaj promień formy' + suffix))
        area = pi * r ** 2
    elif shape == 'p':
        a = float(input('Podaj szerokość formy' + suffix))
        b = float(input('Podaj wysokość formy' + suffix))
        area = a * b
    
    return area


ori_shape = get_baking_mold_shape('Podaj kształt formy wyjściowej')
to_shape = get_baking_mold_shape('Podaj kształt formy docelowej')

ori = get_baking_mold_area(ori_shape, True)
to = get_baking_mold_area(to_shape, False)
wsp = to / ori

is_still_running = True
while is_still_running:
    how_much = float(input('Ile? (podaj liczbę mniejszą lub równą zeru, aby zakończyć): '))
    is_still_running = how_much >= 0
    print(how_much * wsp if is_still_running else 'Do widzenia!')
