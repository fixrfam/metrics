import os

class Config:

    def config(self, section: str) -> dict:
        """Returns the database configuration for the given section.

        Args:
            section (str): Name of the configuration section.

        Returns:
            dict: Dictionary with database configuration values.
        """
        match section:
            case "fixr":
                return {
                    "host": os.getenv("HOST_FIXR"),
                    "port": os.getenv("PORT_FIXR"),
                    "user": os.getenv("USER_FIXR"),
                    "password": os.getenv("PASSWORD_FIXR"),
                    "database": os.getenv("DATABASE_FIXR"),
                }
            case _:
                raise ValueError(f"Invalid value [{section}]!")
