import pytest

from api.security.jwt.decoder import decode_token, Unauthorized


def test_decode_token_valid_then_provide_claim(mocker):
    token = mocker.sentinel.token
    claim = decode_token(token)

    assert claim['name'] == mocker.sentinel.token


def test_decode_token_invalid_then_throw_unauthorized():
    token = 'bad_guy'

    with pytest.raises(Unauthorized):
        decode_token(token)
