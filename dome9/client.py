from typing import Dict, Any, Union, Optional

import requests
from urllib.parse import urljoin
from requests.auth import HTTPBasicAuth

from dome9.consts import RequestMethods
from dome9.exceptions import Dome9APIException
from dome9.statics import Statics


class Client:

	_DEFAULT_SITE = 'https://api.dome9.com/v2/'
	_DEFAULT_FORMAT = 'application/json'
	_HTTP_OK_RANGE = range(200, 299)

	def __init__(self, apiKey: str, apiSecret: str, baseURL: str = _DEFAULT_SITE):
		"""initializes a d9 SDK object.

		Args:
			apiKey (str): API key.
			apiSecret (str): API secret.
			baseURL (str): Origin of API (URL). Defaults to 'https://api.dome9.com/v2/'.
		"""

		Statics.checkIsUUID(apiKey)
		Statics.checkOnlyContainsLowercaseAlphanumeric(apiSecret)
		Statics.checkIsHTTPURL(baseURL)

		self._baseURL = baseURL
		self._clientAuth = HTTPBasicAuth(apiKey, apiSecret)

	def _request(self, method: RequestMethods, route: str, body: Any = None, params: Optional[Dict[str, Union[str, int]]] = None) -> Any:
		url = urljoin(self._baseURL, route)
		headers = {'Accept': Client._DEFAULT_FORMAT, 'Content-Type': Client._DEFAULT_FORMAT}

		try:
			response = getattr(requests, method.value)(url=url, json=body, params=params, headers=headers, auth=self._clientAuth)
		except requests.ConnectionError as connectionError:
			raise Dome9APIException(f'{url} {connectionError}')

		if response.status_code not in Client._HTTP_OK_RANGE:
			raise Dome9APIException(message=response.reason, code=response.status_code, content=response.content)

		if response.content:
			try:
				jsonResponse = response.json()

				return jsonResponse

			except ValueError as valueError:
				raise Dome9APIException(message=str(valueError), code=response.status_code, content=response.content)
