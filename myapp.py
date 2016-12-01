import logging
import mylib
FORMAT = "%(levelname)s> In %(module)s.%(funcName)s line %(lineno)d at %(asctime)-s> %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
# logger = logging.getLogger(__name__)


def st():
    logging.info('Started')
    mylib.do_something()
    logging.info('Finished')

if __name__ == '__main__':
    st()
