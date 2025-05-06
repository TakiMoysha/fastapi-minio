from .base import get_config

config = get_config()

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(asctime)s %(levelprefix)s <%(name)s>: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",  # stderr
        },
    },
    "loggers": {
        "uvicorn.error": {
            "handlers": ["default"],
            "level": config.logging.uvicorn_error_level,
            "propagate": False,
        },
        "uvicorn.access": {
            "handlers": ["default"],
            "level": config.logging.uvicorn_access_level,
            "propagate": False,
        },
        "": {
            "handlers": ["default"],
            "level": config.logging.level,
            "propagate": False,
        },
    },
}
