
import pygame

class Path:
    def __init__(self, points):
        self.points = [pygame.Vector2(point) for point in points]

    def draw(self, surface):
        for i in range(len(self.points) - 1):
            pygame.draw.line(surface, (0, 0, 0), self.points[i], self.points[i + 1], 50)
            pygame.draw.rect(surface, (0, 0, 0), (self.points[i].x - 15, self.points[i].y - 15, 30, 30))


# import pygame

# class Path:
#     def __init__(self, points):
#         self.points = [pygame.Vector2(point) for point in points]

#     def draw(self, surface):
#         for i in range(len(self.points) - 1):
#             pygame.draw.line(surface, (0, 0, 0), self.points[i], self.points[i + 1], 50)
#             square_rect = pygame.Rect(self.points[i], self.points[i + 1], 30, 30)
#             pygame.draw.rect(surface, (0, 0, 0), square_rect)


    #         pygame.draw.s(surface, (0, 0, 0), self.points[i], self.points[i + 1], 50)
        
    # def draw(self, surface):
    #     for point in self.points:
    #         # Draw square
    #         square_rect = pygame.Rect(point.x - 15, point.y - 15, 30, 30)
    #         pygame.draw.rect(surface, (0, 0, 0), square_rect)
            
    #         # Draw line
    #         index = self.points.index(point)
    #         if index < len(self.points) - 1:
    #             pygame.draw.line(surface, (0, 0, 0), point, self.points[index + 1], 50)