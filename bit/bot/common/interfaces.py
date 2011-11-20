
from zope.interface import Interface as I


class IConfiguration(I):
    pass

class IMUCBot(I):
    pass

class IFileConfiguration(I):
    pass

class IRoles(I):
    pass

class IAIMLMacro(I):
    pass

class IGroupOfPeople(I):
    """ group of people, an organisation or company """

class IMembers(I):
    """ possible buddies 8) """

class IMember(I):
    """ possible buddies 8) """

class IGroup(I):
    """ possible buddies 8) """        


class IMemory(I):
    """ persistent information """


class IGroups(I):
    """ possible buddies 8) """    

class ICurateBotProtocol(I):
    """ curate command """

class IBotRequest(I):
    """ curate command """
