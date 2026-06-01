from types import TracebackType

import mysql.connector
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursorDict

from src.utils.config import Config

class Connections:

    def __init__(self, section: str) -> None:
        self.section = section
        self.conn: MySQLConnection | None = None
        self.cursor: MySQLCursorDict | None = None

    def __enter__(self) -> tuple[MySQLConnection, MySQLCursorDict]:
        """Estabelece a conexão e retorna conexão + cursor do banco.

        Raises:
            ValueError: Seção inválida.
            RuntimeError: Se ocorrer um erro ao conectar ao banco.

        Returns:
            tuple[MySQLConnection, MySQLCursorDict]:
                Conexão e cursor do banco de dados.
        """
        config = Config().config(self.section)

        if isinstance(config, str):
            raise ValueError(config)

        try:
            if self.section in ["fixr"]:
                self.conn = mysql.connector.connect(
                    host=config["host"],
                    user=config["user"],
                    password=config["password"],
                    database=config["database"],
                    port=config["port"],
                    auth_plugin="mysql_native_password",
                    charset="utf8",
                )

                self.cursor = self.conn.cursor(dictionary=True)

            else:
                raise ValueError(f"Seção não suportada: {self.section}")

        except Exception as e:
            raise RuntimeError(
                f"Erro ao conectar ao banco de dados "
                f"{self.section}: {e}"
            ) from e

        return self.conn, self.cursor

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> bool:
        """Fecha o cursor e a conexão com o banco de dados.

        Args:
            exc_type: Tipo da exceção levantada.
            exc_val: Valor da exceção levantada.
            exc_tb: Traceback da exceção.
        """

        if self.cursor is not None:
            try:
                self.cursor.close()
            except Exception:
                pass

        if self.conn is not None:
            try:
                self.conn.close()
            except Exception:
                pass

        if exc_type is not None:
            print(f"Erro ocorrido: {exc_val}")
            print(f"Rastreamento da pilha: {exc_tb}")

        return False