from javacodeloader.keyword import KeyWordType
class JavaBase:
    """基础"""
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
    """权限"""
    def __init__(self,access_control=None):
        """默认权限是default"""
        super(JavaBase, self).__init__()
        self.access_control=access_control
    def isPublic(self):
        return self.access_control==KeyWordType.AccessControl.Public
    def isDefault(self):
        return self.access_control==None
    def isProtected(self):
        return self.access_control==KeyWordType.AccessControl.Protected
    def isPrivate(self):
        return self.access_control==KeyWordType.AccessControl.Private
    def set_access_control(self,name):
        """设置属性[Public,Protected,Private,None]"""
        name=name.lower()
        if (name in KeyWordType.AccessControl.members):
            self.access_control=name
class Closure:
    """闭包"""
    def __init__(self,parent=None):
        self.parent=parent
        if parent!=None:
            self.parent.child.append(self)
        self.titile=None
        self.child=[]
class ClassLoader:
    """类加载"""
    def __init__(self,path):
        self.class_pool=[]
    def getJavaClass(self,name):
        """获取java类,a.b.c.d"""
        return self.class_pool[name]
    def loadJavaClass(self,path):
        pass

class JavaClass(AccessControl):
    """java类信息"""
    def __init__(self,path,classLoader=None):
        super(AccessControl, self).__init__()
        self.classLoader=classLoader
        self.filepath=path
        self.Imports=[]
        self.Fileds=[]
        self.Methods=[]
        self.Annotations=[]
        self.innerClass=[]
    def doimport(self,line):
        self.importlist.append(line)
    @classmethod
    def static_load_content(self,content):
        """静态方法加载"""
        #DFA or {}load
        #分层
        root=Closure()
        layer=root
        temp=""
        for c in content:
            if c == "{":
                layer=Closure(layer)
                layer.titile=temp
                temp=""
            elif c== "}":
                layer=layer.parent
            elif c== ";":
                layer.child.append(temp)
                temp=""
            else:
                temp+=c
        print(root.child)
        pass
    def loadContent(self,content):
        """加载内容"""
        self.static_load_content(content)
        return self
    def print(self):
        pass

class JavaMethod(AccessControl):
    """java方法"""
    def __init__(self,name=None,):
        pass
class JavaFiled(AccessControl):
    def __init__(self):
        pass
class Annotation(JavaBase):
    pass



    

# class JavaField:

    