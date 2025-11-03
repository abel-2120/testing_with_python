# santa_floors.py

def final_floor(instructions):

    floor = 0
    for char in instructions:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
    return floor


def first_basement_position(instructions):
   

    floor = 0
    for i, char in enumerate(instructions, start=1):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor == -1:
            return i
    return None  # if Santa never enters the basement


# Example usage
if __name__ == "__main__":
    data = input("Enter Santa's directions (e.g. ()())(()): ")
    print("Final Floor:", final_floor(data))
    position = first_basement_position(data)
    if position:
        print("First enters basement at position:", position)
    else:
        print("Santa never enters the basement.")

