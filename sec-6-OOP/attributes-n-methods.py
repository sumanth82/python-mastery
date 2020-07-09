#help(<instance_name_or_class_name>)
#Useful TOOL:
#help(list)

class PlayerCharacter:
    membership = True                   # Class object attribute (static); MUST be in the same indent level as the init method
                                        # This is an attribute at the class level
    def __init__(self, name):
        self.name = name
    
    def run(self):
        print('run')
        return('some_method')
    
player1 = PlayerCharacter('Tom')

print(player1.name)     # O/P: Tom

print(player1.membership)   # O/P: True












