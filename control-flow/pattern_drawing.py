def draw_pattern(size):
    row = 0
    while row < size:
        for i in range(size):
            print("*", end="")
        print()
        row =+ 1

def main():
    size = int(input("Enter the size of the pattern: "))
    if size > 0:
        draw_pattern(size)
    else:
        print("Please enter a positive interger.")

if __name__ == "__main__":
    main()

