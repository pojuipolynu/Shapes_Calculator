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

    class_dictionary = {
        "square": Square,
        "rectangle": Rectangle,
        "circle": Circle
    }
    
    try:
        for key in [key_words.square, key_words.rectangle, key_words.circle]:
            if separated_user_input[key]:
                shape_object = class_dictionary[key].parse_data(separated_user_input[key])
                calculation_output += str(shape_object) + "\n"

    except (ValueError, TypeError):
        return key_words.valueerror
    except IndexError:
        return key_words.indexerror

    return calculation_output if calculation_output else key_words.indexerror