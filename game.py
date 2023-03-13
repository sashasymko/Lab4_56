"""
the Game (task 5)
"""
class Room():
    """
    class Room
    """
    def __init__(self, name):
        """
        initialize the Room
        """
        self.name = name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def set_description(self, description):
        """
        setting description
        """
        self.description = description

    def get_description(self):
        """
        getting description
        """
        return self.description

    def set_character(self, character):
        """
        setting the character
        """
        self.character = character

    def get_character(self):
        """
        getting the character
        """
        return self.character

    def set_item(self, item):
        """
        setting the item
        """
        self.item = item

    def get_item(self):
        """
        getting the item
        """
        return self.item

    def get_name(self):
        """
        getting the name
        """
        return self.name

    def set_name(self, name):
        """
        setting the name
        """
        self.name = name

    def link_room(self, room_to_link, direction):
        """
        linking the room
        """
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        """
        getting the details
        """
        print(self.get_name())
        print("--------------------")
        print(self.get_description())
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)

    def move(self, direction):
        """
        move
        """
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self

    def get_opposite_direction(self, direction):
        """
        getting opposite direction
        """
        if direction == "north":
            return "south"
        if direction == "south":
            return "north"
        if direction == "east":
            return "west"
        if direction == "west":
            return "east"

class Character():
    """
    class Character
    """
    def __init__(self, name, description):
        """
        initialize the Character
        """
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None
        self.defeated = 0

    def describe(self):
        """
        describing
        """
        print(self.name + " is here!")
        print(self.description)

    def set_conversation(self, conversation):
        """
        setting the conversation
        """
        self.conversation = conversation

    def talk(self):
        """
        talking
        """
        if self.conversation is not None:
            print(self.name + " says: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def set_weakness(self, weakness):
        """
        setting weakness
        """
        self.weakness = weakness

    def get_weakness(self):
        """
        getting weakness
        """
        return self.weakness

    def fight(self, item):
        """
        fighting
        """
        if item == self.weakness:
            print("You fend " + self.name + " off with the " + item)
            self.defeated += 1
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False

    def get_defeated(self):
        """
        getting defeted
        """
        return self.defeated

class Enemy(Character):
    """
    class Enemy
    """
    def __init__(self, name, description):
        """
        initialize the Enemy
        """
        super().__init__(name, description)

class Item():
    """
    class Item
    """
    def __init__(self, name):
        """
        initialize the Item
        """
        self.name = name
        self.description = None

    def set_description(self, description):
        """
        setting description
        """
        self.description = description

    def get_description(self):
        """
        getting description
        """
        return self.description

    def get_name(self):
        """
        getting name
        """
        return self.name

    def set_name(self, name):
        """
        setting name
        """
        self.name = name

    def describe(self):
        """
        describing
        """
        print(self.name + ": " + self.description)
        