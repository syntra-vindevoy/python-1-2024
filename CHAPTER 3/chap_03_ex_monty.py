def print_right(text):
    text = text.strip()

    assert len(text) <= 40, "Maximum length of text is 40."

    return f"{(40 - len(text)) * ' '}{text}"



