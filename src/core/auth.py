from fastapi import HTTPException, Security, status
from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
)

from src.utils.config import Config

security = HTTPBearer()


class TokenAuth:
    """Handles Bearer token authentication for API requests."""

    def verify_token(self, token: str) -> bool:
        """Validates the provided token against the configured API token.

        Args:
            token: Bearer token received from the request.

        Returns:
            bool: True if the token is valid, otherwise False.
        """
        expected = Config().get("API_TOKEN")

        return token == expected

    async def get_current_token(
        self,
        credentials: HTTPAuthorizationCredentials = Security(security),
    ) -> str:
        """Validates the Bearer token from the Authorization header.

        This dependency is intended to be used with FastAPI's
        dependency injection system. It extracts the token from the
        Authorization header and validates it against the configured
        API token.

        Args:
            credentials: Authorization credentials provided by
                FastAPI's HTTPBearer security scheme.

        Raises:
            HTTPException: If the token is invalid.

        Returns:
            str: The validated Bearer token.
        """

        token = credentials.credentials

        if not self.verify_token(token):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return token


auth = TokenAuth()