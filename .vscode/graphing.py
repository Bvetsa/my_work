import math

x1 = (int(input("Give me the x of the first point on your graph. ")))
y1 = (int(input("Give me the y of the first point of your graph. ")))
x2 = (int(input("Give me the x of the second point of your graph. ")))
y2 = (int(input("Give me the y of the second point of your graph. ")))



distx = x1 - x2
disty = y1 - y2
distxy = distx ** 2 + disty ** 2
hypo = math.sqrt(distxy)
'''
def print_data():
    print("\n")
    print("The first point is " + str(p1))
    print("The second point is " + str(p2))
    print("The slope of the two points is " + str(slope))
    print("The distance between the two points is " + str(hypo))
'''
class graph_point: #creates class
    def __init__(self, x, y): #creates function init which creates attributes for objects
        self.x = x #turns the self.x into just x to make it easier to use
        self.y = y #same as previous

    def print_point(self): #creates function print point
        print( "(" + str(self.x) + "," + str(self.y) + ")" ) #prints out the point in proper format (x,y)

    def distance_from_center(self): #creates function distance from center
        center_point = graph_point(0,0) #creates a variable with a point (0,0)
        self.distance_from_another_point( center_point ) #finds the distance between 2 points with one point being (0,0)
    
    def slope_between_2_points(self,p2):
        slope_numerator = y2 - y1
        slope_denomenator = x2 - x1
        slope = slope_numerator / slope_denomenator
        print(slope)

    def slope_from_center(self,):
        center_point = graph_point(0,0)
        slope_center = self.slope_between_2_points(center_point)
        print(slope_center)
    
    def area_from_another_point(self, p2):
        area = distx * disty * 1/2
        print(area)

    def area_from_center(self):
        center_point = graph_point(0,0)
        area_center = self.area_from_another_point(center_point)
        print(area_center)

    def distance_from_another_point( self, p2 ): #creates function with 2 variables, self and new variable
        x_distance = self.x - p2.x #finds the distance between x's between the 2 points
        y_distance = self.y - p2.y #finds the distance between y's of both points
        print( math.sqrt( ( x_distance * x_distance ) + (y_distance * y_distance ) ) ) #finds and prints the distance of the 2 points
    def smallest_angle(self, p2):
        if distx == disty:
            print("45")
        elif distx > disty:
            print(math.atan(disty/distx) * 180 / math.pi)
        elif disty < distx:
            print(math.atan(distx/disty) * 180 / math.pi + )
p1 = graph_point(x1, y1)
p2 = graph_point(x2, y2)


p1.print_point() #calls the function print point with point 1 variable
p2.distance_from_center() #calls the function distance from center with p2 as its variable
p1.distance_from_another_point( p2 ) #calls dinstance from another point function between p1 and p2
p1.slope_between_2_points(p2)
p1.slope_from_center()
p1.area_from_another_point(p2)
p1.area_from_center()
p1.smallest_angle(p2)
