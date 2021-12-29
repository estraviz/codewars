# Safen User Input Part I - htmlspecialchars
def html_special_chars(data):
    convertions = {
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        '&': '&amp;',
    }
    return "".join(convertions.get(c, c) for c in data)
