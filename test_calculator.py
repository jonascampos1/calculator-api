import unittest
from services.calculator import sum_,sub_,div_,mult_,square_root_


class TestCalculator(unittest.TestCase):

    #Happy test cases
    def test_valid_operations(self):
        self.assertEqual(sum_(1,1),2)
        self.assertEqual(sub_(1,1),0)
        self.assertEqual(mult_(2,1),2)
        self.assertEqual(div_(4,2),2)
        self.assertEqual(square_root_(9),3)

        print("OK -> Happy test cases")


    #TypeError test cases
    def test_Error_operations(self):
        #Sum
        self.assertRaises(TypeError,sum_,'1',1)
        self.assertRaises(TypeError,sum_,1,'2')
        self.assertRaises(TypeError,sum_,'a',1)
        self.assertRaises(TypeError,sum_,1,'a')
        self.assertRaises(TypeError,sum_,'a','b')
        self.assertRaises(TypeError,sum_,True,1)
        self.assertRaises(TypeError,sum_,1,True)
        #Complex numbers
        self.assertRaises(TypeError,sum_,1,1+3j)

        #Sub
        self.assertRaises(TypeError,sub_,'1',1)
        self.assertRaises(TypeError,sub_,1,'2')
        self.assertRaises(TypeError,sub_,'a',1)
        self.assertRaises(TypeError,sub_,1,'a')
        self.assertRaises(TypeError,sub_,'a','b')
        self.assertRaises(TypeError,sub_,True,1)
        self.assertRaises(TypeError,sub_,1,True)
        #Complex numbers
        self.assertRaises(TypeError,sub_,1,1+3j)

        #Mult
        self.assertRaises(TypeError,mult_,'1',1)
        self.assertRaises(TypeError,mult_,1,'2')
        self.assertRaises(TypeError,mult_,'a',1)
        self.assertRaises(TypeError,mult_,1,'a')
        self.assertRaises(TypeError,mult_,'a','b')
        self.assertRaises(TypeError,mult_,True,1)
        self.assertRaises(TypeError,mult_,1,True)
        #Complex numbers
        self.assertRaises(TypeError,mult_,1,1+3j)

        #Div
        self.assertRaises(ZeroDivisionError,div_,1,0)        
        self.assertRaises(TypeError,div_,'1',1)
        self.assertRaises(TypeError,div_,1,'2')
        self.assertRaises(TypeError,div_,'a',1)
        self.assertRaises(TypeError,div_,1,'a')
        self.assertRaises(TypeError,div_,'a','b')
        self.assertRaises(TypeError,div_,True,1)
        self.assertRaises(TypeError,div_,1,True)
        #Complex numbers
        self.assertRaises(TypeError,div_,1,1+3j)

        #square_root
        self.assertRaises(ValueError,square_root_,-1)   
        self.assertRaises(TypeError,square_root_,'1')
        self.assertRaises(TypeError,square_root_,'a')
        self.assertRaises(TypeError,square_root_,True)
        #Complex numbers
        self.assertRaises(TypeError,square_root_,1+3j)

        print("OK ->Raise exceptions")
 


