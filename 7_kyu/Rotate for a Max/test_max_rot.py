from max_rot import max_rot


def test_max_rot():
    assert max_rot(38458215) == 85821534
    assert max_rot(195881031) == 988103115
    assert max_rot(896219342) == 962193428
    assert max_rot(69418307) == 94183076
    assert max_rot(257117280) == 571172802
    assert max_rot(240522578) == 452782025
    assert max_rot(561656824) == 666824515
    assert max_rot(672963486) == 796348662
    assert max_rot(48192242) == 89242412
    assert max_rot(25053359) == 55392035
    assert max_rot(785727925) == 877925752
    assert max_rot(275076894) == 750768942
    assert max_rot(507992495) == 507992495
    assert max_rot(461358517) == 638517415
    assert max_rot(563692037) == 669203753
    assert max_rot(159043701) == 590437011
    assert max_rot(896304934) == 963049348
    assert max_rot(273293210) == 732932102
    assert max_rot(451496516) == 549651641
    assert max_rot(1) == 1
    assert max_rot(16130873362142) == 63873362142110
    assert max_rot(84005278654009) == 84005278654009
    assert max_rot(51564279810300) == 51564279810300
    assert max_rot(12364484492416) == 26484492416134
    assert max_rot(63026816035764) == 63026816035764
    assert max_rot(77910393341241) == 79103933412417
    assert max_rot(88700243816673) == 88700243816673
    assert max_rot(65879065959482) == 65879065959482
    assert max_rot(88361793184682) == 88361793184682
    assert max_rot(91556298303742) == 91556298303742
