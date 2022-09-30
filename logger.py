from datetime import date, datetime as dt
from time import time

def result_logger(oper, res, a, b):
    time = dt.now().strftime('%H:%M')
    with open ('log.txt', 'a') as file:
        file.write('{}: {} {} {} = {}\n'
                    .format(time, a, oper, b, res))