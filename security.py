# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 23:17:36 2019

@author: Guz
"""
import keyring

def keyring_get_password(username, program):
    # keyring_impl = keyring.get_keyring()
    # verbose("Note: will use the backend: '{0}'".format(keyring_impl))
    password = keyring.get_password(program, username)
    if not password:
        print("No password found in keychain, please enter it now to store it.")
    return password

def keyring_set_password(username, program):
    # keyring_impl = keyring.get_keyring()
    # verbose("Note: will use the backend: '{0}'".format(keyring_impl))
    print("No password found in keychain, please enter it now to store it.")
    password = input('password:')
    keyring.set_password(program, username, password)

# keyring_set_password('Гузь А.О')
# p =  keyring_get_password('Гузь А.О', '1c')
# print(p)

