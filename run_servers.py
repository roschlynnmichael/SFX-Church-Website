import subprocess
import os

def run_servers(path):
    os.chdir(path)
    subprocess.Popen(['python', 'app.py'])
    return 1

if __name__ == '__main__':
    main_webpath = os.path.join(os.getcwd(), 'Main Website')
    admin_webpath = os.path.join(os.getcwd(), 'Admin Panel')
    if run_servers(main_webpath) == 1 and run_servers(admin_webpath) == 1:
        print("Servers are running")
    else:
        print("Failed to run servers")
