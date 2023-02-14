
# import thread
import datetime
# import os
# import sys
# current = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# sys.path.append(current)
# from util import logger_conf as log
import os
import sys
# print(f"before syspath:{sys.path}")
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../', '../')))
# print(f"after syspath:{sys.path}")
from util.logger_conf import logger

nowStr: str = datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
logger.info(f"datetime now:{nowStr}")
# print(f"__name__:{__name__}")