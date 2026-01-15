from netmiko import ConnectHandler

my_router = {
	'device_type': 'cisco_ios',
	'host': '192.168.56.100',
	'username':'admin',
	'password':'cisco',
	}
config_commands = [
	'interface loopback100',
	'description Created by phython',
	'ip address 1.1.1.1 255.255.255.255',
	]
print("Connecting to the router...")

connection = ConnectHandler(**my_router)

print("Configuring the device..")

connection.send_config_set(config_commands)

output = connection.send_command("show ip interface brief")

print("-" * 30)
print(output)
print("-" *30)

connection.disconnect()
