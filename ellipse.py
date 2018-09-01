import math
import shapely
from shapely.geometry import Polygon


class Ellipse():

    def __init__(self, a, b, resolution=1000):
        self.center = 0.
        self.a = a
        self.b = b
        self.polygon = Polygon(self.make_points(resolution))
        self.area = self.polygon.area

    def make_points(self, precision):
        points = list()
        thetas = [(i/float(precision))*2*math.pi for i in range(precision)]
        for i in range(precision):
            theta = (i/float(precision))*2*math.pi
            points.append((self.x(theta), self.y(theta)))
        return list((self.x(theta), self.y(theta)) for theta in thetas)

    def x(self, theta):
        return self.a*math.cos(theta)

    def y(self, theta):
        return self.b*math.sin(theta)

    def intersection(self, ellipse):
        return self.polygon.intersection(ellipse.polygon)

    def translate(self, y_offset):
        self.center += y_offset
        self.polygon = shapely.affinity.translate(self.polygon, yoff=y_offset)


def find_distance_for_half_intersect(reference_ellipse, intersect_ellipse, precision=1e-15):
    timeout = 0
    target_area = 0.5*reference_ellipse.area
    distance = False
    lower_bound = 0
    upper_bound = 2*max(reference_ellipse.a, intersect_ellipse.a)
    assert(reference_ellipse.intersection(intersect_ellipse).area>=target_area) 
    while not distance:
        timeout+=1
        current_distance = float(lower_bound+upper_bound)/2
        intersect_ellipse.translate(current_distance-intersect_ellipse.center)
        current_area = reference_ellipse.intersection(intersect_ellipse).area
        print('current_distance: '+str(current_distance))
        print('intersect area: '+str(current_area))
        print('error: '+str(abs(target_area-current_area)))
        print('-------------------------------------------------------------------')
        if abs(target_area-current_area)<precision:
            distance = current_distance
        elif target_area>current_area:
            upper_bound=current_distance
        elif target_area<current_area:
            lower_bound=current_distance
        else:
            raise()

        if timeout > 10000:
            print('damn')
            return
    print('-------------------------------------------------------------------')
    print('Distance: '+str(distance))

    return distance

