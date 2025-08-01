from . import SYSTEM
from ..utils import LOG_DIR, UTILS
from main import ENV_GUNICORN, timestamp

import subprocess, signal, sys

_main_proc = None
_worker_proc = None

execute = UTILS.resolve('exec')
load_env = UTILS.resolve('load_env')


@SYSTEM.register('start_site')
def start_main():
    global _main_proc
    if _main_proc:
        stop_main()

    logfile = LOG_DIR / f"{timestamp()}.log"
    _main_proc = execute(
        ENV_GUNICORN + ['app:app', '-b', f'127.0.0.1:5001', '-k', 'eventlet'],
        env=load_env(),
        stdout=open(logfile, 'w'),
        stderr=subprocess.STDOUT
    )


@SYSTEM.register('stop_site')
def stop_main():
    global _main_proc
    if _main_proc:
        _main_proc.terminate()
        _main_proc = None


@SYSTEM.register('restart_site')
def restart_main(reload: bool = False):
    if _main_proc and reload:
        _main_proc.send_signal(signal.SIGHUP)
        return

    stop_main()
    start_main()


@SYSTEM.register('start_worker')
def start_worker():
    global _worker_proc
    worker_logs = LOG_DIR / "worker"
    worker_logs.mkdir(parents=True, exist_ok=True)
    log_file = worker_logs / f"{timestamp()}.log"
    _worker_proc = execute(
        [sys.executable, 'worker.py'],
        env=load_env(),
        stdout=open(log_file, 'w'),
        stderr=subprocess.STDOUT
    )


@SYSTEM.register('stop_worker')
def stop_worker():
    global _worker_proc
    if _worker_proc:
        _worker_proc.terminate()
        _worker_proc = None


@SYSTEM.register('restart_worker')
def restart_worker():
    stop_worker()
    start_worker()


@UTILS.register('site_status')
def site_online() -> bool:
    return _main_proc is not None and _main_proc.poll() is None


@UTILS.register('worker_status')
def worker_running() -> bool:
    return _worker_proc is not None and _worker_proc.poll() is None
