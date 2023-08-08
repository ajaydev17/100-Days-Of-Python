import math


def paint_calci(width, height, coverage):
    total_area = width * height
    number_of_cans = math.ceil(total_area / coverage)
    return number_of_cans


wall_width = int(input("Enter the width of the wall: "))
wall_height = int(input("Enter the height of the wall: "))
can_per_coverage = 5

result = paint_calci(width=wall_width, height=wall_height,
                     coverage=can_per_coverage)
print(f"You would need {result} cans to paint the entire wall!!.")
