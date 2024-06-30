import json
with open("info.json", "r") as file:
        data = json.load(file)
        for i in data["SeaCreature"]["goldfish"]:
                print(i)
        # for i in data["SeaCreature"]:
        #     if i == "goldfish":
        #         print(i['name'])
        #     for key, value in i:
        #         print(key)
        #         print(value)