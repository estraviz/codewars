from first_non_repeated import first_non_repeated

tester = (
    "1122321235121222dsfasddssdfa112232123" + "sdfasdfasdf" +
    "1122321235121222dsfasddssdfa112232123sdfasdfasdf112232123" +
    "1122321235121222dsfasddssdfa112232123sdfasdfasdf112232123" +
    "1122321235121222dsfasddssdfa112232123sdfasdfasdf112232123" +
    "1122321235121222dsfasddssdfa112232123sdfasdfasdf112232123" +
    "1122321235121222dsfasddssdfa112232123sdfasdfasdf112232123" +
    "asddssdfa112232123sdfasdfasdf1122z321231122321235121222dsfasddssdf" +
    "1122321235121222dsfasddssdf1122321235121222dsfasddssdf" +
    "1122321235121222dsfasddssdf1122321235121222dsfasddssdf112" +
    "p2321235121222dsfasddssdf1122321235121222dsfasddssdf")


def test_first_non_repeated():
    assert first_non_repeated("test") == 'e'
    assert first_non_repeated("teeter") == 'r'
    assert first_non_repeated("1122321235121222") == '5'
    assert first_non_repeated("rend") == 'r'
    assert first_non_repeated(tester) == 'z'
