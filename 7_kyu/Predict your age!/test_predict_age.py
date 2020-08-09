from predict_age import predict_age


def test_predict_age():
    assert predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86
