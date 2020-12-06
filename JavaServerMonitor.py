from apscheduler.schedulers.background import BackgroundScheduler
import requests


sched = BackgroundScheduler(daemon=True)


def check_java_server_alive():
    status = requests.get("https://meaningfull-insight.herokuapp.com/")
    if status.status_code == 200:
        print("Java server is alive")
    else:
        print("Java server is not responding")


def init_monitor():
    interval = 5 * 60  # Every 5 minutes
    sched.add_job(check_java_server_alive, 'interval', seconds=interval)
    sched.start()
    print("Scheduler for Java server Initialized")
