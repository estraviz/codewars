from weather_info import weather_info


def test_weather_info():
    assert weather_info(56) == '13.33 is above freezing temperature'
    assert weather_info(50) == '10.0 is above freezing temperature'
    assert weather_info(33) == '0.56 is above freezing temperature'
    assert weather_info(23) == '-5.0 is freezing temperature'
    assert weather_info(5) == '-15.0 is freezing temperature'
    assert weather_info(0) == '-17.78 is freezing temperature'
