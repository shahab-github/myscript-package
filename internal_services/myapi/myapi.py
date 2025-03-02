import logging

logger = logging.getLogger(__name__)


class MyApi:
    def __init__(self):
        pass

    def is_healthy(self):
        logger.info('is_healthy')
        print('is_healthy', True)
