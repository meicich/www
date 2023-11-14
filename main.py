import schedule
import time
import datetime
import os

def job():
    filename = datetime.datetime.now().strftime("./%Y-%m-%d.txt")
    with open(filename, 'w') as f:
        f.write(datetime.datetime.now().strftime("%Y-%m-%d"))
    os.system('git add *')
    os.system('git commit -m "Automated commit"')
    os.system('git push')

schedule.every().day.at("00:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


