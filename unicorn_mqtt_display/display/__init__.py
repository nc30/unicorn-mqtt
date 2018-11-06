from logging import getLogger
logger = getLogger(__name__)

import unicornhathd
import time

width, height = unicornhathd.get_shape()

from .clock import loop as clock_loop
from .weather import loop as weather_loop

from threading import Thread, Event

event = Event()
driver = None

def change(mode):
    if mode not in ('clock', 'weather'):
        logger.warn('invalid mode (%s)', mode)
        return False

    logger.debug('get change call to "%s"', mode)

    func = None
    if mode == 'clock':
        func = clock_loop
    elif mode == 'weather':
        func = weather_loop
    else:
        logger.error('cant get function.')
        return False

    event.set()
    time.sleep(1)
    event.clear()

    driver = Thread(target=func, args=(event,))
    driver.daemon = True
    driver.start()

    logger.debug('change sequence is end.')
    return True

def start():
    logger.debug('display initial function start.')
    change('clock')

def end():
    event.set()
    time.sleep(1)
    unicornhathd.off()
