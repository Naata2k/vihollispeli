import pygame

naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Piirtäminen")

def main():
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break

        naytto.fill((0, 0, 0))
        pygame.draw.line(naytto, (0, 0, 255), (640, 400), (0, 0))
        pygame.display.flip()
        pygame.draw.line(naytto, (0, 255, 0), (640, 0), (0, 400))
        pygame.display.flip()

main()