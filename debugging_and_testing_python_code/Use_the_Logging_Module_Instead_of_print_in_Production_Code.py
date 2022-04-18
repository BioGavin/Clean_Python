import logging
import logging.config

f = "%(asctime)s|%(levelname)-8s|%(filename)s:%(lineno)s|%(message)s"


def intro1():
    # logging 日志级别：debug, info, warning, error, critical.
    # logging 默认的日志级别是warning.
    # 使用baseConfig()来指定日志输出级别
    print("this is print log")
    logging.basicConfig(level=logging.DEBUG, filename='demo.log', filemode='w')
    logging.debug("this is debug log")
    logging.info("this is info log")
    logging.warning("this is warning log")
    logging.error("this is error log")
    logging.critical("this is critical log")


def intro2():
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("姓名 %s, 年龄 %d", "张三", 18)
    logging.debug("姓名 %s, 年龄 %d" % ("张三", 18))
    logging.debug("姓名 {}, 年龄 {}".format("张三", 18))
    logging.debug(f"姓名 {'张三'}, 年龄 {18}")
    logging.basicConfig(format=f, level=logging.DEBUG, datefmt="%Y-%m-%d %H:%M:%S")
    logging.debug("姓名 %s, 年龄 %d", "张三", 18)


def intro3():
    # 编程方式实现高级写法
    # 记录器
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # print(logger)

    # 处理器
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)
    # print(consoleHandler)
    fileHandler = logging.FileHandler(filename='addDemo.log', mode='w')
    fileHandler.setLevel(logging.DEBUG)
    # print(fileHandler)

    # 格式化器
    formatter = logging.Formatter(f)

    # 给处理器设置格式
    consoleHandler.setFormatter(formatter)
    fileHandler.setFormatter(formatter)

    # 给记录器设置处理器
    logger.addHandler(consoleHandler)
    logger.addHandler(fileHandler)

    # 定义过滤器
    flt = logging.Filter("cn.ccb")
    # 关联过滤器
    logger.addFilter(flt)

    # 打印日志
    logger.debug("this is debug log")
    logger.info("this is info log")
    logger.warning("this is warning log")
    logger.error("this is error log")
    logger.critical("this is critical log")


def intro4():
    # 使用配置文件
    logging.config.fileConfig('logging.conf')  # 载入配置文件
    rootlogger = logging.getLogger()
    apploglogger = logging.getLogger('applog')
    rootlogger.debug("this is root debug.")
    apploglogger.debug("this is applog debug.")
    try:
        int('q')
    except Exception as e:
        rootlogger.exception(e)


def intro5():
    # 使用字典配置
    logging.config.dictConfig({"loggers": "applog"})
    logger = logging.getLogger("applog")
    print(logger)


if __name__ == '__main__':
    intro5()
