# coding=utf-8
from core import fekyou
from core import fekyousCollection


class DebInject(fekyou):
    TITLE = "Debinject"
    DESCRIPTION = "Debinject is a tool that inject malicious code into *.debs"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/UndeadSec/Debinject.git"]
    RUN_COMMANDS = ["cd Debinject;python debinject.py"]
    PROJECT_URL = "https://github.com/UndeadSec/Debinject"


class Pixload(fekyou):
    TITLE = "Pixload"
    DESCRIPTION = "Pixload -- Image Payload Creating tools \n " \
                  "Pixload is Set of tools for creating/injecting payload into images."
    INSTALL_COMMANDS = [
        "sudo apt install libgd-perl libimage-exiftool-perl libstring-crc32-perl",
        "sudo git clone https://github.com/chinarulezzz/pixload.git"
    ]
    PROJECT_URL = "https://github.com/chinarulezzz/pixload"

    def __init__(self):
        # super(Pixload, self).__init__([
        #     ('How To Use', self.show_project_page)
        # ], runnable = False)
        super(Pixload, self).__init__(runnable = False)


class PayloadInjectorTools(fekyousCollection):
    TITLE = "Payload Injector"
    TOOLS = [
        DebInject(),
        Pixload()
    ]
