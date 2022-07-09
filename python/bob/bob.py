def response(hey_bob):

    hoi_bob = hey_bob.strip()

    is_question = hoi_bob.endswith("?")
    is_yelled = hoi_bob.isupper()
    is_empty = len(hoi_bob) == 0

    if is_empty:
        bob = "Fine. Be that way!"
    elif is_yelled and is_question:
        bob = "Calm down, I know what I'm doing!"
    elif is_yelled and not is_question:
        bob = "Whoa, chill out!"
    elif is_question:
        bob = "Sure."
    else:
        bob = "Whatever."
    return bob
