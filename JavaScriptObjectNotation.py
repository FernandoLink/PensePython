import json 

with open("JavaScriptObjectNotation.json", "r") as read_file:
    data = json.load(read_file)
    
print(data['nome'])
print(data['exarray'][1])
print(data['exobj']['exnull'])
print(data['exarobj'][0]['obj1'])
