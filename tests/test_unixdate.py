import unittest
import datetime

from stuffr import unix2date, date2unix

class TestUnixDate(unittest.TestCase):

    def test_unix_to_date(self):
        expected = datetime.datetime(1970,1,1,0,0)
        date = unix2date(0)
        self.assertEqual(expected, date)
    
    def test_date_to_unix(self):
        expected = 0
        timestamp = date2unix(1970,1,1,0,0,0)
        self.assertEqual(expected, timestamp)
    
    def test_unix_to_date_to_unix(self):
        expected = 52254455 #random number
        date = unix2date(expected)
        timestamp = date2unix(date.year, date.month, date.day, date.hour, date.minute, date.second)
        self.assertEqual(expected, timestamp)
        
if __name__ == '__main__':

    # unittest.main() will look at this file and find all classes
    # that are subclasses of unittest.TestCases and run all methods in thoses
    # classes that start with test_
    unittest.main()
