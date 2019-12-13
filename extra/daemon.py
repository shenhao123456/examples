"""
Generic linux daemon base class for python 3.x.
"""

import sys
import os
import time
import atexit
import signal
import psutil


class Daemon:
    """
    A generic daemon class.

    Usage: subclass the daemon class and override the run() method.
    """

    def __init__(self, pidfile):
        self.pidfile = pidfile

    def daemonize(self):
        """
        Daemonize class. UNIX double fork mechanism. see Stevens' "Advanced
        Programming in the UNIX Environment" for details (ISBN 0201563177)
        http://www.erlenstar.demon.co.uk/unix/faq_2.html#SEC16
        """

        try:
            pid = os.fork()
            if pid > 0:
                # exit first parent
                sys.exit(0)
        except OSError as e:
            sys.stderr.write('fork #1 failed: {0}\n'.format(e))
            sys.exit(1)

        # decouple from parent environment
        os.chdir("/")
        os.setsid()
        os.umask(0)

        # do second fork
        try:
            pid = os.fork()
            if pid > 0:
                # exit from second parent
                sys.exit(0)
        except OSError as e:
            sys.stderror.write('fork #2 failed: {0}\n'.format(e))

        # redirect standard file descriptors
        sys.stdout.flush()
        sys.stderr.flush()
        si = open(os.devnull, 'r')
        so = open(os.devnull, 'a+')
        se = open(os.devnull, 'a+')

        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        # write pidfile
        # atexit.register(self.delpid)

        pid = str(os.getpid())
        with open(self.pidfile, 'w+') as f:
            f.write(pid + '\n')

    def delpid(self):
        os.remove(self.pidfile)

    def start(self):
        """
        Start the daemon.
        """

        # Check for a pidfile to see if the daemon already runs
        try:
            with open(self.pidfile, 'r') as pf:
                pid = int(pf.read().strip())
        except Exception:
            pid = None

        if pid:
            message = "pidfile {0} already exist. Daemon already running?\n"
            sys.stderr.write(message.format(self.pidfile))
            sys.exit(1)

        # Start the daemon
        self.daemonize()
        self.run()

    def stop(self):
        """
        Stop the daemon.
        """

        # Get the pid from the pidfile
        try:
            with open(self.pidfile, 'r') as pf:
                pid = int(pf.read().strip())
        except IOError:
            pid = None

        if not pid:
            message = "pidfile {0} does not exist. Daemon not running?\n"
            sys.stderr.write(message.format(self.pidfile))
            return  # not an error in a restart

        # Try killing the daemon process
        # get all children process of parent process, and kill them all.
        parent_process = psutil.Process(pid)
        children_process = parent_process.children(recursive=True)
        try:
            for child in children_process:
                child.kill()
                time.sleep(0.1)
        except psutil.NoSuchProcess as e:
            print(e)
        try:

            while 1:
                os.kill(pid, signal.SIGTERM)
                time.sleep(0.1)
        except OSError as e:
            e = str(e.args)
            if e.find("No such process") > 0:
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)
            else:
                print(str(e.args))
                sys.exit(1)

    def restart(self):
        """
        Restart the daemon
        """

        self.stop()
        self.start()

    def run(self):
        """
        You should override this method when you subclass Daemon. It will be called the process has been daemonized by start() or restart().
        """
