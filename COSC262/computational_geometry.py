# an example related to computational geometry

import matplotlib.pyplot as plt
from graphviz import Graph

# # First some simple text output.
# vertices = [(0, 0), (100, 0), (1, 50), (100, 100), (0, 100), (0,0)]
# vx, vy = zip(*vertices)  # Unpack them
# points = [(1, 1), (20, 20), (20, 80), (60, 50),
#      (97, 1), (1, 48), (1, 52), (97, 99), (1, 99)]
# px, py = zip(*points) # Unpack
# print("Vertex x values:", vx)
# print("Vertex y values:", vy)
# print("Point x values:", px)
# print("Point y values:", py)

# # Now a matplotlib graph
# axes = plt.axes()
# axes.plot(vx, vy, color='blue', marker='o', linestyle='--')
# axes.plot(px, py, color='red', marker='x', linestyle='')
# axes.set_title('The example from the geometry lecture notes')


# g = Graph()
# g.node('Root', '23')
# g.node('Leaf1', '13', shape='box')
# g.node('Leaf2', '99', shape='box')
# g.edge('Root', 'Leaf1')
# g.edge('Root', 'Leaf2')
# g.render('graph', format='png', view=False)


class Vec:
    """A simple vector in 2D. Also used as a position vector for points"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def lensq(self):
        return self.dot(self)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


def signed_area(a, b, c):
    """Twice the area of the triangle abc.
    Positive if abc are in counter clockwise order.
    Zero if a, b, c are colinear.
    Otherwise negative.
    """
    p = b - a
    q = c - a
    return p.x * q.y - q.x * p.y


def is_ccw(a, b, c):
    """True iff triangle abc is counter-clockwise."""
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
    # May want to throw an exception if area == 0
    return area > 0


def is_on_segment(p, a, b):
    # Check if p is collinear with a and b --> 0 if collinear
    if signed_area(a, b, p) != 0:
        return False

    # Check if p is within the bounding box of a and b
    if min(a.x, b.x) <= p.x <= max(a.x, b.x) and min(a.y, b.y) <= p.y <= max(a.y, b.y):
        return True
    else:
        return False


def classify_points(line_start, line_end, points):
    """Returns a two tuple of integers.
    The first element of the tuple is the number of points from the points list that
    lie to the right of the given line, looking from start to end and
    the second element of the tuple is the number of points to the left of the line.
    The line is assumed to extend infinitely in both directions.
    You may assume that no points lie exactly on the line.
    All points are of the type Vec with integer coordinates as defined in the lecture notes
    """
    left = 0
    right = 0
    for point in points:
        left_expression = (point.x - line_start.x) * (line_end.y - line_start.y)
        right_expression = (point.y - line_start.y) * (line_end.x - line_start.x)
        expression = left_expression - right_expression
        if expression < 0:
            left += 1
        else:
            right += 1

    return (right, left)


def intersecting(a, b, c, d):
    """Returns True if the line segment from a to b intersects the line segment from c to d.
    Otherwise the function returns False.
    The parameters a, b, c and d are all points of type Vec as defined in the lecture notes.
    Coordinates are all integers.
    """
    is_intersecting = is_ccw(a, d, b) != is_ccw(a, c, b)
    different_sides = is_ccw(c, a, d) != is_ccw(c, b, d)

    return is_intersecting and different_sides


def is_strictly_convex(vertices):
    """Takes a list of three or more points, each of type Vec as in the lecture notes, and returns True if and only if the vertices,
    taken in the given order, define a strictly-convex counter-clockwise polygon.
    Otherwise the function returns False.
    While a convex polygon can have interior angles equal to 180o, a strictly-convex polygon has all interior angles strictly less than 180o.
    """
    n = len(vertices)
    if n < 3:
        return False  # Needs a min of 3 to form a polygon

    for i in range(n):
        a = vertices[i]
        b = vertices[(i + 1) % n]
        c = vertices[(i + 2) % n]

        if not is_ccw(a, b, c):
            return False

    return True


def gift_wrap(points):
    """Returns points on convex hull in CCW using the Gift Wrap algorithm"""
    # Get the bottom-most point (and left-most if necessary).
    assert len(points) >= 3
    bottommost = min(points, key=lambda p: (p.y, p.x))
    hull = [bottommost]
    done = False

    # Loop, adding one vertex at a time, until hull is (about to be) closed.
    while not done:
        candidate = None
        # Loop through all points, looking for the one that is "rightmost"
        # looking from last point on hull
        for p in points:
            if p is hull[-1]:
                continue
            if candidate is None or is_ccw(candidate, hull[-1], p):
                candidate = p
        if candidate is bottommost:
            done = True  # We've closed the hull
        else:
            hull.append(candidate)

    return hull


points = [
    Vec(1, 99),
    Vec(0, 100),
    Vec(50, 0),
    Vec(50, 1),
    Vec(50, 99),
    Vec(50, 50),
    Vec(100, 100),
    Vec(99, 99),
]
verts = gift_wrap(points)
# for v in verts:
# print(v)


points = [
    Vec(1, 1),
    Vec(99, 1),
    Vec(100, 100),
    Vec(99, 99),
    Vec(0, 100),
    Vec(100, 0),
    Vec(1, 99),
    Vec(0, 0),
    Vec(50, 50),
]
verts = gift_wrap(points)
# for v in verts:
# print(v)


class PointSortKey:
    """A class for use as a key when sorting points wrt bottommost point"""

    def __init__(self, p, bottommost):
        """Construct an instance of the sort key"""
        self.direction = p - bottommost
        self.is_bottommost = self.direction.lensq() == 0  # True if p == bottommost

    def __lt__(self, other):
        """Compares two sort keys. p1 < p2 means the vector the from bottommost point
        to p2 is to the left of the vector from the bottommost to p1.
        """
        if self.is_bottommost:
            return True  # Ensure bottommost point is less than all other points
        elif other.is_bottommost:
            return False  # Ensure no other point is less than the bottommost
        else:
            area = (
                self.direction.x * other.direction.y
                - other.direction.x * self.direction.y
            )
            return area > 0


def plot_hull(points, hull):
    """Plot the given set of points and the computed convex hull"""
    plt.scatter([p.x for p in points], [p.y for p in points])
    plt.plot([v.x for v in hull + [hull[0]]], [v.y for v in hull + [hull[0]]])
    plt.show()


def plot_poly(points):
    """Plot the given set of points as a closed polygon"""
    plt.plot([v.x for v in points + [points[0]]], [v.y for v in points + [points[0]]])
    plt.show()


def simple_polygon(points):
    """Takes a list of points (each of type Vec) and returns a simple polygon that passes through all points.
    You must use the algorithm in the notes, so that the first point will be the bottom-most (and, if necessary, left-most) point
    and the other points follow in counter-clockwise order.
    The return value should be a list of points of type Vec.
    """
    bottommost = min(points, key=lambda p: (p.y, p.x))
    simply_poly = sorted(points, key=lambda p: PointSortKey(p, bottommost))
    return simply_poly


def graham_scan(points):
    bottommost = min(points, key=lambda p: (p.y, p.x))
    sorted_points = simple_polygon(points)
    hull = [bottommost, sorted_points[0]]

    for p in sorted_points[1:]:
        while len(hull) >= 2 and not is_ccw(hull[-2], hull[-1], p):
            hull.pop()
        hull.append(p)
    return hull


points = [Vec(100, 100), Vec(0, 100), Vec(50, 0)]
verts = graham_scan(points)
# for v in verts:
# print(v)


points = [Vec(100, 100), Vec(0, 100), Vec(100, 0), Vec(0, 0), Vec(49, 50)]
verts = graham_scan(points)
# for v in verts:
# print(v)


points = [Vec(100, 100), Vec(0, 100), Vec(50, 0)]
verts = simple_polygon(points)
# for v in verts:
# print(v)


points = [Vec(100, 100), Vec(0, 100), Vec(100, 0), Vec(0, 0), Vec(49, 50)]
verts = simple_polygon(points)
# for v in verts:
# print(v)


verts = [(0, 0), (100, 0), (100, 100), (0, 100)]
points = [Vec(v[0], v[1]) for v in verts]
# print(is_strictly_convex(points))


verts = [(0, 0), (0, 100), (100, 100), (100, 0)]
points = [Vec(v[0], v[1]) for v in verts]
# print(is_strictly_convex(points))


a = Vec(0, 0)
b = Vec(100, 0)
c = Vec(101, 1)
d = Vec(101, -1)
# print(intersecting(a, b, c, d))

a = Vec(0, 0)
b = Vec(100, 0)
c = Vec(99, 1)
d = Vec(99, -1)
# print(intersecting(a, b, c, d))

points = [
    Vec(1, 99),
    Vec(0, 100),
    Vec(50, 0),
    Vec(50, 1),
    Vec(50, 99),
    Vec(50, 50),
    Vec(100, 100),
    Vec(99, 99),
]

# print(classify_points(Vec(0, 49), Vec(100, 49), points))


points = [
    Vec(1, 99),
    Vec(0, 100),
    Vec(50, 0),
    Vec(50, 1),
    Vec(50, 99),
    Vec(50, 50),
    Vec(100, 100),
    Vec(99, 99),
]

# print(classify_points(Vec(100, 49), Vec(0, 49), points))

a = Vec(1000, 2000)
b = Vec(0, 0)
p = Vec(500, 1000)
# print(is_on_segment(p, a, b))


a = Vec(0, 0)
b = Vec(1000, 2000)
point_tuples = [
    (-1, -1),
    (-1, -2),
    (-1000, -2000),
    (0, 0),
    (1, 2),
    (500, 1000),
    (500, 1001),
    (500, 999),
    (1000, 2000),
    (1001, 2001),
    (1001, 2002),
    (2000, 4000),
]
points = [Vec(p[0], p[1]) for p in point_tuples]
# for p in points:
#     print(p, is_on_segment(p, a, b))


# Do not alter the next two lines
from collections import namedtuple

Node = namedtuple("Node", ["value", "left", "right"])


# Rewrite the following function to avoid slicing
def binary_search_tree(nums, is_sorted=False, start=0, end=None):
    """Return a balanced binary search tree with the given nums
    at the leaves. is_sorted is True if nums is already sorted.
    Avoids slicing by using start and end indices.
    """
    if not is_sorted:
        nums = sorted(nums)
        is_sorted = True  # Ensure we don't sort in recursive calls

    if end is None:
        end = len(nums)

    n = end - start
    if n == 1:
        tree = Node(nums[start], None, None)  # A leaf
    else:
        mid = start + n // 2  # Midpoint index
        left = binary_search_tree(nums, is_sorted, start, mid)
        right = binary_search_tree(nums, is_sorted, mid, end)
        tree = Node(nums[mid - 1], left, right)

    return tree


# Leave the following function unchanged
def print_tree(tree, level=0):
    """Print the tree with indentation"""
    if tree.left is None and tree.right is None:  # Leaf?
        print(2 * level * " " + f"Leaf({tree.value})")
    else:
        print(2 * level * " " + f"Node({tree.value})")
        print_tree(tree.left, level + 1)
        print_tree(tree.right, level + 1)


nums = [22, 41, 19, 27, 12, 35, 14, 20, 39, 10, 25, 44, 32, 21, 18]
tree = binary_search_tree(nums)
# print_tree(tree)


class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
    origin to define points.
    """

    point_num = 0
    box_calls = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.label = "P" + str(Vec.point_num)
        Vec.point_num += 1

    def __add__(self, other):
        """Vector addition"""
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Vector subtraction"""
        return Vec(self.x - other.x, self.y - other.y)

    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)

    def dot(self, other):
        """Dot product"""
        return self.x * other.x + self.y * other.y

    def lensq(self):
        """The square of the length"""
        return self.dot(self)

    def in_box(self, bottom_left, top_right):
        """True iff this point (warning, not a vector!) lies within or on the
        boundary of the given rectangular box area"""
        Vec.box_calls += 1
        return (
            bottom_left.x <= self.x <= top_right.x
            and bottom_left.y <= self.y <= top_right.y
        )

    def __getitem__(self, axis):
        return self.x if axis == 0 else self.y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

    def __lt__(self, other):
        """Less than operator, for sorting"""
        return (self.x, self.y) < (other.x, other.y)


class KdTree:
    """A 2D k-d tree"""

    LABEL_POINTS = True
    LABEL_OFFSET_X = 0.25
    LABEL_OFFSET_Y = 0.25

    def __init__(self, points, depth=0, max_depth=10):
        """Initialiser, given a list of points, each of type Vec, the current
        depth within the tree (0 for the root) and the maximum depth
        allowable for a leaf node.
        """
        if len(points) < 2 or depth >= max_depth:  # Ensure at least one point per leaf
            self.is_leaf = True
            self.points = points
        else:
            self.is_leaf = False
            self.axis = (
                depth % 2
            )  # 0 for vertical divider (x-value), 1 for horizontal (y-value)
            points = sorted(points, key=lambda p: p[self.axis])
            halfway = len(points) // 2
            self.coord = points[halfway - 1][self.axis]
            self.leftorbottom = KdTree(points[:halfway], depth + 1, max_depth)
            self.rightortop = KdTree(points[halfway:], depth + 1, max_depth)

    def points_in_range(self, query_rectangle):
        """Return a list of all points in the tree 'self' that lie within or
        on the boundary of the given query rectangle, which is defined by
        a pair of points (bottom_left, top_right), both of which are Vecs.
        """
        bottom_left, top_right = query_rectangle
        matches = []
        if self.is_leaf == True:
            matches = [points for points in self.points if points.in_box(bottom_left, top_right)]
        else:
            if bottom_left[self.axis] <= self.coord:
                matches += self.leftorbottom.points_in_range(query_rectangle)
            if top_right[self.axis] >= self.coord:
                matches += self.rightortop.points_in_range(query_rectangle)

        return matches

    def plot(self, axes, top, right, bottom, left, depth=0):
        """Plot the the kd tree. axes is the matplotlib axes object on
        which to plot, top, right, bottom, left are the coordinates of
        the bounding box of the plot.
        """

        if self.is_leaf:
            axes.plot([p.x for p in self.points], [p.y for p in self.points], "bo")
            if self.LABEL_POINTS:
                for p in self.points:
                    axes.annotate(
                        p.label,
                        (p.x, p.y),
                        xytext=(p.x + self.LABEL_OFFSET_X, p.y + self.LABEL_OFFSET_Y),
                    )
        else:
            if self.axis == 0:
                axes.plot([self.coord, self.coord], [bottom, top], "-", color="gray")
                self.leftorbottom.plot(axes, top, self.coord, bottom, left, depth + 1)
                self.rightortop.plot(axes, top, right, bottom, self.coord, depth + 1)
            else:
                axes.plot([left, right], [self.coord, self.coord], "-", color="gray")
                self.leftorbottom.plot(axes, self.coord, right, bottom, left, depth + 1)
                self.rightortop.plot(axes, top, right, self.coord, left, depth + 1)
        if depth == 0:
            axes.set_xlim(left, right)
            axes.set_ylim(bottom, top)

    def __repr__(self, depth=0):
        """String representation of self"""
        if self.is_leaf:
            return depth * 2 * " " + "Leaf({})".format(self.points)
        else:
            s = depth * 2 * " " + "Node({}, {}, \n".format(self.axis, self.coord)
            s += self.leftorbottom.__repr__(depth + 1) + "\n"
            s += self.rightortop.__repr__(depth + 1) + "\n"
            s += depth * 2 * " " + ")"  # Close the node's opening parens
            return s


point_tuples = [(1, 3), (10, 20), (5, 19), (0, 11), (15, 22), (30, 5)]
points = [Vec(*tup) for tup in point_tuples]
tree = KdTree(points)
in_range = tree.points_in_range((Vec(0, 3), Vec(5, 19)))
# print(sorted(in_range))


class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
    origin to define points.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Vector addition"""
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Vector subtraction"""
        return Vec(self.x - other.x, self.y - other.y)

    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)

    def dot(self, other):
        """Dot product"""
        return self.x * other.x + self.y * other.y

    def lensq(self):
        """The square of the length"""
        return self.dot(self)

    def __getitem__(self, axis):
        return self.x if axis == 0 else self.y

    def __repr__(self):
        """String representation of self"""
        return "({}, {})".format(self.x, self.y)


class QuadTree:
    """A QuadTree class for COSC262.
    Richard Lobb, May 2019
    """

    MAX_DEPTH = 20

    def __init__(self, points, centre, size, depth=0, max_leaf_points=2):
        self.centre = centre
        self.size = size
        self.depth = depth
        self.max_leaf_points = max_leaf_points
        self.children = []

        points = [p for p in points if self.in_square(p, centre, size)]
        if len(points) > max_leaf_points and depth < QuadTree.MAX_DEPTH:
            self.is_leaf = False
            half_size = size / 2
            quarter_size = size / 4
            centres = [
                Vec(centre.x - quarter_size, centre.y - quarter_size),
                Vec(centre.x - quarter_size, centre.y + quarter_size),
                Vec(centre.x + quarter_size, centre.y - quarter_size),
                Vec(centre.x + quarter_size, centre.y + quarter_size),
            ]
            for i in range(4):
                child_points = [
                    p for p in points if self.in_square(p, centres[i], half_size)
                ]
                child = QuadTree(
                    child_points, centres[i], half_size, depth + 1, max_leaf_points
                )
                self.children.append(child)
        else:
            self.is_leaf = True
            self.points = points

    def in_square(self, point, centre, size):
        """Check if a point is within the square defined by the centre and size."""
        half_size = size / 2
        return (centre.x - half_size <= point.x <= centre.x + half_size) and (
            centre.y - half_size <= point.y <= centre.y + half_size
        )

    def plot(self, axes):
        """Plot the dividing axes of this node and
        (recursively) all children"""
        if self.is_leaf:
            axes.plot([p.x for p in self.points], [p.y for p in self.points], "bo")
        else:
            axes.plot(
                [self.centre.x - self.size / 2, self.centre.x + self.size / 2],
                [self.centre.y, self.centre.y],
                "-",
                color="gray",
            )
            axes.plot(
                [self.centre.x, self.centre.x],
                [self.centre.y - self.size / 2, self.centre.y + self.size / 2],
                "-",
                color="gray",
            )
            for child in self.children:
                child.plot(axes)
        axes.set_aspect(1)

    def __repr__(self, depth=0):
        """String representation with children indented"""
        indent = 2 * self.depth * " "
        if self.is_leaf:
            return indent + "Leaf({}, {}, {})".format(
                self.centre, self.size, self.points
            )
        else:
            s = indent + "Node({}, {}, [\n".format(self.centre, self.size)
            for child in self.children:
                s += child.__repr__(depth + 1) + ",\n"
            s += indent + "])"
            return s


# Example test
import matplotlib.pyplot as plt

points = [(60, 15), (15, 60), (30, 58), (42, 66), (40, 70)]
vecs = [Vec(*p) for p in points]
tree = QuadTree(vecs, Vec(50, 50), 100)
print(tree)

# Plot the tree, for debugging only
axes = plt.axes()
tree.plot(axes)
axes.set_xlim(0, 100)
axes.set_ylim(0, 100)
plt.show()
