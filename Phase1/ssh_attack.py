import paramiko

def ssh_login(ip, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        print(f"Attempting SSH login to {ip} with {username}:{password}")
        client.connect(ip, username=username, password=password, timeout=5)

        stdin, stdout, stderr = client.exec_command('whoami')
        output = stdout.read().decode().strip()
        print(f"Login successful! Command output: {output}")
        client.close()
        return True

    except paramiko.AuthenticationException:
        print("[-] Authentication failed.")
    except Exception as e:
        print(f"[!] SSH connection error: {e}")
    return False

if __name__ == "__main__":
    ssh_login("192.168.56.101", "vagrant", "vagrant")
