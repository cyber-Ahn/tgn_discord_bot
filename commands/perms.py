import json

def get(memb, id, home_phat):
    with open(home_phat + "SETTINGS/" + id + "/authorization.json", "r") as f:
        cachjson = f.read()
        settings = json.loads(cachjson)
    lvl1 = settings["perms"]["lvl1"]
    lvl2 = settings["perms"]["lvl2"]
    lvl3 = settings["perms"]["lvl3"]
    lvl4 = settings["perms"]["lvl4"]
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

def check(memb, lvl, id, home_phat):
    return get(memb, id, home_phat) >= lvl

if __name__ == "__main__":
    print("This is a library, it can not be started directly.")