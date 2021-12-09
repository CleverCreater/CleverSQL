"""
Interpreter
import UNDL
"""
import re


class Interpreter:
    def __init__(self, undl):
        self.undl = undl
        self.Name = None
        with open(self.undl) as code:
            self.code = code.readlines()

    def name(self):
        for code in self.code:
            self.Name = re.findall('^Name:(.+?)\n', code)
            if self.Name:
                break
            else:
                self.Name = None
        return self.Name

    def ip(self):
        for code in self.code:
            self.Name = re.match(r'^IP:(\d){4}', code)
            if self.Name is not None:
                break
        return self.Name

    def interpret(self):
        for code in self.code:
            re.findall(re.compile("r[Name](.*?)"), code)
