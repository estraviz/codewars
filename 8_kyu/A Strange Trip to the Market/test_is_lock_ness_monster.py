from is_lock_ness_monster import is_lock_ness_monster


def test_is_lock_ness_monster():
    a = "Your girlscout cookies are ready to ship. \
         Your total comes to tree fiddy"
    assert is_lock_ness_monster(a) is True

    a = "Howdy Pardner. Name's Pete Lexington. I reckon you're the kinda \
         stiff who carries about tree fiddy?"
    assert is_lock_ness_monster(a) is True

    a = "I'm from Scottland. I moved here to be with my family sir. Please, \
         $3.50 would go a long way to help me find them"
    assert is_lock_ness_monster(a) is True

    a = "Yo, I heard you were on the lookout for Nessie. Let me know if you \
         need assistance."
    assert is_lock_ness_monster(a) is False

    a = "I will absolutely, positively, never give that darn Lock Ness \
         Monster any of my three dollars and fifty cents"
    assert is_lock_ness_monster(a) is False

    a = "Did I ever tell you about my run with that paleolithic beast? He \
         tried all sorts of ways to get at my three dolla and fitty cent? \
         I told him 'this is MY 4 dolla!'. He just wouldn't listen."
    assert is_lock_ness_monster(a) is False

    a = "Hello, I come from the year 3150 to bring you good news!"
    assert is_lock_ness_monster(a) is False

    a = "By 'tree fiddy' I mean 'three fifty'"
    assert is_lock_ness_monster(a) is True

    a = "I will be at the office by 3:50 or maybe a bit earlier, but \
         definitely not before 3, to discuss with 50 clients"
    assert is_lock_ness_monster(a) is False

    assert is_lock_ness_monster("") is False
