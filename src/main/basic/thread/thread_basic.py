# import thread
import datetime
# import os
# import sys
# current = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# sys.path.append(current)
from util import logger_conf as log


nowStr: str = datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
log.logger.info(f"datetime now:{nowStr}")
# print(sys.path)