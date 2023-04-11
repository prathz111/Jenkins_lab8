import unittest
from netmiko import ConnectHandler
import re


# Function to check the IP address of loopback 99 on Router 3
def check_loopback_99_ip():
    R3 = {"device_type": "cisco_ios", "ip": "198.51.100.13", "username": "netman", "password": "netman"}
    net_connect = ConnectHandler(**R3)
    output = net_connect.send_command("show ip int brief")
    loop99_output = net_connect.send_command("show ip int loop99")
    net_connect.disconnect()
    for line in loop99_output.split("\n"):
        if "Internet address" in line:
            ip = line.split()[-1]
            break
    if re.match(r"^10\.1\.3\.\d{1,3}/24$", ip):
        print("Loopback 99 on Router 3 has the correct IP address.")
        return True
    else:
        print("Loopback 99 on Router 3 does not have the correct IP address.")
        return False

# Function to check if Router 1 is configured for only one area
def check_router1_areas():
    R1 = {"device_type": "cisco_ios", "ip": "198.51.100.11", "username": "netman", "password": "netman"}
    net_connect = ConnectHandler(**R1)
    output = net_connect.send_command("show ip protocols")
    net_connect.disconnect()
    if "Number of areas in this router is 1" in output:
        print("Router 1 is configured for only one area.")
        return True
    else:
        print("Router 1 is not configured for only one area.")
        return False

# Function to check if a ping from Router 2's loopback to Router 5's loopback is successful
def check_ping_router2_to_router5():
    R2 = {"device_type": "cisco_ios", "ip": "198.51.100.12", "username": "netman", "password": "netman"}
    R5_loopback_ip = "10.1.5.1"
    net_connect = ConnectHandler(**R2)
    output = net_connect.send_command(f"ping {R5_loopback_ip} source 10.1.2.1")
    net_connect.disconnect()
    if "Success rate is 100 percent" in output:
        print("Ping from Router 2's loopback to Router 5's loopback is successful.")
        return True
    else:
        print("Ping from Router 2's loopback to Router 5's loopback is not successful.")
        return False

#check_loopback_99_ip()
#check_router1_areas()
#check_ping_router2_to_router5()

class TestFunctions(unittest.TestCase):
    def test_check_loopback_99_ip(self):
        expected_output = True
        actual_output = check_loopback_99_ip()
        self.assertEqual(expected_output, actual_output)

    def test_check_router1_areas(self):
        expected_output = True
        actual_output = check_router1_areas()
        self.assertEqual(expected_output, actual_output)

    def test_check_ping_router2_to_router5(self):
        expected_output = True
        actual_output = check_ping_router2_to_router5()
        self.assertEqual(expected_output, actual_output)

unittest.main()
