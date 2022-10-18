from distutils.debug import DEBUG
from distutils.log import debug
import logging
import psutil


fd = open("/etc/passwd","r")
#print(type(fd),help(fd.read))
for line in fd:
    print(fd.readlines(3))

    print("next line")
snetio = psutil.net_io_counters()



logging.basicConfig(filename="agent.log",
                    filemode="a",
                    format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d][%(levelname)s] %(message)s',
                    level=logging.DEBUG
                    )
logging.debug("123")
logging.info("dfjek")
logging.error("error")
logging.critical("critical")
print(psutil.net_io_counters())
