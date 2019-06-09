from string_clean import string_clean


def test_string_clean():
    assert string_clean("") == ""
    assert string_clean("! !") == "! !"
    assert string_clean("123456789") == ""
    assert string_clean("(E3at m2e2!!)") == "(Eat me!!)"
    assert string_clean("Dsa32 cdsc34232 csa!!! 1I 4Am cool!") == \
        "Dsa cdsc csa!!! I Am cool!"
    assert string_clean("A1 A1! AAA   3J4K5L@!!!") == "A A! AAA   JKL@!!!"
    assert string_clean("Adgre2321 A1sad! A2A3A4 fv3fdv3J544K5L@") == \
        "Adgre Asad! AAA fvfdvJKL@"

    a = "Ad2dsad3ds21 A  1$$s122ad! A2A3Ae24 f44K5L@222222 "
    assert string_clean(a) == "Addsadds A  $$sad! AAAe fKL@ "

    a = "33333Ad2dsad3ds21 A3333  1$$s122a!d! A2!A!3Ae$24 f2##222 "
    assert string_clean(a) == "Addsadds A  $$sa!d! A!A!Ae$ f## "

    a = "My \"me3ssy\" d8ata issues2! Will1 th4ey ever, e3ver be3 so0lved?"
    b = "My \"messy\" data issues! Will they ever, ever be solved?"
    assert string_clean(a) == b

    a = "Wh7y can't we3 bu1y the goo0d software3? #cheapskates3"
    b = "Why can't we buy the good software? #cheapskates"
    assert string_clean(a) == b
