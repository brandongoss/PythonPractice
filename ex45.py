from sys import exit

from random import randint

class Scene(object):
# nothing to put in superclass, just practicing inheritance
    def enter(self):
        pass

class Player(object):

    weaponlist = []

    def set_weapon(self, selection):
        weaponlist.append(selection)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self, Player):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('Finish')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    messages = [
                "Good job, you're dead now.",
                "Wow, dead as hell.",
                "You have died."
    ]

    def enter(self):

        print Death.messages[randint(0, len(messages)-1)]
        exit(1)

class Atrium(Scene):

    def enter(self):

        print """
        Wow! It's really dark in here.
        As you slowly walk through the maze, you notice something.
        A door! Will you enter or pass this door?
        """

        selection = raw_input("> ")

        if selection == 'enter':
            return 'FireRoom'

        else:
            print "You get lost in the dark, wandering aimlessly."
            return 'Death'

class FireRoom(Scene):

    def enter(self, Player):
        print """
        A great blaze appears on either side of you.
        As you walk through the fire laden corridor, you notice something.
        To your right a torch, and to your left a pocket watch.
        Just then you hear a rumbling coming from behind you, better act quick.
        You only have time to grab one object, which will it be?
        The pocket watch, or the torch?
        """

        selection = raw_input("> ")

        if selection == 'pocket watch':
            Player.set_weapon(selection)
            return 'CerberusRoom'

        elif selection == 'torch':
            Player.set_weapon(selection)
            return 'CerberusRoom'

        else:
            return 'Death'

class CerberusRoom(Scene):

    def enter(self, Player):
        print """
        As the door swings open you notice a great three headed beast before you.
        Awoken by stone door hitting the opposing wall, up stands the massive
        Cerberus, clearly annoyed. He guards a large door which could lead you
        to Icarus, what do you do? Run or fight?
        """

        selection = raw_input("> ")

        if selection == 'run':
            print "You get lost in the dark, wandering aimlessly."
            return 'Death'

        elif selection == 'fight':
            for name in weaponlist:
                if name == 'torch':
                    print """
                    The Cerberus, fearing the fire, hides in the corner.
                    You walk by him and proceed through the next door.
                    """
                    return 'MinotaurRoom'

                if name == 'pocket watch':
                    print """
                    Slowly you start to swing the watch back and forth.
                    The Cerberus becomes entranced, and eventually hypnotized.
                    Under the spell of your command, he his now at your service.
                    You and the Cerberus walk into the next room together.
                    """
                    Player.set_weapon('Cerberus')
                    return 'MinotaurRoom'

                else:
                    return 'Death'

class MinotaurRoom(Scene):

    def enter(self, Player):
        print """
        Icarus! There he is! But a massive beast stands before you, with
        the body of a man and the head of a bull. You cannot outrun him,
        you must fight him if you wish to save your dear friend.
        """

        for name in weaponlist:
            if name == 'torch':
                print "The Minotaur is unafraid of fire. This is not good."
                return 'Death'

            if name == 'Cerberus':
                print """
                Good thing you have the Cerberus with you, he will do the fighting.
                Back and forth the two battle, until eventually the Cerberus bites
                the Minotaur's head off. Meanwhile you sit back and watch on as
                your hypontized minion does all the work.
                """
                return 'Finish'

            else:
                print "You have no weapons! Oh no!"
                return 'Death'

class Finish(Scene):

    def enter(self):
        print "You win! Icarus is saved and the Minotaur is dead!"
        return 'Finish'

class Map(object):

    scenes = {
        'Atrium': Atrium(),
        'FireRoom': FireRoom(),
        'CerberusRoom': CerberusRoom(),
        'MinotaurRoom': MinotaurRoom(),
        'Death': Death(),
        'Finish': Finish(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('Atrium')
a_game = Engine(a_map)
a_game.play()
