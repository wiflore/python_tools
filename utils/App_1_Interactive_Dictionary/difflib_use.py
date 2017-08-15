import difflib
import json
from difflib import SequenceMatcher
from difflib import get_close_matches

SequenceMatcher(None, "rainn", "rain")
ratio = SequenceMatcher(None, "rainn", "rain").ratio()
print(ratio)

closer = get_close_matches("rainn", ["help", "pyramid", "rain"])
print(closer)


data = json.load(open("data.json"))
print(type(data))
print(len(data))
print(type(data.keys()))

closer = get_close_matches("rainn", data.keys())
print(closer)
closer = get_close_matches("rainn", data.keys(), n = 5)
print(closer)
closer = get_close_matches("rainn", data.keys(), n = 1)
print(closer)
