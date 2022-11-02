from typing import Dict

from hummingbot.connector.time_synchronizer import TimeSynchronizer
from hummingbot.core.web_assistant.auth import AuthBase
from hummingbot.core.web_assistant.connections.data_types import WSRequest, RESTRequest


class OpexAuth(AuthBase):
    def __init__(self, api_key: str, secret_key: str, time_provider: TimeSynchronizer):
        self.api_key = api_key
        self.secret_key = secret_key
        self.time_provider = time_provider

    async def rest_authenticate(self, request: RESTRequest) -> RESTRequest:
        headers = {}
        if request.headers is not None:
            headers.update(request.headers)
        headers.update(self.header_for_authentication())
        request.headers = headers
        return request

    def header_for_authentication(self) -> Dict[str, str]:
        return {
            "X-API-KEY": self.api_key,
            "X-SECRET-KEY": self.secret_key
        }

    async def ws_authenticate(self, request: WSRequest) -> WSRequest:
        return request  # No websocket for now
