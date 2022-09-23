import softest
import logging


class Utility(softest.TestCase):

    def softassert(self, actual, expected):
        return self.soft_assert(self.assertEqual(actual, expected, msg=f'Actual text: {actual} is not same as Expected text: {expected}'))

    def _loggers(self, loglevel=logging.DEBUG):
        logger = logging.getLogger(__name__)
        logger.setLevel(loglevel)
        ch = logging.StreamHandler()
        fh = logging.FileHandler(filename='demologger.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        logger.addHandler(ch)
        logger.addHandler(fh)
        return logger