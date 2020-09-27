class KeyWord:
    Private="private"
    Protected="protected"
    Public="public"
    Abstract="abstract"
    Class="class"
    Extends="extends"
    Final="final"
    Implements="implements"
    Interface="interface"
    Native="native"
    New="new"
    Static="static"
    Strictfp="strictfp"
    Synchronized="synchronized"
    Transient="transient"
    Volatile="volatile"
class KeyWordType:
    AccessControl=AccessControl()
    Modifier=Modifier()

class AccessControl:
    """访问控制"""
    members=[KeyWord.Public,KeyWord.Protected,KeyWord.Private,None]
class Modifier:
    """修饰符"""
    members=[KeyWord.Abstract,KeyWord.Class,KeyWord.Extends,KeyWord.Final,KeyWord.Implements,KeyWord.Interface,KeyWord.Native,KeyWord.New,KeyWord.Static,KeyWord.Strictfp,KeyWord.Synchronized,KeyWord.Transient,KeyWord.Volatile]
class AccessControl:
    members=[KeyWord.Public,KeyWord.Protected,KeyWord.Private,None]
class AccessControl:
    members=[KeyWord.Public,KeyWord.Protected,KeyWord.Private,None]
class AccessControl:
    members=[KeyWord.Public,KeyWord.Protected,KeyWord.Private,None]
class AccessControl:
    members=[KeyWord.Public,KeyWord.Protected,KeyWord.Private,None]

class JavaBase:
    def __init__(self,name=None,value=None):
        self.name=name
        self.value=value
    def getName(self):
        return self.name
    def setName(self,name):
        self.name=name
    def getValue(self):
        return self.value
    def setValue(self,value):
        self.value=value

class AccessControl(JavaBase):
    
    def __init__(self,access_control=None):
        """默认权限是default"""
        super(JavaBase, self).__init__()
        self.access_control=access_control
    def isPublic(self):
        return self.access_control==KeyWord.Public
    def isDefault(self):
        return self.access_control==None
    def isProtected(self):
        return self.access_control==KeyWord.Protected
    def isPrivate(self):
        return self.access_control==KeyWord.Private
    def set_access_control(self,name):
        """设置属性[Public,Protected,Private,None]"""
        name=name.lower()
        if (name in KeyWordType.AccessControl.members):
            self.access_control=name