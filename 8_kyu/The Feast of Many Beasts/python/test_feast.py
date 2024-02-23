from feast import feast


def test_feast():
    assert feast("great blue heron", "garlic naan") is True
    assert feast("chickadee", "chocolate cake") is True
    assert feast("brown bear", "bear claw") is False
    assert feast("marmot", "mulberry tart") is True
    assert feast("porcupine", "pie") is True
    assert feast("electric eel", "lasagna") is False
    assert feast("slow loris", "salsas") is True
    assert feast("ox", "orange lox") is True
    assert feast("blue-footed booby", "blueberry") is True
