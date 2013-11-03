import os
import application
import unittest
import tempfile

class DwarfTestCase(unittest.TestCase):

    def setUp(self):
        application.app.config.from_object('config.TestingConfig')
        self.app = application.app.test_client()
        self.basedir = os.path.abspath(os.path.dirname(__file__))

    def tearDown(self):
        pass

    def test_initialize(self):
        assert os.path.exists(os.path.join(self.basedir + '/content/')) == 1
        assert os.listdir(os.path.join(self.basedir + '/content/')) != []

    def test_home(self):
        rv = self.app.get('/')
        assert rv.mimetype == 'text/html'
        assert rv.status_code == 200
        assert rv.charset == 'utf-8'
        assert 'DWARF' in rv.data


if __name__ == '__main__':
    unittest.main()

