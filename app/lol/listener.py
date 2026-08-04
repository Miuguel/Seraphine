import subprocess
import logging
import json

import asyncio
from PyQt5.QtCore import QThread, pyqtSignal
import aiohttp

from app.common.logger import logger
from app.common.signals import signalBus
from app.common.util import getLolClientPids, isLolGameProcessExist, getTasklistPath

TAG = "Listener"


class LolProcessExistenceListener(QThread):
    def __init__(self, parent):
        # Current Seraphine connected client pid
        self.runningPid = 0

        super().__init__(parent)

    def run(self):
        path = getTasklistPath()

        if not path:
            signalBus.tasklistNotFound.emit()
            return

        while True:
            # Get all currently running client pids
            pids = getLolClientPids(path)

            # If there are clients running
            if len(pids) != 0:

                # If no client is currently connected, then the first client has started
                if self.runningPid == 0:
                    self.runningPid = pids[0]
                    signalBus.lolClientStarted.emit(self.runningPid)

                # If there is a client running, but the currently connected client is not among them
                # This means it was a multi-client situation, and now the originally connected client has closed,
                # so switch to the new client
                elif self.runningPid not in pids:
                    self.runningPid = pids[0]
                    signalBus.lolClientChanged.emit(self.runningPid)

            # If no clients are running, and there was a client running in the last check
            else:
                if self.runningPid and not isLolGameProcessExist(path):
                    self.runningPid = 0
                    signalBus.lolClientEnded.emit()

            self.msleep(1500)


class StoppableThread(QThread):
    def __init__(self, target, parent) -> None:
        self.target = target
        super().__init__(parent)

    def run(self):
        self.target()
