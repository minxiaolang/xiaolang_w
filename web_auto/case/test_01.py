import unittest
#导入测试框架

class LoginTt(unittest.TestCase):
    def setUp(self):
        print('打开浏览器')

    def tearDown(self):
        print('关闭浏览器')
    def test01(self):
        '''验证1'''
        print('111111111111111')
        a='admin'
        b='admin'
        self.assertTrue(a==b)


    def test02(self):
        '''验证2'''
        print('2222222222222222222')
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)

if __name__=="__main__":
    print('hhhhh')
    unittest.main()