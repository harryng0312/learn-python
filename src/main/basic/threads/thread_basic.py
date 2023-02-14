# import thread
import datetime
# import os
# import sys
# current = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# sys.path.append(current)
# from util import logger_conf as log
# import os
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../', '../')))
from . import thread_basic
from util import logger_conf as log

nowStr: str = datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
log.logger.info(f"datetime now:{nowStr}")
# print(f"__name__:{__name__}")