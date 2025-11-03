def wrapping_paper_area(l: int, w: int, h: int) -> int:
    """
    Calculate total wrapping paper needed for one box.
    Formula:
        Surface area = 2*l*w + 2*w*h + 2*h*l
        Extra paper = area of the smallest side
    Total = Surface area + Extra paper
    """
    side1 = l * w
    side2 = w * h
    side3 = h * l
    extra = min(side1, side2, side3)
    total = 2 * (side1 + side2 + side3) + extra
    return total


if __name__ == "__main__":
    print(" Wrapping Paper Calculator ")
    print("Enter box dimensions as l,w,h (comma separated). Type 'done' to finish.\n")

    total_paper = 0

    while True:
        entry = input("Enter box dimensions: ").strip()
        if entry.lower() == "done":
            break
        try:
            l, w, h = map(int, entry.split(","))
            paper = wrapping_paper_area(l, w, h)
            print(f"Paper needed for this box: {paper} square feet\n")
            total_paper += paper
        except ValueError:
            print(" Invalid input. Use format like: 2,3,4\n")

    print(f"🎉 Total wrapping paper needed: {total_paper} square feet")

