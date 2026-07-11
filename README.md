# QR Generator

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

A minimal Python CLI utility that generates a QR code image from any text or URL — no external services, no API keys, no configuration required.

Built to address a recurring practical need: sharing links at events and on printed materials without depending on third-party QR generators that may impose rate limits, require sign-ups, or transmit input data to external servers.

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

- Generates a QR code from any string or URL entered via terminal prompt
- Saves the result as `qrcode.png` in the current working directory
- Fully offline — no network calls, no accounts, no rate limits

## Tech Stack

- **Language:** Python 3.10+
- **Library:** [`qrcode`](https://pypi.org/project/qrcode/) with the `Pillow` image backend

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

```bash
git clone https://github.com/mirconegri/QrGenerator.git
cd QrGenerator
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install qrcode[pil]
```

## Usage

```bash
python import_qr_code.py
```

```
Enter the text or URL to generate the QR code: https://github.com/mirconegri
QR code successfully generated and saved as 'qrcode.png'.
```

The output file appears in the working directory and can be scanned by any standard QR reader.

## Configuration and Environment

No environment variables or configuration files are required. All input is provided interactively at runtime.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Open a Pull Request

For bugs or suggestions, open an [Issue](https://github.com/mirconegri/QrGenerator/issues).

### Author

**Mirco Negri** — Computer Science @ UniTrento

[![Portfolio](https://img.shields.io/badge/Portfolio-00599C?style=for-the-badge&logo=globe&logoColor=white)](https://mirconegri.github.io/Portfolio/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mirconegri)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mirco-negri-263810225)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mirconegri06@gmail.com)

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
