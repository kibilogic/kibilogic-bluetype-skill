# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from mycroft.skills.core import MycroftSkill
from mycroft.skills.core import intent_handler, intent_file_handler
from adapt.intent import IntentBuilder



# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

# unique name of the skill
class BluetypeSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(BlueetypeSkill, self).__init__(name="BluetypeSkill")
        
    @intent_handler(IntentBuilder('BluetypeIntent').require('BluetypeKeyword').build())
    def new_handle(self, message):
        # In this case, respond by simply speaking a canned response.
        # Mycroft will randomly speak one of the lines from the file
        #    dialogs/en-us/hello.world.dialog
        #self.speak_dialog("filetype")
        self.speak("this is a good day")


    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    def stop(self):
	pass
        

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return BluetypeSkill()
