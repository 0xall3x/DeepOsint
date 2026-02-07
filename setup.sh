#!/bin/bash
echo "[*] Creando entorno virtual..."
python3 -m venv venv
source venv/bin/activate

echo "[*] Actualizando pip e instalando dependencias..."
pip install --upgrade pip
pip install -r requirements.txt

echo "[+] Instalación completada."
