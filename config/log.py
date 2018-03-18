import json

_FORMAT_DEFAULT = {
    "time": "%(asctime)s",
    "level": "%(levelname)s/%(name)s",
    "message": "%(message)s"}

_FORMATTER_DEFAULT = {
    "format": json.dumps(_FORMAT_DEFAULT)
}

_FORMAT_DEFAULT["correlation_id"] = "%(correlation_id)s"

_FORMATTER_CORRELATION_ID = {
    "format": json.dumps(_FORMAT_DEFAULT)
}

_COMMON_FORMATTERS = {
    "default": _FORMATTER_DEFAULT,
    "correlation_id_formatter": _FORMATTER_CORRELATION_ID
}

_HANDLER_CONSOLE = {
    "class": "logging.StreamHandler",
    "formatter": "default",
    "level": "DEBUG",
    "filters": []
}

_HANDLER_CONSOLE_CORRELATION_ID = dict(_HANDLER_CONSOLE, formatter="correlation_id_formatter")


_LOGGER_CONSOLE = {
    "level": "DEBUG",
    "propagate": 0,
    "handlers": ["console"]
}

_LOGGER_CONSOLE_CORRELATION_ID = {
    "level": "DEBUG",
    "propagate": 0,
    "handlers": ["console_correlation_id"]
}

_COMMON_HANDLERS = {
    "console": _HANDLER_CONSOLE,
    "console_correlation_id": _HANDLER_CONSOLE_CORRELATION_ID
}


TEST_LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "default": _FORMATTER_DEFAULT
    },
    "handlers": {
        "console": _HANDLER_CONSOLE
    },
    "loggers": {
        "": _LOGGER_CONSOLE,
        "TwitterStreamListener": _LOGGER_CONSOLE,
        "HashTagsSummarizer": _LOGGER_CONSOLE,
    }
}

DEV_LOGGING_CONFIG = {
    "version": 1,
    "formatters": _COMMON_FORMATTERS,
    "handlers": _COMMON_HANDLERS,
    "loggers": {
        "": _LOGGER_CONSOLE,
        "TwitterStreamListener":_LOGGER_CONSOLE,
        "HashTagsSummarizer":   _LOGGER_CONSOLE,
    }
}

PROD_LOGGING_CONFIG = {
    "version": 1,
    "formatters": _COMMON_FORMATTERS,
    "handlers": _COMMON_HANDLERS,
    "loggers": {
        "":                     _LOGGER_CONSOLE,
        "tornado.access":       _LOGGER_CONSOLE,
        "tornado.application":  _LOGGER_CONSOLE,
        "tornado.general":      _LOGGER_CONSOLE,
        "TwitterStreamListener":_LOGGER_CONSOLE,
        "HashTagsSummarizer":   _LOGGER_CONSOLE,
        "AliasesHandler":       _LOGGER_CONSOLE_CORRELATION_ID
    }
}

CONFIGURATIONS = {
    "PROD": PROD_LOGGING_CONFIG,
    "DEV":  DEV_LOGGING_CONFIG,
    "TEST": TEST_LOGGING_CONFIG
}


def configure_logging():
    from config.env import ENV_TYPE
    from config.log import CONFIGURATIONS

    from logging import config
    config.dictConfig(CONFIGURATIONS[ENV_TYPE])