# coding=utf-8
import os
from time import sleep

from core import fekyou
from core import fekyousCollection


class UpdateTool(fekyou):
    TITLE = "Update Tool or System"
    DESCRIPTION = "Update Tool or System"

    def __init__(self):
        super(UpdateTool, self).__init__([
            ("Update System", self.update_sys),
            ("Update fekyou", self.update_ht)
        ], installable = False, runnable = False)

    def update_sys(self):
        os.system("sudo apt update && sudo apt full-upgrade -y")
        os.system(
            "sudo apt-get install tor openssl curl && sudo apt-get update tor openssl curl")
        os.system("sudo apt-get install python3-pip")

    def update_ht(self):
        os.system("sudo chmod +x /etc/;"
                  "sudo chmod +x /usr/share/doc;"
                  "sudo rm -rf /usr/share/doc/fekyou/;"
                  "cd /etc/;"
                  "sudo rm -rf /etc/fekyou/;"
                  "mkdir fekyou;"
                  "cd fekyou;"
                  "git clone https://github.com/ABDUL174/fekyou.git;"
                  "cd fekyou;"
                  "sudo chmod +x install.sh;"
                  "./install.sh")


class UninstallTool(fekyou):
    TITLE = "Uninstall fekyou"
    DESCRIPTION = "Uninstall fekyou"

    def __init__(self):
        super(UninstallTool, self).__init__([
            ('Uninstall', self.uninstall)
        ], installable = False, runnable = False)

    def uninstall(self):
        print("fekyou started to uninstall..\n")
        sleep(1)
        os.system("sudo chmod +x /etc/;"
                  "sudo chmod +x /usr/share/doc;"
                  "sudo rm -rf /usr/share/doc/fekyou/;"
                  "cd /etc/;"
                  "sudo rm -rf /etc/fekyou/;")
        print("\nfekyou Successfully Uninstalled..")
        print("Happy Hacking..!!")
        sleep(1)


class ToolManager(fekyousCollection):
    TITLE = "Update or Uninstall | fekyou"
    TOOLS = [
        UpdateTool(),
        UninstallTool()
    ]
