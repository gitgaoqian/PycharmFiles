# #TEST1：日志配置不从文件中读取，按照时间轮转记录日志
# import logging
# import logging.handlers
# import time
# #logging流程：创建logger记录器、创建handler处理程序、创建formatter格式化程序、日志记录
#
#
# # create logger
# logger = logging.getLogger('simple_example')
# logger.setLevel(logging.DEBUG)
#
# # create console handler and set level to debug
# ch = logging.handlers.TimedRotatingFileHandler(filename="test.log",when='S',interval=30,backupCount=5)
# ch.setLevel(logging.DEBUG)
#
# # create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# # add formatter to ch
# ch.setFormatter(formatter)
#
# # add ch to logger
# logger.addHandler(ch)
#
# # 'application' code
# count=1
# while count < 200:
#     logger.debug('debug message')
#     logger.info('info message')
#     logger.warning('warn message')
#     logger.error('error message')
#     logger.critical('critical message')
#     time.sleep(1)
#     count=count+1

# #TEST2 日志配置从文件中读取
import logging
import logging.config
import logging.handlers
import time

logging.config.fileConfig('logging.conf')
# create logger
logger = logging.getLogger('root')
# 'application' code
count=1
while count < 200:
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')
    time.sleep(1)
    count=count+1