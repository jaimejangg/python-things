#!/usr/bin/env python

import subprocess

interface = raw_input("interface >")
new_mac = raw_input("new MAC >")

print("[+] direccion MAC " + interface + " a " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])