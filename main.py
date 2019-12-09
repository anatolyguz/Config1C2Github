
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

test = False

logfile = 'C:/Users/Guz/Config1C2Github/backup_conf.log'

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = logfile)

logging.info("================================") 
logging.info("Запуск скрипта")




pathtocnfig = 'config.ini' 
config = configparser.ConfigParser()
config.read(pathtocnfig)   

githubUrl = config.get('Settings', 'githubUrl')


bin1c = config.get('Settings', 'bin1c')
#База 1С
BASE = config.get('Settings', 'bin1c')

#Користувач 1с, під яким буде здійсено вивантаження
login1с = os.getenv('l1')
password1с = os.getenv('p1')
cmd = bin1c + ' DESIGNER  /F ' + BASE + ' /N ' + login1с + ' /P ' + password1с
  

tmpdir = '/tmp/LTE'
dirfrom1c = '/home/user/xml'
if test:
	if os.path.isdir(tmpdir):
		shutil.rmtree(tmpdir)
	repo = mygit.clone(tmpdir)
	# dir_util.copy_tree(dirfrom1c, tmpdir)
	mygit.add(repo, tmpdir)
	mygit.commit(repo)

else:
    with tempfile.TemporaryDirectory() as tmpdirname:
        print(tmpdirname)
         # Вигрузку бедмо робити у тимчасовий каталог
        repo = mygit.clone(tmpdirname, githubUrl)
        try:
#            q=1
            cmd = cmd + ' /DumpConfigToFiles '+  tmpdirname
            logging.info('Вивартаження конфігурації') 
            c1.BackupConfigToxml(cmd)
#            time.sleep(50)
        except Exception as e:
            logging.error(e)
            logging.error('Завершение работы') 
            print(str(e))
            exit(1)
        try:    
            logging.info('Оновлення локального репозиторію') 
#            if test:
#               testfile = os.path.join(localRepoPath, 'testfile.txt.')
#               with open(testfile, "w") as file:
#                   file.write('just test....')
            mygit.add(repo, tmpdirname, '.')
        except Exception as e:
            logging.error(e)
            logging.error('Завершение работы') 
            print(str(e))
            exit(1)
      
        try:
            logging.info('Комміт....')
            mygit.commit(repo)
        except Exception as e:
            logging.error(e)
            logging.error('Завершение работы') 
            print(str(e))
            exit(1)
            
            

logging.info('Завершение работы') 

print('Hello world')