import math
from utils.key_words_class import key_words
from utils.shapes_template import Circle, Square, Rectangle

def get_side_length(point1: list[float], point2: list[float]):
    side_length = math.sqrt(pow(point1[0]-point2[0], 2) + pow(point1[1]-point2[1], 2))

    return side_length

def input_separator(user_input: str) -> dict:
    user_input_list = user_input.split()

    key_word = ""

    separated_user_input = {
        key_words.square : [],
        key_words.rectangle : [],
        key_words.circle : []
    }
    
    for separated_input in user_input_list:
        if separated_input in [key_words.square, key_words.rectangle, key_words.circle]:
            key_word = separated_input
        if key_word == "":
            return key_words.valueerror
        separated_user_input[key_word].append(separated_input)

    return separated_user_input

def shape_clasificator(user_input: str) -> str:
    calculation_output = ""
    separated_user_input = input_separator(user_input)
    
    try:

        if separated_user_input[key_words.square]:
            square_object = Square.parse_data(separated_user_input[key_words.square])
            calculation_output += str(square_object) + "\n"

        if separated_user_input[key_words.rectangle]:
            topright_index = separated_user_input[key_words.rectangle].index(key_words.topright)
            bottomleft_index = separated_user_input[key_words.rectangle].index(key_words.bottomleft)

            topright_points = [float(separated_user_input[key_words.rectangle][topright_index + 1]), float(separated_user_input[key_words.rectangle][topright_index + 2])]
            bottomleft_points = [float(separated_user_input[key_words.rectangle][bottomleft_index + 1]), float(separated_user_input[key_words.rectangle][bottomleft_index + 2])]
            bottomright_points = [topright_points[0], bottomleft_points[1]]

            rectangle_width = get_side_length(topright_points, bottomright_points)
            rectangle_length = get_side_length(bottomleft_points, bottomright_points)

            calculation_output += str(Rectangle(rectangle_width, rectangle_length)) + "\n"

        if separated_user_input[key_words.circle]:
            radius_index = separated_user_input[key_words.circle].index(key_words.radius) + 1

            calculation_output += str(Circle(float(separated_user_input[key_words.circle][radius_index]))) + "\n"

    except (ValueError, TypeError):
        return key_words.valueerror
    except IndexError:
        return key_words.indexerror

    return calculation_output if calculation_output else key_words.indexerror