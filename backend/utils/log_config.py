import logging


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename='backend.log'
    )


def get_logger(name):
    return logging.getLogger(name)
