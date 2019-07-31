from apscheduler.schedulers.blocking import BlockingScheduler
from backup_airtable import backup

sched = BlockingScheduler()

# @sched.scheduled_job('interval', seconds=30)
@sched.scheduled_job('cron', hour=12, timezone='America/New_York')
def backup_table():
    backup()

sched.start()
