import pytest
from gen import Generator
from unittest.mock import patch


@patch('gen.Generator.fetch_words')
def test_mocked_fetch(mock_fetch, generator):
    # Simulate the API returning only one known word
    mock_fetch.return_value = ['bivouac']

    username = generator.generate_human_readable_username(7)

    assert isinstance(username, str)
    assert len(username) >= 7
    assert generator.is_readable(username)


@pytest.fixture
def generator():
    return Generator()


def test_generate_random_username_length(generator):
    username = generator.generate_username(8)
    assert isinstance(username, str)
    assert len(username) == 8
    assert all(c.isalnum() for c in username)


def test_generate_human_readable_username(generator):
    length = 5
    username = generator.generate_human_readable_username(length)
    assert isinstance(username, str)
    assert len(username) >= length


def test_human_readable_username_is_readable(generator):
    username = generator.generate_human_readable_username(6)
    assert generator.is_readable(
        username), f"Username not readable: {username}"


def test_human_username_starts_and_ends_with_letter(generator):
    username = generator.generate_human_readable_username(6)
    assert username[0].isalpha(), "Username should start with a letter"
    assert username[-1].isalpha(), "Username should end with a letter"


def test_no_repeated_specials(generator):
    username = generator.generate_username(6)
    specials = "!@#$%^&*()_-+=<>?/|\\~`"
    for i in range(1, len(username)):
        assert not (username[i] in specials and username[i] == username[i - 1]), \
            f"Username has repeated special characters: {username}"
