# coding=utf-8
from core import fekyou
from core import fekyousCollection


class KnockMail(fekyou):
    TITLE = "Knockmail"
    DESCRIPTION = "KnockMail Tool Verify If Email Exists"
    INSTALL_COMMANDS = [
        "git clone https://github.com/heywoodlh/KnockMail.git",
        "cd KnockMail;sudo pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd KnockMail;python3 knockmail.py"]
    PROJECT_URL = "https://github.com/heywoodlh/KnockMail"


class EmailVerifyTools(fekyousCollection):
    TITLE = "Email Verify tools"
    TOOLS = [KnockMail()]
    
