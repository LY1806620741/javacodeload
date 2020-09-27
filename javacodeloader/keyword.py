class AccessControl:
    """访问控制"""
    Private="private"
    Protected="protected"
    Public="public"
AccessControl.members=[AccessControl.Private,AccessControl.Protected,AccessControl.Public]
class Modifier:
    """类、方法和变量修饰符"""
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
Modifier.members=[Modifier.Abstract,Modifier.Class,Modifier.Extends,Modifier.Final,Modifier.Implements,Modifier.Interface,Modifier.Native,Modifier.New,Modifier.Static,Modifier.Strictfp,Modifier.Synchronized,Modifier.Transient,Modifier.Volatile]
class ProgramControl:
    """程序控制"""
    Break="break"
    Continue="continue"
    Return="return"
    Do="do"
    While="while"
    If="if"
    Else="else"
    For="for"
    Instanceof="instanceof"
    Switch="switch"
    Case="case"
    Default="default"
ProgramControl.members=[ProgramControl.Break,ProgramControl.Continue,ProgramControl.Return,ProgramControl.Do,ProgramControl.While,ProgramControl.If,ProgramControl.Else,ProgramControl.For,ProgramControl.Instanceof,ProgramControl.Switch,ProgramControl.Case,ProgramControl.Default]
class ErrorHandle:
    """错误处理"""
    Try="try"
    Catch="catch"
    Throw="throw"
    Throws="throws"
    Finally="finally"
ErrorHandle.members=[ErrorHandle.Try,ErrorHandle.Catch,ErrorHandle.Throw,ErrorHandle.Throws,ErrorHandle.Finally]
class PackageCorrelation:
    """包相关"""
    Import="import"
    Package="package"
PackageCorrelation.members=[PackageCorrelation.Import,PackageCorrelation.Package]
class BasicTypes:
    """基本类型"""
    Boolean="boolean"
    Byte="byte"
    Char="char"
    Double="double"
    Float="float"
    Int="int"
    Long="long"
    Short="short"
    Null="null"
    _True="true"
    _False="false"
BasicTypes.members=[BasicTypes.Boolean,BasicTypes.Byte,BasicTypes.Char,BasicTypes.Double,BasicTypes.Float,BasicTypes.Int,BasicTypes.Long,BasicTypes.Short,BasicTypes.Null,BasicTypes._True,BasicTypes._False]
class VariableReference:
    """变量引用"""
    Super="super"
    This="this"
    Void="void"
VariableReference.members=[VariableReference.Super,VariableReference.This,VariableReference.Void]
class ReservedWords:
    """保留字"""
    Goto="goto"
    Const="const"
ReservedWords.members=[ReservedWords.Goto,ReservedWords.Const]
class KeyWordType:
    AccessControl=AccessControl()
    Modifier=Modifier()
    ProgramControl=ProgramControl()
    ErrorHandle=ErrorHandle()
    PackageCorrelation=PackageCorrelation()
    BasicTypes=BasicTypes()
    VariableReference=VariableReference()
    ReservedWords=ReservedWords()
