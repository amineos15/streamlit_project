#!/bin/bash
# Naviguer au dossier contenant l'application Streamlit
cd $(dirname "$0")

# Lancer l'application Streamlit
streamlit run app.py
