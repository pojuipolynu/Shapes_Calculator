import math
from key_words_class import key_words
    

def get_side_length(point1: list[float], point2: list[float]):
    side_length = math.sqrt(pow(point1[0]-point2[0], 2) + pow(point1[1]-point2[1], 2))

    return side_length

def square_data(user_input_list: list):
    try:
        side_key_index = user_input_list.index(key_words.side)
        square_side = float(user_input_list[side_key_index + 1])
    except ValueError:
        return key_words.valueerror
    except IndexError:
        return key_words.indexerror
    square_perimeter = 4 * square_side
    square_area = square_side * square_side
    return f'Square Perimeter {square_perimeter} Area {square_area}\n'

def rectangle_data(user_input_list: list):
    try:
        top_right_point_index = user_input_list.index(key_words.topright)
        bottom_left_point_index = user_input_list.index(key_words.bottomleft)
        top_right_points = [float(user_input_list[top_right_point_index + 1]), float(user_input_list[top_right_point_index + 2])]
        bottom_left_points = [float(user_input_list[bottom_left_point_index + 1]), float(user_input_list[bottom_left_point_index + 2])]
        bottom_right_points = [top_right_points[0], bottom_left_points[1]]
    except ValueError:
        return key_words.valueerror
    except IndexError:
        return key_words.indexerror

    rectangle_width = get_side_length(top_right_points, bottom_right_points)
    rectangle_length = get_side_length(bottom_left_points, bottom_right_points)

    rectangle_perimeter = 2 * (rectangle_width + rectangle_length)
    rectangle_area = rectangle_width * rectangle_length
    return f'Rectangle Perimeter {rectangle_perimeter} Area {rectangle_area}\n' 

def circle_data(user_input_list: list):
    try:
        radius_key_index = user_input_list.index(key_words.radius)
        circle_radius = float(user_input_list[radius_key_index + 1])
    except ValueError:
        return key_words.valueerror
    except IndexError:
        return key_words.indexerror
    
    circle_perimeter = 2 * 3.14 * circle_radius
    circle_area = 3.14 * circle_radius * circle_radius
    return f'Circle Perimeter {circle_perimeter} Area {circle_area}\n'

def shape_clasificator(user_input: str):
    user_input_list = user_input.split()

    separated_user_input = {
        "square" : [],
        "rectangle" : [],
        "circle" : []
    }

    key_word = ""
    
    for separated_input in user_input_list:
        if separated_input in ["square", "rectangle", "circle"]:
            key_word = separated_input
        if key_word == "":
            return key_words.valueerror
        separated_user_input[key_word].append(separated_input)

    square_result = square_data(separated_user_input["square"])
    rectangle_result = rectangle_data(separated_user_input["rectangle"])
    circle_result = circle_data(separated_user_input["circle"])
    
    return square_result+rectangle_result+circle_result

def main():
    user_input_cycle = True
    while user_input_cycle:
        user_input = input("Enter your data.\n")
        user_input = user_input.lower()
        if user_input == "q":
            break
        calculation_result = shape_clasificator(user_input)
        if calculation_result:
            print(calculation_result)


if __name__=="__main__":
    main()