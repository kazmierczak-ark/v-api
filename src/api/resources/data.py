from api.adapters.repositories.data import DataRepository
from api.business_logic.save_data import SaveData
from api.security.jwt.token_info import TokenInfo


def save_data(body, token_info: TokenInfo):
    print(token_info['name'])
    # TODO use authentication token for real
    repo = DataRepository()
    bl = SaveData(repo)
    bl.execute(body)
    return '', 201
