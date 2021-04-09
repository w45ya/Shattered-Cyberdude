import pygame


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + 1280 / 2, -t + 720 / 2

    l = min(0, l)
    l = max(-(camera.width-1280), l)
    t = max(-(camera.height-720), t)
    t = min(0, t)

    return pygame.Rect(l, t, w, h)
