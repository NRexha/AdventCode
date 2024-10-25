def get_digits(word):
    left, right = 0, len(word) - 1
    first_digit = last_digit = '0'

    while left < len(word):
        if word[left].isdigit():
            first_digit = word[left]
            break
        left += 1

    while right >= 0:
        if word[right].isdigit():
            last_digit = word[right]
            break
        right -= 1

    return int(first_digit + last_digit)
    


def main():
    total_sum = 0

    with open("PuzzleInput.txt", "r") as file:
        for line in file:
            word = line.strip()
            combined_number = get_digits(word)
            total_sum += combined_number

    print(total_sum)


if __name__ == "__main__":
    main()
