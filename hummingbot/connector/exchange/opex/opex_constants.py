from hummingbot.core.api_throttler.data_types import RateLimit

EXCHANGE_NAME = "Opex"
REST_URL = "https://dev.opex.dev"

# Rest API endpoints
GET_ORDER_BOOK_PATH_URL = "/api/v3/depth"
GET_TICKER_PATH_URL = "/api/v3/ticker"
CREATE_ORDER_PATH_URL = "/api/v3/order"
CANCEL_ORDER_PATH_URL = "/api/v3/order"
GET_ACCOUNT_SUMMARY_PATH_URL = "/private/get-account-summary"
GET_ORDER_DETAIL_PATH_URL = "/private/get-order-detail"
# GET_OPEN_ORDERS_PATH_URL = "/private/get-open-orders"

RATE_LIMITS = [
    # RateLimit(limit_id=GET_TRADING_RULES_PATH_URL, limit=100, time_interval=1),
    RateLimit(limit_id=CREATE_ORDER_PATH_URL, limit=30, time_interval=0.1),
    RateLimit(limit_id=CANCEL_ORDER_PATH_URL, limit=30, time_interval=0.1),
    RateLimit(limit_id=GET_ACCOUNT_SUMMARY_PATH_URL, limit=5, time_interval=0.1),
    RateLimit(limit_id=GET_ORDER_DETAIL_PATH_URL, limit=30, time_interval=0.1),
    # RateLimit(limit_id=GET_OPEN_ORDERS_PATH_URL, limit=3, time_interval=0.1),
    RateLimit(limit_id=GET_ORDER_BOOK_PATH_URL, limit=100, time_interval=1),
    RateLimit(limit_id=GET_TICKER_PATH_URL, limit=100, time_interval=1),
]

API_REASONS = {}
