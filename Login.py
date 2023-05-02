import streamlit as st
import streamlit_authenticator as stauth
import yaml
import os
import os.path
from yaml.loader import SafeLoader
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
    
    #Authenticator Objekt
    authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
    
name, authentication_status, username = authenticator.login('Login', 'main')





    
     
     
     
if authentication_status:
    authenticator.logout('Logout', 'main')
    if username == 'benutzer':
        st.write(f'Willkommen *{name}*')
        st.title('Alle Funktionen freigeschaltet')
        try:
            os.rename("pages/Leukorechner.txt", "pages/Leukorechner.py")
            os.rename("pages/Funktionsweise.txt", "pages/Funktionsweise.py")
            os.rename("pages/JSON-Daten.txt", "pages/JSON-Daten.py")
            os.rename("pages/Über.txt", "pages/Über.py")
        except (Exception):
            pass
    elif username == 'gast':
        st.write(f'Willkommen *{name}*')
        st.title('Beschränkter Zugriff auf Funktionen')
        try:
            os.rename("pages/Funktionsweise.txt", "pages/Funktionsweise.py")
            os.rename("pages/Über.txt", "pages/Über.py")
        except (Exception):
            pass
      
elif authentication_status == False:
    st.error('Benutzername/Passwort ist falsch')
    try:
        os.rename("pages/Leukorechner.py", "pages/Leukorechner.txt")
        os.rename("pages/Funktionsweise.py", "pages/Funktionsweise.txt")
        os.rename("pages/JSON-Daten.py", "pages/JSON-Daten.txt")
        os.rename("pages/Über.py", "pages/Über.txt")
    except (Exception):
        pass
elif authentication_status == None:
    st.warning('Bitte Benutzernamen und Passwort eingeben') 
    if os.path.isfile("pages/Leukorechner.py"):
        os.rename("pages/Leukorechner.py", "pages/Leukorechner.txt")
    elif os.path.isfile("pages/JSON-Daten.py"):
        os.rename("pages/JSON-Daten.py", "pages/JSON-Daten.txt")
    elif os.path.isfile("pages/Funktionsweise.py"):
        os.rename("pages/Funktionsweise.py", "pages/Funktionsweise.txt")
    elif os.path.isfile("pages/Über.py"):
        os.rename("pages/Über.py", "pages/Über.txt")
    else:
        pass
        
        

    
        

    
 
    
    
    
    
    
   