import configparser
import pandas as pd
import loglg
import logging

config = configparser.ConfigParser()
config.read('config.ini')

def prnLog(msg, lvl = 'info'):
    print(lvl.upper() +' : ' + msg)
    eval('logging.'+lvl+'(\''+msg+'\')')
    
for key, _ in config.items('SERIES'):
    ts = config[key]

    start = ts.get('start', config.get('default', 'start'))
    end = ts.get('end', config.get('default', 'end'))
    
    #infer = lambda y, x: dPrinc.index[x] : if y == 'infer'
    #start = infer(start, 0)
    #end = infer(end, -1)
    if 'infer' in [start, end]:
        infer = True
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)
    print(start, end)

    lgrParams = loglg.logr()

    logging.basicConfig(**lgrParams)

    if start > end:
        #start = infer(start, 0)
        #end = infer(end, -1)
        #logging.ERROR('START MUST BE BEFORE END, infering dates from time series')
        prnLog('The end is before the start...we are inferring from time series', 'error')
