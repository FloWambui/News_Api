import unittest
from ..app.models import models
News=models.News


class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = models(111245, 'POLITICAL NEWS', 'US PRESIDENCY', '/khsjha27hbs', '01/10/2022')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()