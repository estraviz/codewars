import pytest

from solution import validate


data_ok = [
    ('Timmy', 'password', 'Successfully Logged in!'),
    ('Alice', 'alice', 'Successfully Logged in!'),
]


@pytest.mark.parametrize(
    "username, password, result", data_ok
)
def test_should_succesfully_login(username, password, result):
    assert validate(username, password) == result


data_pwd_wrong = [
    ('Timmy', 'h4x0r', 'Wrong username or password!'),
]


@pytest.mark.parametrize(
    "username, password, result", data_pwd_wrong
)
def test_should_detect_wrong_password(username, password, result):
    assert validate(username, password) == result


data_injected_code = [
    ('Timmy', 'password"||""=="', 'Wrong username or password!'),
    ('Admin', 'gs5bw"||1==1//', 'Wrong username or password!'),
]


@pytest.mark.parametrize(
    "username, password, result", data_injected_code
)
def test_should_fail_to_login_due_to_injected_code(username, password, result):
    assert validate(username, password) == result
