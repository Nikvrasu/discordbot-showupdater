import time

from bot.notifier import Notifier

class Scheduler():

    def __init__(self):
        pass

    # Schedule the check_for_updates function to run every 'time' seconds, pass keys along too
    def schedule(self, keys, timeout):
        notifier = Notifier(keys)
        while True:
            notifier.check_for_updates(keys)
            time.sleep(timeout)