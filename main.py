import subprocess
import os
import shlex
import datetime
import logging
import shutil




logfile = 'C:/Users/Guz/Config1C2Github/backup_conf.log'

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = logfile)

logging.info("================================") 
logging.info("Запуск скрипта")



bin1c = 'C:/"Program Files"/1cv8/8.3.15.1489/bin/1cv8.exe'
#bin1c = 'c:/"Program Files"/1cv8/common/1cestart.exe'
#C:\Program Files\1cv8\8.3.15.1489\bin



#База 1С
BASE='C:/Users/Guz/Documents/Developer'
#Користувач 1с, під яким буде здійсено вивантаження
login1с = os.getenv('l1')
password1с = os.getenv('p1')



localPathForBackup = 'C:/Users/Guz/Config1C2Github/xml'



def removeoldxml(path):
    for d in os.listdir(path):
        print(d)
        fullpath = path + '/' + d
        if os.path.isdir(fullpath):
            shutil.rmtree(fullpath)
        else:
            os.remove(fullpath)
   
    
    

def backup1c():
    #Перевырка ыснування каталогу вивантаження.... 
    #якщо нема, то буде згенерована відповідна помилка
#    open(localPathForBackup)
    #Видаляються старі файли
    removeoldxml(localPathForBackup)
    
    
  #  NameOfFile =  prefix + datetime.datetime.today().strftime('_%Y-%m-%d__%H%M') + '.dt'
    # FullNameOfFile = localPathForBackup + NameOfFile
   # FullNameOfFile = 'E:/Arhiv/8/Zorja-Agro_2019-12-02__2119.dt'
    # print(FullNameOfFile)
    #cmd = bin1c + ' ENTERPRISE  /F ' + BASE + ' /N ' + login + ' /P ' + password
    #cmd = bin1c + ' DESIGNER  /F ' + BASE + ' /N ' + login1с + ' /P ' + password1с + ' /Out ' + logfile + ' -NoTruncate /DumpConfigToFiles ' +  localPathForBackup
    cmd = bin1c + ' DESIGNER  /F ' + BASE + ' /N ' + login1с + ' /P ' + password1с + ' /DumpConfigToFiles ' +  localPathForBackup
    print(cmd)
    args = shlex.split(cmd)
    #print(args)
    subprocess.run(args, shell=True)
    
    #return FullNameOfFile

#try:
backup1c()
#except Exception as e:
#    logging.error(e)
#    logging.info("Завершение работы") 
#    exit(1)
#    print(str(e))

logging.info("Завершение работы") 

print('Hello world')