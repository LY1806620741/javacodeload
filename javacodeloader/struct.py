from javacodeloader.keyword import KeyWordType
import re

class Util:
    @classmethod
    def getblock(self,string):
        """获取字符块"""
        return re.findall("[a-z0-9.@\u4e00-\u9fa5()\"']+",string)
    @classmethod
    def getlayer(self,content):
        """获取层级闭包"""
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
        return root
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
    def __repr__(self):
        return "class [%s] %s" % (type(self).__name__, self.__dict__)
class AccessControl(JavaBase):
    """权限"""
    def __init__(self,access_control=None):
        """默认权限是default"""
        super(AccessControl, self).__init__()
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
        super(JavaClass, self).__init__()
        self.classLoader=classLoader
        self.filepath=path
        self.Imports=[]
        self.Fileds=[]
        self.Methods=[]
        self.Annotations=[]
        self.innerClass=[]
    def doimport(self,line):
        self.Imports.append(line)
    def doAnnotation(self,ann):
        self.Annotations.append(ann)
    @classmethod
    def static_load_content(self,instance,content):
        """静态方法加载"""
        #DFA or {}load
        #分层
        root=Util.getlayer(content)
        #读取第一层类和引用
        for i in root.child:
            if isinstance(i,str):#读取引用
                i=Util.getblock(i)
                if (i[0]==KeyWordType.PackageCorrelation.Import):
                    instance.doimport(i[1])
            else:#类读取
                for j in Util.getblock(i.titile):
                    if j.startswith("@"):#类注解
                        p=j.find("(")
                        if p>1:
                            instance.doAnnotation(JavaAnnotation(j[1:p],j[p+1:-1]))
                        else:
                            instance.doAnnotation(JavaAnnotation(j[1:]))
        print(instance.Annotations)
        pass
    def loadContent(self,content):
        """加载内容"""
        self.static_load_content(self,content)
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
class JavaAnnotation(JavaBase):
    def __init__(self,name=None,value=None):
        super(JavaAnnotation, self).__init__(name,value)



    

# class JavaField:

    