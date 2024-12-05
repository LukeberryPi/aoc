import math

def find_next_odd_root(n: int) -> int:
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if i ** 2 >= n:
            return i

    return 0

def main(n: int) -> int:
    n_layer = find_next_odd_root(n)
    largest_odd_square = n_layer ** 2
    central_square_coordinates = [n_layer // 2, n_layer // 2]
    distance_to_largest_odd_square = largest_odd_square - 312051

    if distance_to_largest_odd_square < n_layer:
        n_coordinates = [distance_to_largest_odd_square - n_layer - 1, n_layer - 1]
    else:
        return 0

    result = 0
    for coordinate_central_square, coordinate_n in zip(central_square_coordinates, n_coordinates):
        result += abs(coordinate_central_square - coordinate_n)

    return result


with open('2017/3/input.txt') as f:
    print(main(int(f.read())))