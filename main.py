import datetime
import os

for i in range(0,10):
    filename = datetime.datetime.now().strftime("./%Y-%m-%d.txt")
    with open(filename, 'w') as f:
        f.write(datetime.datetime.now().strftime("%Y-%m-%d"))
        f.write(str(i))
    os.system('git add *')
    os.system('git commit -m "Automated commit"')
    os.system('git push')
