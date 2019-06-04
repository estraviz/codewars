from correct import correct


def test_correct_simple():
    assert correct("L0ND0N") == "LONDON"
    assert correct("DUBL1N") == "DUBLIN"
    assert correct("51NGAP0RE") == "SINGAPORE"
    assert correct("BUDAPE5T") == "BUDAPEST"
    assert correct("PAR15") == "PARIS"


def test_correct_more():
    a = "1F-RUDYARD K1PL1NG"
    b = "IF-RUDYARD KIPLING"
    assert correct(a) == b

    a = "R0BERT MERLE - THE DAY 0F THE D0LPH1N"
    b = "ROBERT MERLE - THE DAY OF THE DOLPHIN"
    assert correct(a) == b

    a = "R1CHARD P. FEYNMAN - THE FEYNMAN LECTURE5 0N PHY51C5"
    b = "RICHARD P. FEYNMAN - THE FEYNMAN LECTURES ON PHYSICS"
    assert correct(a) == b

    a = "R1CHARD P. FEYNMAN - 5TAT15T1CAL MECHAN1C5"
    b = "RICHARD P. FEYNMAN - STATISTICAL MECHANICS"
    assert correct(a) == b

    a = "5TEPHEN HAWK1NG - A BR1EF H15T0RY 0F T1ME"
    b = "STEPHEN HAWKING - A BRIEF HISTORY OF TIME"
    assert correct(a) == b

    a = "5TEPHEN HAWK1NG - THE UN1VER5E 1N A NUT5HELL"
    b = "STEPHEN HAWKING - THE UNIVERSE IN A NUTSHELL"
    assert correct(a) == b

    a = "ERNE5T HEM1NGWAY - A FARWELL T0 ARM5"
    b = "ERNEST HEMINGWAY - A FARWELL TO ARMS"
    assert correct(a) == b

    a = "ERNE5T HEM1NGWAY - F0R WH0M THE BELL T0LL5"
    b = "ERNEST HEMINGWAY - FOR WHOM THE BELL TOLLS"
    assert correct(a) == b

    a = "ERNE5T HEM1NGWAY - THE 0LD MAN AND THE 5EA"
    b = "ERNEST HEMINGWAY - THE OLD MAN AND THE SEA"
    assert correct(a) == b

    a = "J. R. R. T0LK1EN - THE L0RD 0F THE R1NG5"
    b = "J. R. R. TOLKIEN - THE LORD OF THE RINGS"
    assert correct(a) == b

    a = "J. D. 5AL1NGER - THE CATCHER 1N THE RYE"
    b = "J. D. SALINGER - THE CATCHER IN THE RYE"
    assert correct(a) == b

    a = "J. K. R0WL1NG - HARRY P0TTER AND THE PH1L050PHER'5 5T0NE"
    b = "J. K. ROWLING - HARRY POTTER AND THE PHILOSOPHER'S STONE"
    assert correct(a) == b

    a = "J. K. R0WL1NG - HARRY P0TTER AND THE CHAMBER 0F 5ECRET5"
    b = "J. K. ROWLING - HARRY POTTER AND THE CHAMBER OF SECRETS"
    assert correct(a) == b

    a = "J. K. R0WL1NG - HARRY P0TTER AND THE PR150NER 0F Azkaban"
    b = "J. K. ROWLING - HARRY POTTER AND THE PRISONER OF Azkaban"
    assert correct(a) == b

    a = "J. K. R0WL1NG - HARRY P0TTER AND THE G0BLET 0F F1RE"
    b = "J. K. ROWLING - HARRY POTTER AND THE GOBLET OF FIRE"
    assert correct(a) == b

    a = "J. K. R0WL1NG - HARRY P0TTER AND THE 0RDER 0F PH0EN1X"
    b = "J. K. ROWLING - HARRY POTTER AND THE ORDER OF PHOENIX"
    assert correct(a) == b

    a = "J. K. R0WL1NG - HARRY P0TTER AND THE HALF-BL00D PR1NCE"
    b = "J. K. ROWLING - HARRY POTTER AND THE HALF-BLOOD PRINCE"
    assert correct(a) == b

    a = "J. K. R0WL1NG - HARRY P0TTER AND THE DEATHLY HALL0W5"
    b = "J. K. ROWLING - HARRY POTTER AND THE DEATHLY HALLOWS"
    assert correct(a) == b

    a = "UR5ULA K. LE GU1N - A W1ZARD 0F EARTH5EA"
    b = "URSULA K. LE GUIN - A WIZARD OF EARTHSEA"
    assert correct(a) == b

    a = "UR5ULA K. LE GU1N - THE T0MB5 0F ATUAN"
    b = "URSULA K. LE GUIN - THE TOMBS OF ATUAN"
    assert correct(a) == b

    a = "UR5ULA K. LE GU1N - THE FARTHE5T 5H0RE"
    b = "URSULA K. LE GUIN - THE FARTHEST SHORE"
    assert correct(a) == b

    a = "UR5ULA K. LE GU1N - TALE5 FR0M EARTH5EA"
    b = "URSULA K. LE GUIN - TALES FROM EARTHSEA"
    assert correct(a) == b
