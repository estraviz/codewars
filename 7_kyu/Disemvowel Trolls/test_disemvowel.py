from disemvowel import disemvowel


def test_disemvowel():
    tupl = [("This website is for losers LOL!", "Ths wbst s fr lsrs LL!"),
            ("No offense but,\nYour writing is among the worst I've ever read",
             "N ffns bt,\nYr wrtng s mng th wrst 'v vr rd"),
            ("What are you, a communist?", "Wht r y,  cmmnst?")]

    for case in tupl:
        assert disemvowel(case[0]) == case[1]
