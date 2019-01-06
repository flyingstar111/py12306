from os import path

# from py12306.helpers.config import Config

# 12306 账号
USER_ACCOUNTS = []

# 查询任务
QUERY_JOBS = []

SEAT_TYPES = {
    '商务座': 32,
    '一等座': 31,
    '二等座': 30,
    '特等座': 25,
    '软卧': 23,
    '硬卧': 28,
    '硬座': 29,
    '无座': 26,
}

# Query
QUERY_DATA_DIR = 'runtime/query'


STATION_FILE = 'data/stations.txt'
CONFIG_FILE = 'env.py'

if path.exists(CONFIG_FILE):
    exec(open(CONFIG_FILE, encoding='utf8').read())


def get(key, default=None):
    return eval(key)