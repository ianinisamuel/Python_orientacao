import re

def from_text(string):
    item = re.findall("é \w*", string)
    return item

print(from_text("Meu video game é WiiU e o preço é 1000 reias"))