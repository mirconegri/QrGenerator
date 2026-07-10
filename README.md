# QR Generator

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

A minimal Python script (~5 lines of core logic) that generates a QR code image from any text or URL provided interactively via the terminal.

This project was built as a practical exercise to learn the basics of external module usage, terminal I/O, virtual environments, and Git/GitHub workflows.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration and Environment](#configuration-and-environment)
- [Contributing](#contributing)
- [License](#license)

## Features

- Generates a QR code from any string or URL entered via terminal input
- Saves the result as a PNG image (`qrcode.png`) in the current working directory
- Zero configuration — no API keys, accounts, or external services required

## Tech Stack

- **Language:** Python 3.10+
- **Library:** [`qrcode`](https://pypi.org/project/qrcode/) (with the `Pillow` extra for image rendering)

## Project Structure

```
QrGenerator/
├── import_qr_code.py   # Main script — prompts for input and generates the QR code
├── README.md
└── LICENSE
```

## Getting Started

### Prerequisites

- Python 3.10 or later
- `pip`

### Installation

It's recommended to install the dependency inside a virtual environment:

```bash
git clone https://github.com/mirconegri/QrGenerator.git
cd QrGenerator
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install qrcode[pil]
```

## Usage

Run the script and follow the prompt:

```bash
python import_qr_code.py
```

```
Enter the text or URL to generate the QR code: https://www.github.com
QR code successfully generated and saved as 'qrcode.png'.
```

The generated `qrcode.png` file will appear in the same directory and can be scanned by any standard QR code reader.

## Configuration and Environment

This script does not require any environment variables or configuration files. All input is provided interactively at runtime.

## Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Open a Pull Request describing what you changed and why

For bugs or suggestions, feel free to open an [Issue](https://github.com/mirconegri/QrGenerator/issues).

### 👤 Author & Connect

**Mirco Negri** — *Computer Science Student @ UniTrento*

[![Portfolio](https://img.shields.io/badge/Portfolio-00599C?style=for-the-badge&logo=globe&logoColor=white)](https://mirconegri.github.io/Portfolio/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mirconegri)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mirco-negri-263810225)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mirconegri06@gmail.com)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/mirco_negri_?igsh=MWtlbXY0a3R4NTJmNA==)
[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/share/172rhaPCUK/)

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
<br>
© 2026 Mirco Negri
