import os
import sys
current = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(current)
import main.basic.thread.thread_basic
