from netmiko import ConnectHandler

my_router = {
        'device_type': 'cisco_ios',
        'host': '192.168.56.100',
        'username':'admin',
        'password':'cisco',
        }
print("Connecting to other router...")
connection = ConnectHandler(**my_router)
output = connection.send_command("show ip interface brief")

print("-" * 30)
print(output)
print("-" *30)

connection.disconnect()
