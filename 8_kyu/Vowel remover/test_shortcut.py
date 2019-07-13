import random
from shortcut import shortcut


def test_shortcut_easy():
    for t in [
        ["hello", "hll"],
        ["hellooooo", "hll"],
        ["how are you today?", "hw r y tdy?"],
        ["complain", "cmpln"],
        ["never", "nvr"]
    ]:
        exp, ans = t[0], t[1]
        assert shortcut(exp) == ans


def test_shortcut_not_so_easy():
    for t in [
        ["a e i o u, borriquito como tu", "    , brrqt cm t"],
        ["Explicit is better than implicit", "Explct s bttr thn mplct"],
        ["Beautiful is better than Ugly", "Btfl s bttr thn Ugly"]
    ]:
        exp, ans = t[0], t[1]
        assert shortcut(exp) == ans


def test_shortcut_random():
    for t in random.sample([
        ["We are the Knights who say ni!", "W r th Knghts wh sy n!"],
        ["Nobody expects the Spanish Inquisition!",
            "Nbdy xpcts th Spnsh Inqstn!"],
        ["He's not the messiah. He's a very naughty boy!",
            "H's nt th mssh. H's  vry nghty by!"],
        ["It's just a flesh wound.",
            "It's jst  flsh wnd."],
        ["You don't frighten us, English pig dogs.",
            "Y dn't frghtn s, Englsh pg dgs."],
        ["Mate, this parrot wouldn't VOOM if you put four million volts " +
            "through it!",
            "Mt, ths prrt wldn't VOOM f y pt fr mlln vlts thrgh t!"],
        ["Five is a sufficiently close approximation to infinity.",
            "Fv s  sffcntly cls pprxmtn t nfnty."]
    ], 7):
        exp, ans = t[0], t[1]
        assert shortcut(exp) == ans
