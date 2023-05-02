# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 21:30:54 2023

@author: gzime
"""




# =============================================================================
# -----------------------Leukofit APP-------------------
#   Beschreibung: Diese APP berechnet die Anzhal an weissen Blutzellen.
#    Anhand von Referenzwerten und Eingabewerten, wird das Ergebniss in einem 
#   Balkendiagramm aufgezeigt. Zusätzlich wird die Diagnose erstellt.
#    Datum: 12.04.2023
#    Autoren: Gzime Ramadani, Rinesa Shabija, Priya Jose
# =============================================================================






# Schritt 1: Erstellen der Multipage APP=======================================
#   Es wird eine Multipage APP erstellt. Dieses Python ist die Hauptseite
# =============================================================================

import streamlit as st
st.set_page_config(
    page_title="Leukorechner",
    page_icon="🩸",
)

# Schritt 2: Importieren der Bilbiotheken / Packages===========================
#   Es werden die Bilbiotheken / Packages importiert, welche für
#   die verschiedenen Funktionen benötigt werden (Diagramme, Eingabefelder etc.)
# =============================================================================

import pandas as pd
import matplotlib.pyplot as plt
import json
from datetime import datetime



# Schritt 3: Bild und Titel====================================================
#   Es werden Titel, Header und Bild eingefügt
# =============================================================================
st.title ("Leukorechner")
st.header("Welcome to Leukofit")

from PIL import Image
image = Image.open('media\Blutzellen.jpg')
st.image(image, caption='Leukozyten')




# Schritt 4: Erstellen der Eingabefelder:======================================
#   Es werden die 6 Eingabefelder erstellt.
#   Die Eingabefelder haben den Standardwert 0
# =============================================================================


# Eingabefelder für Blutkörperchenwerte erstellen
Stabkernige_Neutrophile = st.number_input('Stabkernige_Neutrophile', value=0.0, step=0.1)
Segmentkernige_Neutrophile = st.number_input('Segmentkernige_Neutrophile', value=0.0, step=0.1)
Eosinophile = st.number_input('Eosinophile', value=0.0, step=0.1)
Basophile = st.number_input('Basophile', value=0.0, step=0.1)
Monozyten = st.number_input('Monozyten', value=0.0, step=0.1)
Lymphozyten = st.number_input('Lymphozyten', value=0.0, step=0.1)







# Schritt 5: Funktion für Diagramm und JSON====================================
# -----------------------Leukofit APP-------------------
#   Es werden für die Blutzellen Referenzwerte definiert
#   Die Referenzen und Eingabewerte werden in separaten Diagrammen dargestellt.
#   Zusätzlich werden die Balken mit einer Farbskala gefärbt (Rot = Hoch, Grün = Normal, Gelb = Tief)
# =============================================================================

def make_blood_chart(Stabkernige_Neutrophile, Segmentkernige_Neutrophile, Eosinophile, Basophile, Monozyten, Lymphozyten):
    # Referenzwerte
    reference_values = pd.DataFrame({
        'Type': ['Stabkernige_Neutrophile', 'Segmentkernige_Neutrophile', 'Eosinophile', 'Basophile', 'Monozyten', 'Lymphozyten'],
        'Reference Range': [(1,17), (12,67), (0.2,4), (0,1.5), (2,10), (9,33)]
    })

    # User Input
    user_values = pd.DataFrame({
        'Type': ['Stabkernige_Neutrophile', 'Segmentkernige_Neutrophile', 'Eosinophile', 'Basophile', 'Monozyten', 'Lymphozyten'],
        'User Input': [Stabkernige_Neutrophile, Segmentkernige_Neutrophile, Eosinophile, Basophile, Monozyten, Lymphozyten]
   })

    # Definieren der Farben für die Säulen der Diagramme
    colors = ['green' if abs(user_values['User Input'][i] - reference_values['Reference Range'][i][0]) <= 1 or
                         abs(user_values['User Input'][i] - reference_values['Reference Range'][i][1]) <= 1 
              else 'yellow' if abs(user_values['User Input'][i] - reference_values['Reference Range'][i][0]) <= 5 or
                              abs(user_values['User Input'][i] - reference_values['Reference Range'][i][1]) <= 5 
              else 'red' for i in range(len(user_values))]

    # Erstellen der beiden Diagramme
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    # Referenzwerte in das Diagramm einfuegen
    ax1.bar(reference_values['Type'], reference_values['Reference Range'].apply(lambda x: x[1]-x[0]), bottom=reference_values['Reference Range'].apply(lambda x: x[0]))
    ax1.set_xticklabels(reference_values['Type'], rotation=90)
    ax1.set_title('Referenzwerte')

    # User Input aus Eingabefeld in das Diagramm einfuegen und faerben
    ax2.bar(user_values['Type'], user_values['User Input'], color=colors)
    ax2.set_xticklabels(user_values['Type'], rotation=90)
    ax2.set_title('Benutzereingabe')

    # Diagramme anzeigen
    st.pyplot(fig)
    
    
    
    # Schritt 5.1: JSON========================================================
    #   Die Werte der Eingabefelder werden in eine JSON-Datei exportiert.
    # =========================================================================
    
    # Erstellen des Dictionaries mit Variablennamen und ihren Werten
    data = {
        "Zeitstempel": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Stabkernige_Neutrophile": Stabkernige_Neutrophile,
        "Segmentkernige_Neutrophile": Segmentkernige_Neutrophile,
        "Eosinophile": Eosinophile,
        "Basophile": Basophile,
        "Monozyten": Monozyten,
        "Lymphozyten": Lymphozyten,
    }

    # Öffnen der Datei im "append"-Modus und Schreiben des Dictionaries
    with open("blutkörperchen.json", "a") as f:
        json.dump(data, f)
        f.write("\n")  # Fügen Sie eine neue Zeile hinzu, um das Schreiben eines neuen Dictionaries zu trennen

    # Schließen der Datei
    f.close()
    
       
    
    
    
# Schritt 6: Berechnung:=======================================================
# -----------------------Leukofit APP-------------------
#   Anhand den eingegebenen Werten aus den Eingabefeldern,
#   werden die Berechnungen für die Differentialblutkörpererkrankungen (Vergleiche) durchgeführt
# =============================================================================


    # Berechnen und Anzeigen von Differentialblutkörpererkrankungen
    diff = user_values['User Input'] - reference_values['Reference Range'].apply(lambda x: (x[0]+x[1])/2)
    diseases = ['Linksverschibung', 'Pelger_Huet_Anomalie', 'Eosinophilie']
    result = ''
    for i in range(len(diff)):
        if diff[i] > (reference_values['Reference Range'][i][1]-reference_values['Reference Range'][i][0])/2:
            result += f'{diseases[i]} (high)\n'
        elif diff[i] < -(reference_values['Reference Range'][i][1]-reference_values['Reference Range'][i][0])/2:
            result += f'{diseases[i]} (deep)\n'

    st.write('Differential Blood Cell Disease:')
    st.write(result)
    
    
    
    
# Schritt 7: Startknop und Ausführen===========================================
# -----------------------Leukofit APP-------------------
#   Wenn der Startknopf gedrückt wird, wird die Funktion aus Schritt 5
#   ausgeführt. Das Diagramm wird angezeigt und die Daten in die JSON-Datei
#   geschrieben
# =============================================================================

# Startknopf erstellen
if st.button('Start'):
    try:
        make_blood_chart(Stabkernige_Neutrophile, Segmentkernige_Neutrophile, Eosinophile, Basophile, Monozyten, Lymphozyten)  
    except (Exception):
        pass
        st.error('Es kann keine Krankheit angezeigt werden. Die Eingabewerte liegen ausserhalb des Toleranzbereich', icon="❌")


          
        
        
        
        

# Referenzwerte definieren
reference_values = pd.DataFrame({ 'Type': ['Stabkernige_Neutrophile', 'Segmentkernige_Neutrophile', 'Eosinophile', 'Basophile', 'Monozyten', 'Lymphozyten'],
     'Reference Range': [(1,17), (12,67), (0.2,4), (0,1.5), (2,10), (9,33)]
})



# Schritt 8: Berechnung Krankheit:Linksverschiebung============================
#   Die Benutzereingabe wird mit den Referenzen verglichen.
# =============================================================================


# Eingabewerte für Benutzereingabe definieren: Linksverschiebung
user_values = pd.DataFrame({'Type': ['Stabkernige_Neutrophile', 'Segmentkernige_Neutrophile', 'Eosinophile', 'Basophile', 'Monozyten', 'Lymphozyten'],
                           'User Input': [36.5, 41.4, 9.0, 0.0, 5.0, 9.0]})

# Berechnen der Differenz zwischen den vom Benutzer eingegebenen Werten und den Referenzwerten
diff_links = user_values['User Input'] - reference_values['Reference Range'].apply(lambda x: (x[0]+x[1])/2)

# Definieren des Schwellenwerts für Linksverschiebung
threshold_links = (reference_values['Reference Range'][0][1] - reference_values['Reference Range'][0][0]) / 2

# Prüfen für Linksverschiebung
if abs(diff_links[0]) > threshold_links:
    diagnosis_links = "Linksverschiebung"
else:
    diagnosis_links = "No Linksverschiebung"
    
# Diagnose anzeigen fuer Linksverschiebung
print("Diagnosis for Linksverschiebung: ", diagnosis_links) 








# Schritt 9: Berechnung Krankheit:Pelger_Huet_Anomalie=========================
#   Die Benutzereingabe wird mit den Referenzen verglichen.
# =============================================================================

# Eingabewerte für Benutzereingabe definieren: Pelger_Huet_Anomalie
user_values = pd.DataFrame({'Type': ['Stabkernige_Neutrophile', 'Segmentkernige_Neutrophile', 'Eosinophile', 'Basophile', 'Monozyten', 'Lymphozyten'],
                           'User Input': [33.0, 17.0, 5.0, 0.0, 11.0, 33.0]})

# Berechnen der Differenz zwischen den vom Benutzer eingegebenen Werten und den Referenzwerten
diff_ph = user_values['User Input'] - reference_values['Reference Range'].apply(lambda x: (x[0]+x[1])/2)

# Definieren des Schwellenwerts für Pelger_Huet_Anomalie
threshold_ph = (reference_values['Reference Range'][1][1] - reference_values['Reference Range'][1][0]) / 2

# Prüfen für Pelger_Huet_Anomalie
if abs(diff_ph[1]) > threshold_ph:
    diagnosis_ph = "Pelger_Huet_Anomalie"
else:
    diagnosis_ph = "No Pelger_Huet_Anomalie"
    
# Diagnose anzeigen fuer Pelger_Huet_Anomalie
print("Diagnosis for Pelger_Huet_Anomalie: ", diagnosis_ph) 





# Schritt 10: Berechnung Krankheit:Eosinophilie=================================
#   Die Benutzereingabe wird mit den Referenzen verglichen.
# =============================================================================


# Eingabewerte für Benutzereingabe definieren: Eosinophilie
user_values = pd.DataFrame({'Type': ['Stabkernige_Neutrophile', 'Segmentkernige_Netrophile', 'Eosinophile', 'Basophile', 'Monozyten', 'Lymphozyten'],
                               'User Input': [4.0, 18.0, 57.0, 0.0, 8.0, 13.0]})
# Berechnen der Differenz zwischen den vom Benutzer eingegebenen Werten und den Referenzwerten
diff_eo = user_values['User Input'] - reference_values['Reference Range'].apply(lambda x: (x[0]+x[1])/2)

# Definieren des Schwellenwerts für Eosinophilie
threshold_eo = (reference_values['Reference Range'][1][1] - reference_values['Reference Range'][1][0]) / 2

# Prüfen für Eosinophilie
if abs(diff_eo[2]) > threshold_ph:
    diagnosis_eo = "Eosinophilie"
else:
    diagnosis_eo = "No Eosinophilie"
    
# Diagnose anzeigen fuer Eosinophilie
print("Diagnosis for Eosinophilie: ", diagnosis_eo) 








