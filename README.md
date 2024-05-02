---
# Konosuba - Test for LFI Vulnerabilities

This Python script is designed to test for Local File Inclusion (LFI) vulnerabilities in web applications. LFI vulnerabilities occur when a web application allows an attacker to include files on the server, potentially leading to the disclosure of sensitive information or remote code execution.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)
- [Example](#example)
- [Output](#output)
- [Disclaimer](#disclaimer)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Local File Inclusion (LFI) is a web vulnerability that allows an attacker to access, view, or include files located on the server in the document root folder. LFI occurs when user-supplied input is not properly validated. Attackers typically manipulate user-controllable input, such as URL parameters or cookies, to specify the file path to include.

## Features

- Test for LFI vulnerabilities in web applications.
- Specify custom headers and cookies.
- Use a customizable wordlist for payload injection.
- Generate a detailed report of potential vulnerabilities.

## Installation

1. Ensure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).
2. Clone this repository to your local machine using Git:
   ```bash
   git clone https://github.com/yourusername/konosuba.git
   ```
3. Navigate to the cloned directory:
   ```bash
   cd konosuba
   ```
4. Install the required Python libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with the following command-line arguments:
```bash
python konosuba.py <URL> [-H HEADERS] [-C COOKIES] [-w WORDLIST] [-t THREADS]
```

## Options

- `<URL>`: The URL of the web application to test for LFI vulnerabilities.
- `-H, --headers`: Optional. Headers in the format `'HeaderName: Value'`. Separate multiple headers with a comma and space.
- `-C, --cookies`: Optional. Cookies in the format `'CookieName=CookieValue'`. Separate multiple cookies with a semicolon and space.
- `-w, --wordlist`: Optional. Path to the wordlist containing LFI payloads. The default is `wordlist.txt`.
- `-t, --threads`: Optional. Number of threads to use for testing (default is 1).

## Example

```bash
python konosuba.py http://example.com -H "User-Agent: Mozilla/5.0" -C "sessionid=abc123" -w mywordlist.txt -t 4
```

## Output

After running the script, potential vulnerable URLs will be saved to the `output.txt` file and all responses will be logged in the console.

## Disclaimer

This script is intended for educational and testing purposes only. Use it responsibly and only on web applications you have permission to test. The authors assume no liability for any misuse or damage caused by this script.

## Contributing

Contributions are welcome! If you find a bug or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

--- 
