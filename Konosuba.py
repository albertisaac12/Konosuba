import requests
import argparse
import sys
import threading
import time

# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
ENDC = '\033[0m'

__version__ = "1.0"
__author__ = "0xbiohazard.unstopabble[ENS]"

def get_response_info(url, headers=None, cookies=None):
    try:
        response = requests.get(url, headers=headers, cookies=cookies)
        return response.content, len(response.content), response.status_code
    except requests.RequestException:
        return None, 0, 0

def test_lfi(url, wordlist, output_file, headers=None, cookies=None):
    try:
        with open(wordlist, 'r') as f:
            payloads = f.readlines()
    except FileNotFoundError:
        print(f"{RED}[!] Wordlist file not found: {wordlist}{ENDC}")
        return

    print(f"{GREEN}[*] Testing for LFI vulnerabilities using {wordlist}...{ENDC}")

    # Get baseline response info
    baseline_content, baseline_length, baseline_status = get_response_info(url, headers, cookies)

    with open(output_file, "w") as output_file:
        for payload in payloads:
            payload = payload.strip()
            test_url = url + payload
            try:
                # Get response info with payload
                payload_content, payload_length, payload_status = get_response_info(test_url, headers, cookies)
                if payload_status == 200 and (payload_length != baseline_length or payload_content != baseline_content):
                    print(f"{GREEN}[+] Potential LFI vulnerability found: {test_url}{ENDC}")
                    output_file.write(f"Potential LFI vulnerability found: {test_url}\n")
                else:
                    print(f"{YELLOW}[-] Not vulnerable: {test_url}{ENDC}")
            except requests.RequestException:
                print(f"{RED}[!] Error occurred while testing: {test_url}{ENDC}")

def run_tests_in_threads(url, headers=None, cookies=None, wordlists=["wordlist.txt"], num_threads=1):
    threads = []
    for i, wordlist in enumerate(wordlists):
        output_file = f"output_{i+1}.txt"  # Output file name for each thread
        thread = threading.Thread(target=test_lfi, args=(url, wordlist, output_file, headers, cookies))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    # Cool ASCII art
    peach_art = """                                                                                           
       ,--.                                                                                
   ,--/  /|                                                                                
,---,': / '                                                          ,---,                 
:   : '/ /   ,---.        ,---,    ,---.                       ,--,,---.'|                 
|   '   ,   '   ,'\   ,-+-. /  |  '   ,'\   .--.--.          ,'_ /||   | :                 
'   |  /   /   /   | ,--.'|'   | /   /   | /  /    '    .--. |  | ::   : :      ,--.--.    
|   ;  ;  .   ; ,. :|   |  ,"' |.   ; ,. :|  :  /`./  ,'_ /| :  . |:     |,-.  /       \   
:   '   \ '   | |: :|   | /  | |'   | |: :|  :  ;_    |  ' | |  . .|   : '  | .--.  .-. |  
|   |    ''   | .; :|   | |  | |'   | .; : \  \    `. |  | ' |  | ||   |  / :  \__\/: . .  
'   : |.  \   :    ||   | |  |/ |   :    |  `----.   \:  | : ;  ; |'   : |: |  ," .--.; |  
|   | '_\.'\   \  / |   | |--'   \   \  /  /  /`--'  /'  :  `--'   \   | '/ : /  /  ,.  |  
'   : |     `----'  |   |/        `----'  '--'.     / :  ,      .-./   :    |;  :   .'   \ 
;   |,'             '---'                   `--'---'   `--`----'   /    \  / |  ,     .-./ 
'---'                                                              `-'----'   `--`---'     
                                                                                           """
    # Display cool ASCII art with tool name in green
    print(f"{GREEN}{peach_art}")
    print(f"   Konosuba - Test for LFI vulnerabilities")
    print(f"   Made by {__author__}, Version {__version__}{ENDC}")

    parser = argparse.ArgumentParser(prog="tool.py", description="Test for LFI vulnerabilities", 
                                     epilog=f"Made by {__author__}, Version {__version__}", add_help=True)
    parser.add_argument("url", help="URL to test for LFI vulnerability")
    parser.add_argument("-H", "--headers", help="Headers in the format 'HeaderName: Value'")
    parser.add_argument("-C", "--cookies", help="Cookies in the format 'CookieName=CookieValue'")
    parser.add_argument("-w", "--wordlists", nargs='+', help="Wordlists containing LFI payloads", default=["wordlist.txt"])
    parser.add_argument("-t", "--threads", type=int, help="Number of threads to use", default=1)
    args = parser.parse_args()

    headers = dict(item.split(': ', 1) for item in args.headers.split(', ')) if args.headers else None
    cookies = dict(item.split('=', 1) for item in args.cookies.split('; ')) if args.cookies else None

    start_time = time.time()
    run_tests_in_threads(args.url, headers=headers, cookies=cookies, wordlists=args.wordlists, num_threads=args.threads)

    duration = time.time() - start_time
    print(f"{YELLOW}[*] Scan completed in {duration:.2f} seconds{ENDC}")
