#!/bin/bash
echo "[*] Creando entorno virtual..."
python3 -m venv venv
source venv/bin/activate

echo "[*] Actualizando pip e instalando dependencias..."
pip install --upgrade pip
pip install -r requirements.txt

# El comando 'toutatis' a veces no se registra en el PATH global, 
# pero estará disponible en ./venv/bin/toutatis
echo "[+] Instalación completada."
echo "[!] IMPORTANTE: Antes de ejecutar, usa: source venv/bin/activate"
