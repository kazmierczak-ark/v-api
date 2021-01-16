from api.business_logic.models.common import Unauthorized
from api.security.jwt.token_info import TokenInfo


def decode_token(token):
    # TODO decode real token rather than pass dummy info to show security "is there"
    if token == 'bad_guy':
        raise Unauthorized
    else:
        return TokenInfo(name=token)
