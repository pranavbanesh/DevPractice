import logging
def logr(fname= '', lvl = logging.INFO, timefmt = '%I:%M:%S %p'):
    logFigDict = {}
    logFigDict['filename'] = 'example.log'
    logFigDict['level'] = lvl
    logFigDict['format'] ='%(asctime)s %(message)s' 
    logFigDict['datefmt'] = timefmt
    return logFigDict
    #logging.basicConfig(**logFigDict)