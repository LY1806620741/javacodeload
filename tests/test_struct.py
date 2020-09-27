
# -*- coding: utf-8 -*-
#.\setup.py test --test-suite tests.test_struct
import unittest
from unittest import mock
from javacodeloader.struct import JavaClass

class JavaClassTest(unittest.TestCase):

    def test_class_init(self):
      javaclass=JavaClass("")
      self.assertTrue(javaclass.isDefault())
      javaclass.set_access_control("PubLic")
      self.assertFalse(javaclass.isDefault())
      self.assertTrue(javaclass.isPublic())

    #.\setup.py test --test-suite tests.test_struct.JavaClassTest.test_class_load
    def test_class_load(self):
      javaclass=JavaClass("").loadContent("""  package  a.b ;import a.c;

      import a.d;
      @无值注解
      @类注解("类注解值")
      public class 类名 extends 父类{
        @属性注解({"多注解1","多注解2"})
        String 属性名1;
        String 属性名2="字符串";

        @方法注解(value={"值1","值2"},第二注解键="第二注解值")@Override
        void 方法(@Param("") String 参数) {
          if (1=1){

          }
        }
      }
      """)
      print(javaclass)

      self.assertEquals(javaclass.getName(),"类名")


#
# if __name__ == '__main__':
#     unittest.main()
# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(TestClass('test_class_init'))
#     runner = unittest.TextTestRunner()
#     runner.run(suite)