from typing import Optional


class Dome9APIException(Exception):

	def __init__(self, message: str, code: Optional[int] = None, content: Optional[str] = None):
		"""d9 custom exception.

		Args:
			message (str): custom exception message.
			code (int): custom exception code
			content (str): custom exception content.
		"""
		super().__init__(message)
		self.code = code
		self.content = content
