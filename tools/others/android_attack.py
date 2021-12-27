# coding=utf-8
from core import fekyou
from core import fekyousCollection


class Keydroid(fekyou):
    TITLE = "Keydroid"
    DESCRIPTION = "Android Keylogger + Reverse Shell\n" \
                  "[!] You have to install Some Manually Refer Below Link:\n " \
                  "[+] https://github.com/F4dl0/keydroid"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/F4dl0/keydroid.git"]
    RUN_COMMANDS = ["cd keydroid && bash keydroid.sh"]
    PROJECT_URL = "https://github.com/F4dl0/keydroid"


class MySMS(fekyou):
    TITLE = "MySMS"
    DESCRIPTION = "Script that generates an Android App to hack SMS through WAN \n" \
                  "[!] You have to install Some Manually Refer Below Link:\n\t " \
                  "[+] https://github.com/papusingh2sms/mysms"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/papusingh2sms/mysms.git"]
    RUN_COMMANDS = ["cd mysms && bash mysms.sh"]
    PROJECT_URL = "https://github.com/papusingh2sms/mysms"


class LockPhish(fekyou):
    TITLE = "Lockphish (Grab target LOCK PIN)"
    DESCRIPTION = "Lockphish it's the first tool for phishing attacks on the " \
                  "lock screen, designed to\n Grab Windows credentials,Android" \
                  " PIN and iPhone Passcode using a https link."
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/JasonJerry/lockphish.git"]
    RUN_COMMANDS = ["cd lockphish && bash lockphish.sh"]
    PROJECT_URL = "https://github.com/JasonJerry/lockphish"


class Droidcam(fekyou):
    TITLE = "DroidCam (Capture Image)"
    DESCRIPTION = "Powerful Tool For Grab Front Camera Snap Using A Link"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/kinghacker0/WishFish.git;"
        "sudo apt install php wget openssh-client"
    ]
    RUN_COMMANDS = ["cd WishFish && sudo bash wishfish.sh"]
    PROJECT_URL = "https://github.com/kinghacker0/WishFish"


class EvilApp(fekyou):
    TITLE = "EvilApp (Hijack Session)"
    DESCRIPTION = "EvilApp is a script to generate Android App that can " \
                  "hijack authenticated sessions in cookies."
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/crypticterminal/EvilApp.git"]
    RUN_COMMANDS = ["cd EvilApp && bash evilapp.sh"]
    PROJECT_URL = "https://github.com/crypticterminal/EvilApp"


class AndroidAttackTools(fekyousCollection):
    TITLE = "Android Hacking tools"
    TOOLS = [
        Keydroid(),
        MySMS(),
        LockPhish(),
        Droidcam(),
        EvilApp()
    ]
