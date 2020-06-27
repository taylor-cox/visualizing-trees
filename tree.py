import pygame, math, random

class Tree:
    def __init__(self, top):
        self.top = top
    
    def add(self, node):
        working = self.top
        parentWorking = None

        if self.top is None:
            self.top = node
            return
        
        running = True
        while(running):
            if working is not None and working.getValue() > node.getValue():
                parentWorking = working
                working = working.getLeft()
            elif working is not None and working.getValue() < node.getValue():
                parentWorking = working
                working = working.getRight()
            elif working is None and parentWorking.getValue() > node.getValue():
                parentWorking.setLeft(node)
                running = False
            elif working is None and parentWorking.getValue() < node.getValue():
                parentWorking.setRight(node)
                running = False
            elif working.getValue() == node.getValue():
                print(f'Already added {node.getValue()} value to the tree!')
                running = False
    
    def size(self):
        if self.top is None:
            return 0
        return self.top.size()

    def contains(self, node):
        if self.top is None:
            return False
        return self.top.contains(node)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def setParent(self, parent):
        self.parent = parent

    def getValue(self):
        return self.value
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def setLeft(self, left):
        self.left = left
    
    def setRight(self, right):
        self. right = right
    
    def __str__(self):
        return str(self.value)
    
    def size(self):
        if self.left is not None and self.right is not None:
            return 1 + self.left.size() + self.right.size()
        elif self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return 1 + self.right.size()
        else:
            return 1 + self.left.size()
    
    def contains(self, node):
        if node.value == self.value:
            return True
        elif node.value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(node)
        elif node.value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(node)

class TreeDrawer:
    """ Draws the tree to the screen radially. """
    def drawRadially(self, tree, screen, radius, color = (0, 0, 0), size = (0, 0)):
        # Global-esque variables which helper functions use
        self.color = color
        self.screen = screen
        workingNode = tree.top
        self.circleRadius = 15
        self.fontSize = 16
        self.centerOfScreen = (int(size[0] / 2), int(size[1] / 2))

        # Base case
        if workingNode is None:
            return

        # Draw center circle and text
        pygame.draw.circle(screen, color, self.centerOfScreen, self.circleRadius, 1)
        font = pygame.font.Font('freesansbold.ttf', self.fontSize) 
        text = font.render(str(workingNode.getValue()), True, self.color) 
        textRect = text.get_rect()
        textRect.center = self.centerOfScreen
        self.screen.blit(text, textRect)

        # Recursive algorithm to draw the tree to the screen
        self.__drawRadial__(workingNode.getLeft(), 1, radius, self.centerOfScreen, (-90, 90))
        self.__drawRadial__(workingNode.getRight(), 1, radius, self.centerOfScreen, (90, 270))

    """ Recursive helper function for draw radially. Draws the circles to the screen in correct position. """
    def __drawRadial__(self, node, circleNum, radius, fromPoint, angleRange):
        if node is None: # Base case
            return

        # The angle where to draw the circle, imagine unit circle
        angle = math.radians(random.randrange(angleRange[0], angleRange[1]))

        # New center point, based on the angle, the center of the screen, the radius and the # of the circle
        centerPoint = (int(self.centerOfScreen[0] + (circleNum * radius * math.cos(angle))), int(self.centerOfScreen[1] + (circleNum * radius * -math.sin(angle))))

        # Text in the center of the circle (value of the node)
        font = pygame.font.Font('freesansbold.ttf', self.fontSize) 
        text = font.render(str(node.getValue()), True, self.color) 
        textRect = text.get_rect()
        textRect.center = centerPoint
        self.screen.blit(text, textRect)

        # Circle containing value.
        pygame.draw.circle(self.screen, self.color, centerPoint, self.circleRadius, 1)
        # Line connecting last value with this value.
        pygame.draw.line(self.screen, self.color, fromPoint, centerPoint, 1)

        # Average value of the angle range, useful in determining next range
        angRangeValue = int((angleRange[1] - angleRange[0]) / 2)

        nextAngleRangeRight = (angleRange[0], angleRange[1] - angRangeValue)
        nextAngleRangeLeft = (angleRange[0] + angRangeValue, angleRange[1])

        self.__drawRadial__(node.getLeft(), circleNum + 1, radius, centerPoint, nextAngleRangeLeft)
        self.__drawRadial__(node.getRight(), circleNum + 1, radius, centerPoint, nextAngleRangeRight)
