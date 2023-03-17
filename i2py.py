import os
import argparse
import threading
import time

parser = argparse.ArgumentParser()
parser.add_argument(
    '-s', '--start',
    dest='start',
    help='default startup sequence',
    action='store_true'
)
parser.add_argument(
    '-R', '--restart',
    dest='restart',
    help='power cycle services',
    action='store_true'
)
parser.add_argument(
    '-K', '--shutdown',
    dest='shutdown',
    help='Shutdown router and kill all other services',
    action='store_true'
)

class i2pd():
    def start():
        print('Starting i2pd service..')
        os.system('i2pd --service')
    def shutdown():
        print(' ')
        os.system('pkill -9 i2pd')
class nginx():
    def start():
        print('Starting nginx web server..')
        os.system('nginx')
    class logfile():
        x = True
        def start():
            time.sleep(5)
            while nginx.logfile.x == True:
                os.system('rm /var/www/i2pd/logfile/logs.txt')
                os.system('tail --lines=80 /var/www/i2pd/logfile/i2pd.log >> /var/www/i2pd/logfile/logs.txt')
                time.sleep(2)
        def shutdown():
            print(' ')
            nginx.logfile.x = False
class extentions():
    def start():
        print('Starting jsonrpc2 plugins..')
        os.system('python3 /var/www/i2pd/run.py/run.py')    
    def shutdown():
        print('Shutting down extentions')
        os.system('pkill -9 /var/www/i2pd/run.py/run.py')

i2pdThread = threading.Thread(target=i2pd.start)
nginxThread = threading.Thread(target=nginx.start)
logfileThread = threading.Thread(target=nginx.logfile.start)
extentionsThread = threading.Thread(target=extentions.start)

def gogo():
    i2pdThread.start()
    nginxThread.start()
    logfileThread.start()
    extentionsThread.start()
def stop():
    i2pd.shutdown()
    nginx.shutdown()
    nginx.logfile.shutdown()
    extentions.shutdown()

args = parser.parse_args()
def init():
    if args.start == True:
        gogo()
    if args.start and args.logfile == True:
        logfileThread.start()
    if args.shutdown == True:
        stop()
    if args.restart == True:
        stop()
        gogo()
