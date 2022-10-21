import configparser

conf = configparser.ConfigParser()
conf.read(filenames="my.cnf")
cf = conf['mysql']




