import os

class Config:

    def config(self, section: str) -> dict:
        """Retorna as configurações do banco de dados para a seção.

        Args:
            section (str): Nome da seção de configuração.

        Returns:
            dict: Dicionário com as configurações do banco de dados.
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
                raise ValueError(f"Valor [{section}] inválido!")
