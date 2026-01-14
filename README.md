# Network Automation Labs

Hands-on labs to learn **Python-based** network automation using GNS3 and Ubuntu.  
Focus areas: SSH automation with Netmiko, configuration management, and step-by-step learning for network engineers transitioning into automation.

---

## Prerequisites

- Ubuntu VM (used as the automation host)
- GNS3 topology with at least one Cisco IOS router
- Python 3 installed
- Required Python packages:
  ```bash
  pip install netmiko
Ensure your Ubuntu VM can reach the router via IP and SSH (same subnet, SSH enabled on the router).

---

## Lab 1 – Show IP Interface Brief with Netmiko

**File:** `python/netmiko/lab1_show_ip_int_brief.py`

**Goal**  
Connect to a Cisco router over SSH and run `show ip interface brief`, printing the output to the terminal.

**Concepts covered**

- Python dictionary for device connection details
- Netmiko `ConnectHandler` for SSH
- `send_command` to execute show commands
- Cleanly disconnecting from the device

**How to run**

```bash
python3 python/netmiko/lab1_show_ip_int_brief.py
Before running, update the script with your router’s:

- `host` (IP address)
- `username`
- `password`

---

## Lab 2 – Configure Loopback Interface with Netmiko

**File:** `python/netmiko/lab2_config_loopback.py`

**Goal**  
Push configuration to create `Loopback100` with IP `1.1.1.1 255.255.255.255` using a Python script.

**Concepts covered**

- Python list for multiple config commands
- Netmiko `send_config_set` for configuration mode
- Basic configuration automation pattern

**How to run**

```bash
python3 python/netmiko/lab2_config_loopback.py

As with Lab 1, update the device credentials in the script to match your lab router.

---

## Roadmap (Planned Labs)

- Multi-device automation using loops and an inventory
- Separating device data into YAML/JSON files
- Gathering structured output and saving to files
- Intro to REST APIs for network controllers

This repository is a living set of labs documenting the journey from traditional networking to Python-driven network automation.



