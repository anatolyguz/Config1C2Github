# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:40:32 2019

@author: Guz
"""
import os
import shlex
import subprocess
import shutil




def removeoldxml(path):
    for d in os.listdir(path):
        print(d)
        fullpath = path + '/' + d
        if os.path.isdir(fullpath):
            shutil.rmtree(fullpath)
        else:
            os.remove(fullpath)
   


def BackupConfigToxml(cmd):
    #Перевырка ыснування каталогу вивантаження.... 
    #якщо нема, то буде згенерована відповідна помилка
#    open(localPathForBackup)
    #Видаляються старі файли
#    removeoldxml(localPathForBackup)
    
    print(cmd)
    args = shlex.split(cmd)
    #print(args)
    subprocess.run(args, shell=True)
    
    #return FullNameOfFile
