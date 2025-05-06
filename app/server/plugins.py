class LoggingPlugin:
    def __init__(self) -> None:
        pass

    def setup_logging(self):
        import logging
        from app.config.plugins import LOGGING_CONFIG

        logging.config.dictConfig(LOGGING_CONFIG)
