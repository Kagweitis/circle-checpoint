def isInside(circle_x, circle_y, rad, x, y):
    # Compare radius of circle
    # with distance from its center
    # from the given point
    if ((x - circle_x) * (x - circle_x) +
            (y - circle_y) * (y - circle_y) <= rad * rad):
        return True;
    else:
        return False;

    # Driver Code


x = 4;
y = 5;
circle_x = 10;
circle_y = 10;
rad = 10;
if (isInside(circle_x, circle_y, rad, x, y)):
    print("the coordinates (4,5) are Inside");
else:
    print("the coordinates (4,5) are Outside");