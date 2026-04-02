# 📦 QR Generator

[![PDF Merge](https://img.shields.io/badge/Language-python-blue?style=for-the-badge)](https://www.python.org/) [![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE) 

Simple 5 line Python script that generates a **QR code** from a string or URL provided by the user via terminal input.

This project is intended as a practical exercise to learn and practice:

- 📚 usage of external Python modules  
- ⌨️ basic input/output handling  
- 🧪 virtual environments (`venv`)  
- 🌱 first steps with Git and GitHub  

---

## ⚙️ Requirements

- 🐍 Python **3.10+**  
- 📦 Python module `qrcode`  
- 🖼️ `Pillow` module (installed automatically)  

---

## 🛠️ Installation (recommended: virtual environment)

```
python3 -m venv venv
source venv/bin/activate
pip install qrcode[pil]
```

## 🧾 Example Usage

- $ python `import_qr_code.py`
- Enter the text or URL to generate the QR code: `https://www.github.com`
- QR code successfully generated and saved as `'qrcode.png'`.
- This will create a QR code image file named qrcode.png in the current directory, which can be scanned by any QR code reader.

---

## 📜 License

MIT License © 2025 `Mirco Negri`
— see [LICENSE](LICENSE) file for details.

---

## 👤 Author

`Mirco Negri`
GitHub: https://github.com/mirconegri
Portfolio: https://mirconegri.github.io/Portfolio/
