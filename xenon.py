from other.utils import Utils
from scanners import xss
import sys

utilities = Utils()

if len(sys.argv) > 1:
    settings = utilities.get_settings("/home/luwzko/Desktop/projs/Xenon/python/settings")
    print(settings)
else:
    print("Too few command line arguments, must provide the path of the settings file.")
    exit()

if settings["banner"]:
    print(r"""
           _  __                        
          | |/ /___   ____   ____   ____ 
          |   // _ \ / __ \ / __ \ / __ \
         /   |/  __// / / // /_/ // / / /
        /_/|_|\___//_/ /_/ \____//_/ /_/
        """)
            
exploit = xss.XSS(settings["url"], settings["security"])
exploit.main()