from hello_world import HelloWorld


def test_hello_world_no_extra_param():
    assert HelloWorld.main() == "Hello World!"


def test_hello_world_with_one_extra_param():
    assert HelloWorld.main("Javier") == "Hello World Javier!"


def test_hello_world_with_many_extra_param():
    assert HelloWorld.main("Stephen", "Klay", "Draymond", "Kevin", "DeMarcus")\
        == "Hello World Stephen, Klay, Draymond, Kevin, DeMarcus!"
