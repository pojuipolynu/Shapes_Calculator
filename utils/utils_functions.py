import math
from utils.key_words_class import key_words
from utils.shapes_template import Circle, Square, Rectangle

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
            rectangle_object = Rectangle.parse_data(separated_user_input[key_words.rectangle])

            calculation_output += str(rectangle_object) + "\n"

        if separated_user_input[key_words.circle]:
            radius_index = separated_user_input[key_words.circle].index(key_words.radius) + 1

            calculation_output += str(Circle(float(separated_user_input[key_words.circle][radius_index]))) + "\n"

    except (ValueError, TypeError):
        return key_words.valueerror
    except IndexError:
        return key_words.indexerror

    return calculation_output if calculation_output else key_words.indexerror