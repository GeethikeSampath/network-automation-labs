from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException,NetmikoAuthenticationException
from getpass import getpass

host = input("Enter Device IP Address:")
username = input ("Enter User Name:")
password = getpass("Enter Password:")

device = {
	"device_type": "cisco_ios",
	"host": host,
	"username": username,
	"password" : password,
	}
try:
    print(f"\nConnecting to {host}...")
    connection = ConnectHandler(**device)

    print("connected.Running 'show ip interface brief'...")
    output = connection.send_command("show ip inter brief")

    print("-" * 60)
    print(output)
    print("-" * 60)

    connection.disconnect()
    print("Connection closed.\n")
  
except NetmikoTimeoutException:
    print(f"\nERROR: Cannot Reach device at {host}.")
    print("Check the IP address,Network connectivity and SSH on Device.\n")
 
except NetmikoAuthenticationException:
    print(f"\nERROR:Authentication Failiure for device {host}")
    print("Check the User Name and Password Again..\n")
  
except Exception as e:
    print("\nAn unexpected error..")
    print(e)
    print()
