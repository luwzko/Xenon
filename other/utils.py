import requests
import re
import other.forms

class Utils:

    def __init__(self):
        pass

    def read_file(self, path):
        try:
            with open(path, "r") as file:
                return [line[:-1] for line in file.readlines()]
        except FileNotFoundError:
            print("[!] File does not exist.")
            exit()

    def get_html(self, url):
        r = requests.get(url)
        return r.text.split("\n")

    def is_url_valid(self, url):
        r = requests.get(url)
        return r.status_code == 200

    def get_forms(self, url):
        #TODO: polish
        regex = re.compile("<form [^<>]+>.*?<\/form>")
        html = "".join([line.strip("\t ") for line in self.get_html(url)])
        return [other.forms.Form(form) for form in regex.findall(html)] #ez

    def get_settings(self, settings_file):
        #TODO: set values to only keys that are present in the dictionary # half done
        #TODO: add error for no vulnerability and url values
        #TODO: improve and polish
        lines = self.read_file(settings_file)
        settings = {"vulnerability":"", "url":"", "security":"low", "banner":"on"}

        for line in lines:

            key, data = line.split("::")
            key = key.lower()

            for key_1 in settings:
                if key == key_1 and (settings[key_1] == "" and data != "" or settings[key_1] != "" and data == ""):
                    settings[key] = data

        if settings["security"] not in ["low", "medium", "high"]:
            settings["security"] = "low"
            print("[!] Invalid security value, rolling back to low.")
        
        if settings["banner"] not in ["on", "off"]:
            settings["banner"] = "on"
            print("[!] Invalid banner value, rolling back to on.")
        
        settings["banner"] = (settings["banner"] == "on")
        settings["url"] += ("" if settings["url"][-1] == "/" else "/")

        return settings
