import subprocess
import os
import shlex
import datetime


bin1c = 'C:/"Program Files"/1cv8/8.3.15.1489/bin/1cv8.exe'
#bin1c = 'c:/"Program Files"/1cv8/common/1cestart.exe'
#C:\Program Files\1cv8\8.3.15.1489\bin



#База 1С
BASE='C:/Users/Guz/Documents/Developer'
#Користувач 1с, під яким буде здійсено вивантаження
login ='ГузьАО'
password = os.getenv('p1')

localPathForBackup = 'C:/Users/Guz/Conf1C2github/xml'
prefix = 'Zorja-Agro'
PathOfLog = 'C:/Users/Guz/Conf1C2github/backup_conf.log'



def backup1c():
  #  NameOfFile =  prefix + datetime.datetime.today().strftime('_%Y-%m-%d__%H%M') + '.dt'
    # FullNameOfFile = localPathForBackup + NameOfFile
   # FullNameOfFile = 'E:/Arhiv/8/Zorja-Agro_2019-12-02__2119.dt'
    # print(FullNameOfFile)
    #cmd = bin1c + ' ENTERPRISE  /F ' + BASE + ' /N ' + login + ' /P ' + password
    cmd = bin1c + ' DESIGNER  /F ' + BASE + ' /N ' + login + ' /P ' + password + ' /Out ' + PathOfLog + ' -NoTruncate /DumpConfigToFiles ' +  localPathForBackup
    print(cmd)
    args = shlex.split(cmd)
    print(args)
    subprocess.run(args, shell=True)
    
    #return FullNameOfFile

try:
    backup1c()
except Exception as e:
    print(str(e))


print('Hello world')