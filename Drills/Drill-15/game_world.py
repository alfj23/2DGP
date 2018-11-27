import pickle

# layer 0: Background Objects
# layer 1: Foreground Objects
objects = [[], []]  # 얘를 저장하고 나중에 복구하면 게임 세이브 앤 로드 구현가능!


def add_object(o, layer):
    objects[layer].append(o)


def add_objects(l, layer):
    objects[layer] += l


def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break


def clear():
    for l in objects:
        l.clear()


def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o


def save():
    with open('game.sav', 'wb') as f:
        pickle.dump(objects, f)


def load():
    global objects
    with open('game.sav', 'rb') as f:
        objects = pickle.load(f)
