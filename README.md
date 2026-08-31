# DeepOsint 🔍

<p align="center">
  <pre>
  _____                      ____       _       _   
 |  __ \                    / __ \     (_)     | |  
 | |  | | ___  ___ _ __    | |  | | ___ _ _ __ | |_ 
 | |  | |/ _ \/ _ \ '_ \   | |  | |/ __| | '_ \| __|
 | |__| |  __/  __/ |_) |  | |__| |\__ \ | | | | |_ 
 |_____/ \___|\___| .__/    \____/ |___/_|_| |_|\__|
                  | |                               
                  |_|                               
  </pre>
  <i>La herramienta definitiva de agregación OSINT masiva.</i>
</p>

---

## Sobre el Proyecto
**DeepOsint** es un orquestador de inteligencia de fuentes abiertas diseñado para centralizar y automatizar la recolección de datos masivos. Combina la potencia de herramientas consagradas con scripts personalizados de scraping y puentes hacia bots de Telegram.

### Características Principales
* **Multi-Tool Wrapper:** Ejecución integrada de herramientas OSINT populares de GitHub:
  * [Sherlock](https://github.com/sherlock-project/sherlock) y [Maigret](https://github.com/soxoj/maigret) — búsqueda de nombres de usuario en cientos de plataformas.
  * [Toutatis](https://github.com/megadose/toutatis) — inteligencia de perfiles de Instagram.
  * [Holehe](https://github.com/megadose/holehe) y [Socialscan](https://github.com/iojw/socialscan) — verificación de cuentas registradas por email.
  * [theHarvester](https://github.com/laramies/theHarvester) — recolección de subdominios, hosts y correos de un dominio.
* **Telegram Bridge:** Interfaz directa con bots de filtraciones y consultas.
* **Advanced Web Scraping:** Peticiones `curl` personalizadas para evadir bloqueos básicos.
* **Reportes Automáticos:** Exportación de hallazgos en formatos limpios (JSON/TXT).

---

## Autores
Este proyecto es mantenido y desarrollado por:

* [@0xall3x](https://github.com/0xall3x)
* [@veyron92i](https://github.com/veyron92i)

---

## Instalación 
```bash
chmod +x setup.sh
./setup.sh
source venv/bin/activate
```

---

## Uso
```bash
# Investigación de usuario (Sherlock + Maigret [+ Toutatis si pasas --session])
python DeepOsint.py --username <usuario> [--session <sessionid_instagram>]

# Investigación de email (Holehe + Socialscan + Leaks)
python DeepOsint.py --email <email>

# Investigación de dominio (theHarvester: subdominios, hosts, emails)
python DeepOsint.py --domain <dominio.com>
```
