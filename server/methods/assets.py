from server import utils
from server import cache
import config

class Assets():
    @classmethod
    @cache.memoize(timeout=config.cache)
    def list_assets(cls, amount, offset):
        data = utils.make_request("listassets", ["*", False, amount, offset])
        return data

    @classmethod
    def get_asset(cls, name: str):
        data = utils.make_request("getassetdata", [name])
        return data

    @classmethod
    def get_ans(cls, name: str):
        data = utils.make_request("getansdata", [name])
        return data
