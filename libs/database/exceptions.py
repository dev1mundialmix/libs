class DatabaseError(Exception):
    """Base class for other database-related exceptions."""
    pass

class ConnectionError(DatabaseError):
    """Raised when the database connection fails."""
    pass

class QueryError(DatabaseError):
    """Raised when a query execution fails."""
    pass
