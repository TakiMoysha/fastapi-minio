from dataclasses import dataclass, field
from functools import lru_cache

from app.lib.upcast_env import get_upcast_env


@dataclass
class ServerConfig:
    debug: bool = field(default_factory=lambda: get_upcast_env("SERVER_DEBUG", False))

    cors_origins: list[str] = field(
        default_factory=lambda: get_upcast_env(  # type: ignore
            "SERVER_CORS_ORIGINS_BOOTSTRAP",
            ["http://localhost:3000", "http://localhost:8000", "http://localhost:8080"], # type: ignore
        ),
    )
    cors_methods: list[str] = field(
        default_factory=lambda: get_upcast_env(  # type: ignore
            "SERVER_CORS_METHODS_BOOTSTRAP",
            ["GET", "POST", "PUT", "DELETE", "OPTIONS"], # type: ignore
        ),
    )
    cors_headers: list[str] = field(
        default_factory=lambda: get_upcast_env(  # type: ignore
            "SERVER_CORS_HEADERS_BOOTSTRAP",
            ["*"], # type: ignore
        ),
    )


@dataclass
class MinIOConfig:
    endpoint_url: str = field(default_factory=lambda: get_upcast_env("MINIO_ENDPOINT_URL", "localhost:9000"))
    access_key: str = field(default_factory=lambda: get_upcast_env("MINIO_ACCESS_KEY", "minio"))
    secret_key: str = field(default_factory=lambda: get_upcast_env("MINIO_SECRET_KEY", "minio123"))


@dataclass
class DatabaseConfig:
    host: str = field(default_factory=lambda: get_upcast_env("DB_HOST", "localhost"))
    port: int = field(default_factory=lambda: get_upcast_env("DB_PORT", 5432))
    database: str = field(default_factory=lambda: get_upcast_env("DB_NAME", "fastapi"))
    user: str = field(default_factory=lambda: get_upcast_env("DB_USER", "fastapi"))
    password: str = field(default_factory=lambda: get_upcast_env("DB_PASSWORD", "fastapi"))

    @property
    def url(self):
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


@dataclass
class SAQConfig:
    processes: int = field(default_factory=lambda: get_upcast_env("SAQ_PROCESSES", 1))
    concurrency: int = field(default_factory=lambda: get_upcast_env("SAQ_CONCURRENCY", 10))
    web_enabled: bool = field(default_factory=lambda: get_upcast_env("SAQ_WEB_ENABLED", True))
    use_server_lifespan: bool = field(default_factory=lambda: get_upcast_env("SAQ_USE_SERVER_LIFESPAN", True))


@dataclass
class LoggingConfig:
    level: str = field(default_factory=lambda: get_upcast_env("LOGGING_APP_LEVEL", "INFO"))

    uvicorn_access_level: str = field(default_factory=lambda: get_upcast_env("LOGGING_UVICORN_ACCESS_LEVEL", "INFO"))
    uvicorn_error_level: str = field(default_factory=lambda: get_upcast_env("LOGGING_UVICORN_ERROR_LEVEL", "ERROR"))

    saq_level: str = field(default_factory=lambda: get_upcast_env("LOGGING_SAQ_LEVEL", "INFO"))

    sqlalchemy_level: str = field(default_factory=lambda: get_upcast_env("LOGGING_SQLALCHEMY_LEVEL", "INFO"))


@dataclass
class AppConfig:
    server: ServerConfig = field(default_factory=ServerConfig)
    saq: SAQConfig = field(default_factory=SAQConfig)
    minio: MinIOConfig = field(default_factory=MinIOConfig)
    database: DatabaseConfig = field(default_factory=DatabaseConfig)
    logging: LoggingConfig = field(default_factory=LoggingConfig)


@lru_cache(maxsize=1)
def get_config():
    return AppConfig()
