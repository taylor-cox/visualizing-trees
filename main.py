from tree import Tree, Node, TreeDrawer
import pygame, random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

if __name__ == '__main__':
    tree = Tree(None)
    # Example tree
    toAdd = [0]
    for i in range(50):
        x = random.randrange(-100, 100)
        while x in toAdd:
            x = random.randrange(-100, 100)
        toAdd.append(x)
    for value in toAdd:
        tree.add(Node(value))
    for value in toAdd:
        print(str(tree.contains(Node(value))) + ', ' + str(value))

    print(str(tree.size()) + ', ' + str(len(toAdd)))
    
    

    # Pygame setup
    size = width, height = (1000,1000)
    pygame.init()
    screen = pygame.display.set_mode(size) # Main screen
    screen.fill(WHITE)
    running = True
    circleRadius = 50 # Radius of circles being drawn
    
    treeCircles = pygame.Surface(size, pygame.SRCALPHA, 32)
    treeCircles = treeCircles.convert_alpha()
    
    TreeDrawer().drawRadially(tree, treeCircles, circleRadius, BLACK, size)

    # Main pygame loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE) # Clear screen

        backgroundCircles = pygame.Surface(size) # Drawing surface
        backgroundCircles.fill(WHITE) # Clear the surface

        # Adds all the background circles
        for i in range(1, 100):
            pygame.draw.circle(backgroundCircles, BLACK, (int(width / 2), int(height / 2)), circleRadius * i, 1)
        
        # Make the circles slightly transparent
        backgroundCircles.set_alpha(100)

        screen.blit(backgroundCircles, (0, 0))
        screen.blit(treeCircles, (0, 0))
        pygame.display.flip()

