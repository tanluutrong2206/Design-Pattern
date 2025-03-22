import pygame

from factory_method.random_shape.ShapeFactory import ShapeFactory


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Factory Method Pattern Example")
    clock = pygame.time.Clock()

    shape_factory = ShapeFactory()
    shapes = []
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                shape_type = "circle" if len(shapes) % 2 == 0 else "square"
                shape = shape_factory.create_shape(shape_type, x, y)
                shapes.append(shape)

        screen.fill((255, 255, 255))
        for shape in shapes:
            shape.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()