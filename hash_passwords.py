# -*- coding: utf-8 -*-
"""
Created on Tue May  2 10:15:03 2023

@author: Gzime
"""

import streamlit_authenticator as stauth

list_of_passwords = [
    'password_benutzer',
    'password_gast',
]

for pw in list_of_passwords:
    hash = stauth.Hasher([pw]).generate()[0]
    print(f'hash for password "{pw}": {hash}')