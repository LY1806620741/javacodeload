from javacodeloader.keyword import AccessControl,JavaBase
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
        #DFA
        
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

    