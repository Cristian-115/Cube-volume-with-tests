from logging import exception
import unittest
import homework4


class TestCase(unittest.TestCase):
    #all should pass
    def test_cube_volume(self):
        self.assertEqual(homework4.cube_volume(3.0),27)
        
    def test_negatives(self):
        with self.assertRaises(Exception) as context:
            homework4.cube_volume(-1.0)
            self.assertTrue("number must be positive" in context.exception)
    def test_typeError(self):
        with self.assertRaises(TypeError):
            homework4.cube_volume("this should raise an exception")

#######################################################################################################################
    #should pass
    def test_average(self):
        list = [2,4,5,8]
        self.assertEqual(4.75, homework4.avg(list) )
            
    #should pass
    def test_empty_list(self):
        list1 = [1,2]
        self.assertEqual(len(list1), 0)

    #should pass
    def test_negatives(self):
        with self.assertRaises(TypeError):
            homework4.cube_volume("this should raise an exception")
           

#######################################################################################################################

    #should pass
    def test_badFirst(self):
        with self.assertRaises(TypeError): homework4.fname(20, "name")

    #should pass
    def test_fullname(self):
        self.assertTrue("Cristian Garibay", homework4.fname("Cristian", "Garibay"))

    #should fail
    def test_fail(self):
        self.assertEqual("cristiangaribay", homework4.fname("Cristian", "Garibay"))
           
if __name__ == '__main__':
    unittest.main()