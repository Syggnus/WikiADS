import json


class JSONHandler:
    def __init__(self, filename):
        self.filename = filename
    
    def read(self):
        with open(self.filename, encoding="utf-8") as f:
            return json.load(f)
