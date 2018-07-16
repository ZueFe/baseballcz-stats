"""
Worker script set on remote server to download data from the page regularly.
"""
from apscheduler.schedulers.blocking import BlockingScheduler
import remote.server.scrape_data as sd

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=23, minute=35, timezone='Europe/Bratislava')
def work_data():
    """
    Schedules job, downloads all data from the page and stores them locally,
    then sends all downloaded data to remote FTP.
    Scheduled to run every day at midnight.
    Uses *BlockingScheduler* class from *APScheduler* library.
    """
    print('Download started')
    sd.download_all()
    sd.send_to_ftp()

sched.start()
