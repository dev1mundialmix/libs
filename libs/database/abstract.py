import os
import cx_Oracle
from .exceptions import DatabaseError, ConnectionError, QueryError

class OracleDatabase():
    def __init__(self, user, password, dns, service_name, port, debug=False):
        self.user = user
        self.password = password
        self.dns = dns
        self.service_name = service_name
        self.port = port
        self.debug = debug
        self.connection = None
        self.cursor = None

        if self.debug:
            current_dir = os.path.dirname(os.path.realpath(__file__))
            cx_Oracle.init_oracle_client(lib_dir=current_dir + "/dll")

    def create_connection(self):
        """Estabelece a conexão com o banco de dados Oracle."""
        try:
            self.connection = cx_Oracle.connect(
                self.user, self.password, f"{self.dns}:{self.port}/{self.service_name}"
            )
            self.cursor = self.connection.cursor()
        except cx_Oracle.Error as e:
            print(f"Oracle Error: {e}")
            raise ConnectionError(f"Failed to connect to the database: {e}")

    def close_connection(self):
        """Fecha a conexão com o banco de dados Oracle."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def execute_query(self, query, **params):
        """Executa uma query no banco de dados Oracle."""
        try:
            self.cursor.execute(query, **params)
            if query.strip().lower().startswith("select"):
                columns = [col[0] for col in self.cursor.description]  # Extrai os nomes das colunas
                result = self.cursor.fetchall()
                return [dict(zip(columns, row)) for row in result]  # Converte o resultado em um dicionário
        except cx_Oracle.Error as e:
            print(f"Oracle Error: {e}")
            raise QueryError(f"Failed to execute query: {e}")

    def commit(self):
        """Faz o commit da transação atual."""
        try:
            if self.connection:
                self.connection.commit()
        except cx_Oracle.Error as e:
            print(f"Oracle Error: {e}")
            raise DatabaseError(f"Failed to commit the transaction: {e}")

    def rollback(self):
        """Faz o rollback da transação atual."""
        try:
            if self.connection:
                self.connection.rollback()
        except cx_Oracle.Error as e:
            print(f"Oracle Error: {e}")
            raise DatabaseError(f"Failed to rollback the transaction: {e}")
        