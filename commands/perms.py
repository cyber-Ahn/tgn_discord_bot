import json

with open("SETTINGS/authorization.json", "r") as f:
    cachjson = f.read()
    settings = json.loads(cachjson)

lvl1 = settings["perms"]["lvl1"]
lvl2 = settings["perms"]["lvl2"]
lvl3 = settings["perms"]["lvl3"]
lvl4 = settings["perms"]["lvl4"]

def get(memb):
    lvl = [0]
    for r in memb.roles:
        if r.name in lvl4:
            lvl.append(4)
        elif r.name in lvl3:
            lvl.append(3)
        elif r.name in lvl2:
            lvl.append(2)
        elif r.name in lvl1:
            lvl.append(1)
    return max(lvl)

def check(memb, lvl):
    return get(memb) >= lvl