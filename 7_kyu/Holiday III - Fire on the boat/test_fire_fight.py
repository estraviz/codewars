from fire_fight import fire_fight


def test_fire_fight():
    tests = [
        [
            "Boat Rudder Mast Boat Hull Water Fire Boat Deck Hull Fire Propeller Deck Fire Deck Boat Mast",
            "Boat Rudder Mast Boat Hull Water ~~ Boat Deck Hull ~~ Propeller Deck ~~ Deck Boat Mast"
        ],
        ["Mast Deck Engine Water Fire", "Mast Deck Engine Water ~~"],
        [
            "Fire Deck Engine Sail Deck Fire Fire Fire Rudder Fire Boat Fire Fire Captain",
            "~~ Deck Engine Sail Deck ~~ ~~ ~~ Rudder ~~ Boat ~~ ~~ Captain"
        ],
    ]

    for inp, exp in tests:
        assert fire_fight(inp) == exp
