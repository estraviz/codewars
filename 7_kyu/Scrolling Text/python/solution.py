# Scrolling Text
def scrolling_text(text):
    result = [text := text.upper()]
    for i in range(1, len(text)):
        result.append(text := text[1:] + text[0])
    return result
