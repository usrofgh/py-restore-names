import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_template():
    return [
        {
            "first_name": None,
            "last_name": "Livesey",
            "full_name": "Doctor Livesey",
        },
        {
            "first_name": None,
            "last_name": "Silver",
            "full_name": "John Silver",
        },
        {
            "last_name": "Pew",
            "full_name": "Blind Pew",
        },
    ]


def test_restore_names(user_template):


    restore_names(user_template)

    assert user_template == [
        {
            "first_name": "Doctor",
            "last_name": "Livesey",
            "full_name": "Doctor Livesey",
        },
        {
            "first_name": "John",
            "last_name": "Silver",
            "full_name": "John Silver",
        },
        {
            "first_name": "Blind",
            "last_name": "Pew",
            "full_name": "Blind Pew",
        },
    ]
