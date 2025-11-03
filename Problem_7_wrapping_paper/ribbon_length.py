def wrapping_paper_area(l: int, w: int, h: int) -> int:
    """
    Calculate total wrapping paper needed for one box.
    Formula: 2*l*w + 2*w*h + 2*h*l + area of smallest side
    """
    side1 = l * w
    side2 = w * h
    side3 = h * l
    extra = min(side1, side2, side3)
    return 2 * (side1 + side2 + side3) + extra


def ribbon_length(l: int, w: int, h: int) -> int:
    """
    Calculate total ribbon needed for one box.
    Formula: smallest perimeter + volume
    """
    sides = sorted([l, w, h])
    smallest_perimeter = 2 * (sides[0] + sides[1])
    volume = l * w * h
    return smallest_perimeter + volume


# Main program
if __name__ == "__main__":
    print("Enter box dimensions as l,w,h (comma separated). Type 'done' to finish.")

    total_paper = 0
    total_ribbon = 0

    while True:
        entry = input("Box: ").strip()
        if entry.lower() == "done":
            break
        try:
            l, w, h = map(int, entry.split(","))
            total_paper += wrapping_paper_area(l, w, h)
            total_ribbon += ribbon_length(l, w, h)
        except ValueError:
            print("Invalid format. Please enter like 2,3,4")

    print(f"\nTotal wrapping paper needed: {total_paper} square feet")
    print(f"Total ribbon needed: {total_ribbon} feet")

