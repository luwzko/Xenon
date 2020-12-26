from other import forms, utils
import requests
import re

class XSS:

    def __init__(self, url, security):
        
        self.utils = utils.Utils()
        self.security = security

        if self.utils.is_url_valid(url):
            self.url = url
        else:
            print(f"[!] {url} is offline")  
            print("Wait a couple of minutes before running Xenon again or check the settings file for typos.")
            exit()

    def main(self):

        output_dict = {}
        
        for form in self.utils.get_forms(self.url):
            for input_tag in form.get_input_tags_attrs():
                if form.get_method() == "get":
                    req = requests.get(self.url + form.get_action(), data = {form_tag_attrs[input_tag]["id"]:"Xenon"+form_tag_attrs[input_tag]["id"]})
                else:
                    req = requests.post(self.url + form.get_action(), data = {form_tag_attrs[input_tag]["id"]:"Xenon"+form_tag_attrs[input_tag]["id"]})
                
                output = re.compile("\n.*?Xenon" + form_tag_attrs[input_tag]["id"] + ".*?\n").search(input_tag)
                if output.replace("Xenon" + form_tag_attrs[input_tag]["id"] + "", "") == "":
                    print(f"\nPossible vulnerbility! at {input_tag}\n")