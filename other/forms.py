import re

class Form:

    def __init__(self, html):

        self.action = re.compile("action=\"[^<> ]+\"").search(html)
        self.input_tags = re.compile("<input type=\"(search|text)\" [^<>]+/>").findall(html)
        self.method = re.compile("method=\"(get|post)\"").search(html)

        self.input_tags_attrs = {}
        for input_tag in self.input_tags:
            self.input_tags_attrs[input_tag] = {}
            for attr in re.compile("[^<> ]=\".*?\"").findall(input_tag):
                attr_name, attr_val = attr.split("=")
                self.input_tags_attrs[input_tag][attr_name] = attr_val.strip("\"")

    def get_action(self) -> str:
        return self.action

    def get_input_tags(self) -> list:
        return self.input_tags

    def get_method(self) -> str:
        return self.method

    def get_input_tags_attrs(self) -> dict:
        return self.input_tags_attrs
