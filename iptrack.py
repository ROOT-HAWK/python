#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import requests
import json
import time
import urllib.request, urllib.parse, urllib.error
import os

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'

class config:
        key = "d33083fa4739714fbfa7cb00f5b38070" #go https://ipstack.com/

def banner():
        os.system('clear')
        print(color.GREEN + """
████████╗██████╗  █████╗  ██████╗██╗  ██╗ ███████  ██████╗
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝ ██╔═══   ██╔══██╗
   ██║   ██████╔╝███████║██║     █████╔╝  ███████  ██████╔╝
   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗  ██║      ██╔══██╗
   ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗ ███████  ██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝  ╚═════╝ ╚═╝  ╚═╝

        Author: R00T-H4WK
        """ + color.END)

def main():
        banner()
        if len(sys.argv) == 2:
                number = sys.argv[1]
                api = "http://apilayer.net/api/validate?access_key=a2da9fcba148fea8973d032916b14e4b&number=14158586273&country_code=ID&format=1"
                output = requests.get(api)
                content = output.text
                obj = json.loads(content)
                country_code = obj['country_code']
                country_name = obj['country_name']
		location = obj['location']
                carrier = obj['carrier']
                line_type = obj['line_type']

                print(color.YELLOW + "tracker >> " + color.END + "information gathering")
                print("--------------------------------------")
                time.sleep(0.2)

                if country_code == "":
                        print(" - Getting Country               [ " + color.RED + "FAILED " + color.END + "]")
                else:
                        print(" - Getting Country               [ " + color.GREEN + "OK " + color.END + "]")

                time.sleep(0.2)
                if country_name == "":
                        print(" - Getting Country Name          [ " + color.RED + "FAILED " + color.END + "]")
                else:
                        print(" - Getting Country Name          [ " + color.GREEN + "OK " + color.END + "]")

                time.sleep(0.2)
                if location == "":
                        print(" - Getting Location              [ " + color.RED + "FAILED " + color.END + "]")
                else:
                        print(" - Getting Location              [ " + color.GREEN + "OK " + color.END + "]")

                time.sleep(0.2)
                if carrier == "":
                        print(" - Getting Carrier               [ " + color.RED + "FAILED " + color.END + "]")
                else:
                        print(" - Getting Carrier               [ " + color.GREEN + "OK " + color.END + "]")

                time.sleep(0.2)
                if line_type == None:
                        print(" - Getting Device                [ " + color.RED + "FAILED " + color.END + "]")
                else:
                        print(" - Getting Device                [ " + color.GREEN + "OK " + color.END + "]")

                print("")
                print(color.YELLOW + "tracker >> " + color.END + "Information Output")
                print("--------------------------------------")
                print(" - Ip number: " + str(number))
                print(" - Country: " + str(country_code))
                print(" - Country Name: " + str(country_name))
                print(" - Location: " + str(location))
                print(" - Carrier: " + str(carrier))
                print(" - Device: " + str(line_type))
        else:
                print("[?] Usage:")
                print(color.CYAN + " ./%s <phone-number>" % (sys.argv[0]))
                print(color.CYAN + " ./%s +62852xxxxxx" % (sys.argv[0]))


if __name__ == "__main__":
    main()
