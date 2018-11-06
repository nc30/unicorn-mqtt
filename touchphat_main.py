#! /usr/bin/env python3
from logging import getLogger
logger = getLogger('touchphat_mqtt_controller')

from logging import Formatter, StreamHandler, INFO
import sys
import os

logger.setLevel(INFO)
handler = StreamHandler(stream=sys.stdout)
handler.setFormatter(
    Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
)
logger.addHandler(handler)

from touchphat_mqtt_controller import main
import signal

if __name__ == '__main__':
    try:
        main()
        signal.pause()

    except KeyboardInterrupt:
        pass

    except Exception as e:
        logger.exception(e)
        raise e

    finally:
        logger.info('stopping...')
        sys.stdout.write("bye.\n")
