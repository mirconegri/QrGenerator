# QR Generator

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

A minimal Python script (~5 lines of core logic) that generates a QR code image from any text or URL provided interactively via the terminal.

This project was built as a practical exercise to learn the basics of external module usage, terminal I/O, virtual environments, and Git/GitHub workflows.

## Features

- Generates a QR code from any string or URL entered via terminal input
- Saves the result as a PNG image (`qrcode.png`) in the current working directory
- Zero configuration — no API keys, accounts, or external services required

## Tech Stack

- **Language:** Python 3.10+
- **Library:** [`qrcode`](https://pypi.org/project/qrcode/) (with the `Pillow` extra for image rendering)

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

## Configuration / Environment

This script does not require any environment variables or configuration files. All input is provided interactively at runtime.

## Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Open a Pull Request describing what you changed and why

For bugs or suggestions, feel free to open an [Issue](https://github.com/mirconegri/QrGenerator/issues).

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

© 2026 Mirco Negri
