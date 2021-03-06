from scan_techniques.scan_technique import ScanTechnique
import socket

DEFAULT_TIMEOUT = 3  # add support for timeout options


class TCPFullConnect(ScanTechnique):
    name = "TCP Full Connect"
    description = "soon"

    def __init__(self, target):
        super(TCPFullConnect, self).__init__(target)

    def start(self):
        socket.setdefaulttimeout(DEFAULT_TIMEOUT)
        self.in_progress = True
        for p in self.target.ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.connect((self.target.ip_address, p))
            except:  # add more advanced error handling - not all errors mean s is closed
                self.target.results[p] = "closed"
            else:
                self.target.results[p] = "open"

        self.in_progress = False

    def stop(self):
        self.in_progress = False
