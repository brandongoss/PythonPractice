import dice
from sys import exit

class Scene(object):
# nothing to put in superclass, just practicing inheritance
    def enter(self):
        pass

class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene):

    messages = [
                "Good job, you're dead now.",
                "Wow, dead as hell.",
                "You have died."
    ]

    def enter(self):

        selection = dice.roll('1d3')
        print Death.messages(selection)
        exit(1)

class Atrium(Scene):

    def enter(self):

        print """
        Wow! It's really dark in here.
        As you slowly walk through the maze, you notice something.
        A door! Will you enter or pass this door?
        """

        selection = raw_input("> ")

        if selection == 'enter'
            return 'FireRoom'

        else:
            print "You get lost in the dark, wandering aimlessly."
            return 'Death'

class FireRoom(Scene):

    def enter(self):
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
            return 'CerberusRoom'

        elif selection == 'torch':
            return 'Cavern'

        else:
            return 'Death'

class CerberusRoom(Scene):

    def enter(self):
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
            return

class Cavern(Scene):

    def enter(self):
        pass

class MinotaurRoom(Scene):

    def enter(self):
        pass

class Finish(Scene):

    def enter(self):
        print "You win! Icarus is saved and the Minotaur is dead!"
        return 'Finish'

class Weapon(object):
    
    def pick_up(self):
        pass

class Torch(Weapon):

    def throw(self):
        pass

class PocketWatch(Weapon):

    def hypnotize(self):
        pass

class Cerberus(Weapon):

    def eat(self):
        pass

class Map(object):

    scenes = {
        'Atrium': Atrium(),
        'FireRoom': FireRoom(),
        'CerberusRoom': CerberusRoom(),
        'Cavern': Cavern(),
        'MinotaurRoom': MinotaurRoom(),
        'Death': Death(),
        'Finish': Finish(),
    }

    weapons = {
        'torch': Torch(),
        'pocket watch': PocketWatch(),
        'cerberus': Cerberus(),
    }

    def __init__(self, start_scene):
        pass

    def next_scene(self, current_scene):
        pass

    def opening_scene(self):
        pass

a_map = Map('Atrium')
a_game = Engine(a_map)
a_game.play()
