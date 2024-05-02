---
# Konosuba - Test for LFI Vulnerabilities

This Python script is designed to test for Local File Inclusion (LFI) vulnerabilities in web applications. LFI vulnerabilities occur when a web application allows an attacker to include files on the server, potentially leading to the disclosure of sensitive information or remote code execution.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)
- [Advanced Usage](#AdvanceUsage)
- [Example](#example)
- [Output](#output)
- [Testing](#Testing)
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
   git clone https://github.com/albertisaac12/Konosuba.git
   ```
3. Navigate to the cloned directory:
   ```bash
   cd Konosuba
   ```
4. Install the required Python libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with the following command-line arguments:
```bash
python3 konosuba.py <URL> [-H HEADERS] [-C COOKIES] [-w WORDLIST] [-t THREADS]
```

## Options

- `-h, --help`: Prompts the Help Section.
- `<URL>`: The URL of the web application to test for LFI vulnerabilities.
- `-H, --headers`: Optional. Headers in the format `'HeaderName: Value'`. Separate multiple headers with a comma and space.
- `-C, --cookies`: Optional. Cookies in the format `'CookieName=CookieValue'`. Separate multiple cookies with a semicolon and space.
- `-w, --wordlist`: Optional. Path to the wordlist containing LFI payloads. The default is `wordlist.txt`.
- `-t, --threads`: Optional. Number of threads to use for testing (default is 1).

- NOTE1: The number of threads and wordlists must match example, if -w are wordlist1.txt wordlist2.txt then, -t must be 2.  [ -w <worlist1> <wordlist2> -t 2 ]
- NOTE2: The number of output files generated will be equal to the number of wordlists provided.

<div style="text-align:center">
    <img src="https://github.com/albertisaac12/Konosuba/assets/91803132/cc0052aa-be82-4e1a-899c-09a78ec6d560">
  </div>

## AdvanceUsage

Simple Usgae:
```bash
python3 konosuba.py <URL>
```

Usage with Cookies:
```bash
python3 konosuba.py -C '<Cookie>' <URL>
```

Usage with Header and Cookies:
```bash
python3 konosuba.py -H <header> -C '<Cookie>' <URL>
```

Usage with Multiple word-lists with mandatory threading:
```bash
python3 konosuba.py -H <header> -C '<Cookie>' -w <wordlit1.txt> <wordlist2.txt> -t <thread number equal to number of wordlist> <URL>
```

## Example

```bash
python3 konosuba.py -H "User-Agent: Mozilla/5.0" -C "sessionid=abc123" -w mywordlist.txt -t 1 http://example.com
```

## Output

After running the script, potential vulnerable URLs will be saved to the `output.txt` file and all responses will be logged in the console.

## Testing

- Lab setup: dependencies=> docker 
  ```bash
  docker run --rm -it -p 8080:80 vulnerables/web-dvwa
  ```
  <div style="text-align:center">
    <img src="https://github.com/albertisaac12/Konosuba/assets/91803132/9bd542ef-16b0-4e3d-874d-f16d30b282bc" alt="Step 1">
  </div>
  
- Accessing the DVWA: http://localhost:8080 , click on the File Inclusion section.

   <div style="text-align:center">
    <img src="https://github.com/albertisaac12/Konosuba/assets/91803132/10fee3ac-f69e-456a-8901-63d16d1e0e19" alt="Step 2">
  </div>

- Open Burp Suite and capture the request, the User-Agent will be used inside the header option -H, and Cookie will be passed into the -C option
  - NOTE: The tool is still a work in progress and can be further refined -H option may not work all the time.

    <div style="text-align:center">
    <img src="https://github.com/albertisaac12/Konosuba/assets/91803132/f2c55fb3-a23f-48c5-b64c-1b70369da939" alt="Step 3">
  </div>
  
-Run the following command to start the test, I am using two wordlists for the test.
  ```bash
  python3 Konosuba.py -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0' -C 'Cookie: language=en; welcomebanner_status=dismiss; PHPSESSID=is2js1hklvdq9dpje2kklj9eb3; security=low' -w wordlist.txt wordlist2.txt -t 2 http://localhost:8080/vulnerabilities/fi/?page=
  ```
- The output of the test is as shown in the image below.

<div style="text-align:center">
    <img src="https://github.com/albertisaac12/Konosuba/assets/91803132/8ba21fe6-b9b5-4b8f-89ec-c62ce35e2904" alt="Step 4">
  </div>

-There will be two files generated namely "output_1.txt" and "output_2.txt"

<div style="text-align:center">
    <img src="https://github.com/albertisaac12/Konosuba/assets/91803132/867af715-bf0b-476c-8643-8194bb066466" alt="Step 5">
  </div>
  
-Each File will contain the URLs for the LFI found.
  <div style="text-align:center">
    <img src="https://github.com/albertisaac12/Konosuba/assets/91803132/cac8f988-77f2-4519-8a75-39e8a6f5c396" alt="Step 6">
  </div>

- Accessing the URL generated by the Tool

  <div style="text-align:center">
    <img src="https://github.com/albertisaac12/Konosuba/assets/91803132/da91ca7e-d876-489a-8e94-0a1d712b7896" alt="Step 7">
  </div>

## Disclaimer

This script is intended for educational and testing purposes only. Use it responsibly and only on web applications you have permission to test. The authors assume no liability for any misuse or damage caused by this script.

## Contributing

Contributions are welcome! If you find a bug or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

--- 
