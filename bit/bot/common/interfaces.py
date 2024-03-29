from zope.interface import Interface as I

from bit.core.interfaces import IRequest


class IAgents(I):
    pass


class ISubscriptions(I):
    pass


class ISubscribe(I):
    pass


class IWebResource(I):
    pass


class IRoles(I):
    pass


class IIRCBot(I):
    pass


class IIRCRequest(I):
    pass


class INameResolver(I):
    pass


class ISocketRequest(IRequest):
    pass


class IBotSocket(I):
    pass


class IWebRoot(I):
    pass


class ISQLQuery(I):
    pass


class IFlatten(I):
    pass


class IDataBrain(I):
    pass


class IDataRecord(I):
    pass


class IIntelligent(I):
    pass


class IBotAgent(I):
    pass


class IWebImages(I):
    pass


class IWebFolder(I):
    pass


class IWebCSS(I):
    pass


class IWebJS(I):
    pass


class IWebHTML(I):
    pass


class IJSON(I):
    pass


class IData(I):
    pass


class IDataProvider(I):
    pass


class ISessions(I):
    pass


class ISession(I):
    pass


class IWebRoot(I):
    pass


class IMUCBot(I):
    pass


class IAIMLMacro(I):
    pass


class IGroupOfPeople(I):
    """ group of people, an organisation or company """


class IMembers(I):
    """  """


class IMember(I):
    """  """


class IGroup(I):
    """  """


class IMemory(I):
    """ persistent information """


class IGroups(I):
    """  """


class IBotRequest(I):
    """ curate command """
