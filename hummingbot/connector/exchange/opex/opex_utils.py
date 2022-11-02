import opex_constants as CONSTANTS


def convert_from_exchange_trading_pair(exchange_trading_pair: str) -> str:
    return exchange_trading_pair.replace("_", "-")


def convert_to_exchange_trading_pair(hb_trading_pair: str) -> str:
    return hb_trading_pair.replace("-", "_")


def get_api_reason(code: str) -> str:
    return CONSTANTS.API_REASONS.get(int(code), code)


def get_rest_url(path_url: str) -> str:
    return f"{CONSTANTS.REST_URL}{path_url}"
