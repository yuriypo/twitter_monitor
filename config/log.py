import json

_FORMAT_DEFAULT = {
    "time": "%(asctime)s",
    "level": "%(levelname)s/%(name)s",
    "message": "%(message)s"}

_FORMATTER_DEFAULT = {
    "format": json.dumps(_FORMAT_DEFAULT)
}

_COMMON_FORMATTERS = {
    "default": _FORMATTER_DEFAULT
}

_HANDLER_CONSOLE = {
    "class": "logging.StreamHandler",
    "formatter": "default",
    "level": "DEBUG",
    "filters": []
}


_LOGGER_CONSOLE = {
    "level": "DEBUG",
    "propagate": 0,
    "handlers": ["console"]
}

_COMMON_HANDLERS = {
    "console": _HANDLER_CONSOLE
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
        "HashTagsSummarizer": _LOGGER_CONSOLE
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
        "TwitterStreamer":   _LOGGER_CONSOLE,
        "GraphPresentor":   _LOGGER_CONSOLE,
        "TwitterFollowUpMonitor":   _LOGGER_CONSOLE
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
        "TwitterStreamer":   _LOGGER_CONSOLE,
        "GraphPresentor":   _LOGGER_CONSOLE,
        "TwitterFollowUpMonitor":   _LOGGER_CONSOLE
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