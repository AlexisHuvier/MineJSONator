import json


class MineJSONator:
    def __init__(self, modid):
        self.modid = modid

    def run(self):
        while True:
            print("|====== MineJSONator ======|")
            print("| 1. Generate blockstate   |")
            print("| 2. Generate model block  |")
            print("| 2. Generate model item   |")
            print("|==========================|")
            retour = input("Choix : ")
            if retour == "1":
                json_ = self.generate_blockstate()
            elif retour == "2":
                json_ = self.generate_model_block()
            elif retour == "3":
                json_ = self.generate_model_item()
            else:
                json_ = {}
            if json_ != {}:
                path = input("Path : ")
                with open(path, "w") as f:
                    json.dump(json_, f, indent=4)
            if input("Autre JSON ? (O/N) : ").lower() != "o":
                break

    def generate_blockstate(self):
        json_ = {"variants": {}}
        while True:
            variant = input("Nom du variant : ")
            model = input("Model : ")
            rotation_x = int(input("Rotation X : "))
            rotation_y = int(input("Rotation Y : "))
            rotation_z = int(input("Rotation Z : "))
            json_["variants"][variant] = {
                "model": "minecraft:block/"+model[1:] if model.startswith("/") else self.modid+":block/"+model,
                "x": rotation_x,
                "y": rotation_y,
                "z": rotation_z
            }
            if input("Autre Variant ? (O/N) : ").lower() != "o":
                break
        return json_

    def generate_model_block(self):
        json_ = {}
        parent = input("Parent : ")
        json_["parent"] = "block/"+parent[1:] if parent.startswith("/") else self.modid+":block/"+parent
        json_["textures"] = {}
        while True:
            texture = input("Nom de la texture : ")
            path = input("Texture : ")
            json_["textures"][texture] = "minecraft:block/"+path[1:] if path.startswith("/") else \
                self.modid+":block/"+path
            if input("Autre Texture ? (0/N) : ").lower() != "o":
                break
        return json_

    def generate_model_item(self):
        json_ = {}
        if input("Est un Bloc ? (O/N) : ").lower() == "o":
            parent = input("Parent : ")
            json_["parent"] = "minecraft:block/"+parent[1:] if parent.startswith("/") else self.modid+":block/"+parent
        else:
            parent = input("Parent : ")
            json_["parent"] = "minecraft:item/"+parent[1:] if parent.startswith("/") else self.modid+":item/"+parent
            json_["textures"] = {}

            while True:
                texture = input("Nom de la texture : ")
                path = input("Texture : ")
                json_["textures"][texture] = "minecraft:item/" + path[1:] if path.startswith("/") else \
                    self.modid+":item/"+path
                if input("Autre Texture ? (0/N) : ").lower() != "o":
                    break
        return json_

