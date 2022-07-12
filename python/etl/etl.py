def transform(legacy_data):
    shiny_data = {}
    for item in legacy_data.items():
        score = item[0]
        for letter in item[1]:
            shiny_data[letter.lower()] = score
    return shiny_data
