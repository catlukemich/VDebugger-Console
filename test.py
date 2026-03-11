from vdebugger import *

def test_console():
    vd("a", "B")
    vd("a", "B")
    vd("foo", 123)
  
    vd("blu", {"nope": "nonono"})
    vd("blu", {"nope": "nonono"})

def test_pygame():
    import pygame
    pygame.init()
    pygame.display.set_mode((800,600))
    done = False
    clock = pygame.time.Clock()
    some_input = ""
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vd("quit", "yes")
                if vditers("quit", 5):
                    done = True
            if event.type == pygame.MOUSEMOTION:
                vd("pos", event.pos)
                print(event)
            if event.type == pygame.KEYDOWN:
                vd("key pressed", str(event.mod) + " " + chr(event.key))
                some_input += chr(event.key)
                vd("some_input", some_input)
        pygame.display.update()
        clock.tick(20)


if __name__ == "__main__":
    test_console()
    




