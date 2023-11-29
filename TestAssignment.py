from math import sqrt

def pythagorean_distance(coord1, coord2):
    delta_x = coord2[0] - coord1[0]
    delta_y = coord2[1] - coord1[1]

    distance = sqrt(delta_x**2 + delta_y**2)

    return distance

def generate_points_between_coordinates(coord1, coord2, interval=25):

    points = []
    distance = pythagorean_distance(coord1, coord2)


    if distance <= interval:
        return [coord1, coord2]

    num_points = int(distance / interval)

    for i in range(1, num_points):

        fraction = i / num_points
        intermediate_point = (
            coord1[0] + fraction * (coord2[0] - coord1[0]),
            coord1[1] + fraction * (coord2[1] - coord1[1])
        )

        points.append(intermediate_point)
    for i in range(len(points)):
        print(points[i])

    return [coord1] + points + [coord2]

coordinate1 = (100, 150)
coordinate2 = (20,90)
points_between_coordinates = generate_points_between_coordinates(coordinate1, coordinate2)

