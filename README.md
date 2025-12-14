## 📦 QR Generator

Simple 5 line Python script that generates a **QR code** from a string or URL provided by the user via terminal input.

This project is intended as a practical exercise to learn and practice:

- 📚 usage of external Python modules  
- ⌨️ basic input/output handling  
- 🧪 virtual environments (`venv`)  
- 🌱 first steps with Git and GitHub  

---

## 📂 Repository Contents

- 🐍 `import_qr_code.py` – main script for QR code generation  
- 📄 `README.md` – project documentation  
- 🚫 `.gitignore` – excludes non-versioned files and folders  

---

## ⚙️ Requirements

- 🐍 Python **3.10+**  
- 📦 Python module `qrcode`  
- 🖼️ `Pillow` module (installed automatically)  

---

## 🛠️ Installation (recommended: virtual environment)

```bash
python3 -m venv venv
source venv/bin/activate
pip install qrcode[pil]
