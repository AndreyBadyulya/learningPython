import pytest

@pytest.mark.usefixtures("before")
class Test:

    @classmethod
    @pytest.fixture
    def before(cls):
        print('\nbefore each test')


    def test_1(self):
        print('test_1()')


    def test_2(self):
        print('test_2()')