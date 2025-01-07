def are_you_playing_banjo(name):
    return (
        "{} plays banjo".format(name)
        if name.upper()[0] == "R"
        else "{} does not play banjo".format(name)
    )
