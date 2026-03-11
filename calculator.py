from utils.utils_functions import shape_clasificator

def main():
    while True:
        user_input = input("Enter your data (or q to quit).\n")
        user_input = user_input.lower()
        if user_input == "q":
            break
        print(shape_clasificator(user_input))


if __name__=="__main__":
    main()