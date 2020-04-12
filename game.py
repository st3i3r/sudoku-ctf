from pwn import *
from random import choice
import time

HOST = "51.15.89.31"
PORT = 19999


def send_random_action(r, actions):
    action = choice(actions)
    r.sendline(action)
    print("Send {}".format(action))

    return action


directions = ["up", "left", "right"]
spells = ["fire", "water", "earth"]


def play(r, way):
    for i in range(len(way)):
        print("Send {}".format(way[i]))
        r.sendline(way[i])

        decision = r.recvline()
        print(decision.decode())

        monster = r.recvline()
        scene = monster
        print(monster.decode())

    return scene.decode()


way = ["left", "water", "earth"]


def main_loop():
    r = remote(HOST, PORT)
    intro = r.recvuntil("Good luck!")
    r.recvline()

    r.sendline("Hello from the other side".encode())
    r.recvline()
    response = r.recvline().decode()
    scene = play(r, way)
    print("Going to random")

    while True:
        try:
            if "monster" in scene:
                action = send_random_action(r, spells)
            elif "darkness" in scene:
                action = send_random_action(r, directions)
            else:
                break

            res = r.recvline().decode()
            if "terrible" in res:
                break
                r.close()
            else:
                way.append(action)
                print(way)
                break
        except:
            r.interactive()

    main_loop()


main_loop()
