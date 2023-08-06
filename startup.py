from pygame import init, display

def startup():
    init()
    screen = display.set_mode((1200, 800))
    return screen