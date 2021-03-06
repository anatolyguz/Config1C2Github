
import os

import datetime
import logging
import shutil

import configparser
import tempfile
import logging
import time
from  distutils import dir_util
import c1
import mygit
import security


logfile = 'backup_conf.log'

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = logfile)

logging.info("================================") 
logging.info("Запуск скрипта")




pathtocnfig = 'config.ini' 
config = configparser.ConfigParser()
config.read(pathtocnfig)   

githubUrl = config.get('Settings', 'githubUrl')


bin1c = config.get('Settings', 'bin1c')
#База 1С
BASE = config.get('Settings', 'BASE')

#Користувач 1с, під яким буде здійсено вивантаження
login1с = config.get('Settings', 'login1c')
password1с = security.keyring_get_password(login1с, '1c')
cmd = bin1c + ' DESIGNER  /F ' + BASE + ' /N ' + login1с + ' /P ' + password1с
  
test = False
#test = True

tmpdir = 'C:/Users/Guz/AppData/Local/Temp/xml'
tmpdir1 = 'C:\\Users\\Guz\\AppData\\Local\\Temp\\xml'


dirfrom1c = '/home/user/xml'
if test:
    print('test')
    if os.path.isdir(tmpdir):
        mygit.rmdir(tmpdir1)
    repo = mygit.clone(tmpdir, githubUrl)
    time.sleep(20)
    cmd = cmd + ' /DumpConfigToFiles '+  tmpdir
    logging.info('Вивартаження конфігурації') 
    c1.BackupConfigToxml(cmd)
    time.sleep(20)

#    testfile = 'C:/Users/Guz/Config1C2Github/xml/testfile.txt'
#    with open(testfile, "w") as file:
#        file.write('just test....')

#    mygit.add(repo, tmpdir, testfile)
    mygit.add(repo, tmpdir, '.')
    mygit.commit(repo)

else:
    tmpdirname = tempfile.gettempdir()
    tmpdirname = os.path.join( tmpdirname, 'xml')
    print(tmpdirname)
    if os.path.isdir(tmpdirname):
        mygit.rmdir(tmpdirname)
    
    try:
        repo = mygit.clone(tmpdirname, githubUrl)
#        print('clone finish')
    except Exception as e:
        logging.error(e)
        logging.error('Завершение работы') 
        print(str(e))
        exit(1)
        
    try:
        
#        time.sleep(10)
        dirnamefor1c = tmpdirname.replace('\\', '/')
        cmd = cmd + ' /DumpConfigToFiles '+  dirnamefor1c
        logging.info('Вивартаження конфігурації') 
        c1.BackupConfigToxml(cmd)
#        print('Backup finish')
#            time.sleep(50)
    except Exception as e:
        logging.error(e)
        logging.error('Завершение работы') 
        print(str(e))
        exit(1)
    try:    
        logging.info('Оновлення локального репозиторію') 
        mygit.add(repo, tmpdirname, '.')
    except Exception as e:
        logging.error(e)
        logging.error('Завершение работы') 
        print(str(e))
        exit(1)
  
    try:
        logging.info('Комміт....')
        mygit.commit(repo)
#        print('gut')
    except Exception as e:
        logging.error(e)
        logging.error('Завершение работы') 
        print(str(e))
        exit(1)
        
            

logging.info('Завершение работы') 

print('Finish OK!')