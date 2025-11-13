# Practice Login Automation – Python

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.x-green)
![pytest](https://img.shields.io/badge/pytest-9.x-orange)

---

## 🧾 Descripción

Este proyecto es la versión en **Python** del framework de login de práctica que tengo en Java:

➡️ [practice-login-automation (Java + Selenium + Cucumber)](https://github.com/M4R14-N3l0/practice-login-automation)

El objetivo es mostrar cómo automatizar el **login en la web de Practice Test Automation** usando:

- Python  
- Selenium WebDriver  
- pytest  
- Capturas de pantalla automáticas  

---

## 🛠 Tecnologías principales

| Componente | Versión / Detalle |
|-----------|--------------------|
| Lenguaje  | Python 3.13 (recomendado 3.10+) |
| Automatización | Selenium WebDriver 4.x |
| Test runner | pytest 9.x |
| Gestión de dependencias | pip + virtualenv (venv) |
| Navegador | Google Chrome (vía webdriver-manager) |
| Web bajo prueba | https://practicetestautomation.com/practice-test-login/ |

---

## 📁 Estructura del proyecto

```
practice-login-automation-python/
│
├── screenshots/         # Se crea automáticamente con las capturas
├── .venv/               # Entorno virtual (no se sube a Git)
├── conftest.py          # Fixture driver + hook para capturas en fallos
├── test_login.py        # Test de login (escenario positivo por ahora)
└──
```

▶️ Ejecución de pruebas

1. Crear y activar entorno virtual
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate

2. Instalar dependencias
pip install selenium webdriver-manager pytest

3. Ejecutar los tests
pytest -v


Esto:

abre Chrome

realiza el login con student / Password123

valida el login correcto

genera capturas en la carpeta screenshots/

📸 Evidencias

El proyecto genera capturas de pantalla en:

```
screenshots/
  ├── antes_de_hacer_login.png
  ├── login_exitoso.png
  └── test_login_correcto_YYYY-MM-DD_HH-MM-SS.png  # en caso de fallo
```

