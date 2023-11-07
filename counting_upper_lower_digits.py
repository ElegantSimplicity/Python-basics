def count_characters(chain_of_characters: str) -> tuple[int, int, int]:
    """
    Đếm số ký tự in hoa, in thường và số trong một chuỗi.

    Args:
        chain_of_characters: Chuỗi cần đếm.

    Returns:
        Tuple gồm số ký tự in hoa, in thường và số.
    """

    count_upper = 0
    count_lower = 0
    count_digit = 0

    for c in chain_of_characters:
        if c.isupper():
            count_upper += 1
        elif c.islower():
            count_lower += 1
        elif c.isdigit():
            count_digit += 1

    return count_upper, count_lower, count_digit


def main():
    chain_of_characters = input("Nhập chuỗi ký tự: ")

    count_upper, count_lower, count_digit = count_characters(chain_of_characters)

    print("Số ký tự in hoa:", count_upper)
    print("Số ký tự in thường:", count_lower)
    print("Số ký tự số:", count_digit)


if __name__ == "__main__":
    main()

