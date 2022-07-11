def is_valid(isbn):
    isbn_clean = isbn.replace('-', '')
    # sanity checking ISBN
    if (
        len(isbn_clean) != 10 or
        not set("0123456789").issuperset(isbn_clean[0:9]) or
        not set("0123456789X").issuperset(isbn_clean[-1])
    ):
        return False

    digits = [int(char) for char in isbn_clean[0:9]]
    check_digit = 10 if isbn_clean[-1] == "X" else int(isbn_clean[-1])

    result = (
        (
            digits[0] * 10 +
            digits[1] * 9 +
            digits[2] * 8 +
            digits[3] * 7 +
            digits[4] * 6 +
            digits[5] * 5 +
            digits[6] * 4 +
            digits[7] * 3 +
            digits[8] * 2 +
            check_digit * 1
         ) % 11
    )

    return result == 0
