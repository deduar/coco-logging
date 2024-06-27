# import atexit
import yaml
# import json
import logging.config
import logging.handlers
import pathlib

from envyaml import EnvYAML

logger = logging.getLogger("my_app")  # __name__ is a common choice


def setup_logging():
    env = EnvYAML('logging_configs/3-homework-filtered-stdout-stderr.yaml')
    
    # config_file = pathlib.Path("logging_configs/3-homework-filtered-stdout-stderr.yaml")
    # with open(file=config_file, mode="r", encoding="utf-8") as f_in:
    #     config = yaml.safe_load(f_in)
    #     # config = json.load(f_in)

    config = env.__dict__['_EnvYAML__cfg']

    logging.config.dictConfig(config)
    # # queue_handler = logging.getHandlerByName("queue_handler")
    # # if queue_handler is not None:
    # #     queue_handler.listener.start()
    # #     atexit.register(queue_handler.listener.stop)


def main():
    setup_logging()
    logging.basicConfig(level="INFO")
    logger.debug("debug message", extra={"x": "hello"})
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("exception message")


if __name__ == "__main__":
    main()
