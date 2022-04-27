import unittest
from unittest.mock import patch, mock_open
import validators
from funcs import read_alarm_file, random_value, pick_random_ringer


class TestCases(unittest.TestCase):
    def test_read_alarm_file(self):
        file_content_mock = """Hello Human!
        This is a beautiful day.
        Set an alarm for today.
        We will pick a good song.
        Good morning.
        Wake up! wake up! Time to rise and shine """
        file_path = 'd:\\skaehub\\python alarm project\\alarms.txt'

        with patch('funcs.open'.format(__name__),
                   new=mock_open(read_data=file_content_mock)) as _file:
            actual = len(read_alarm_file('alarms.txt'))
            _file.assert_called_once_with(file_path, 'r')
        expected = len(file_content_mock.split('\n'))
        self.assertEqual(expected, actual)
        self.assertIsInstance(read_alarm_file('alarms.txt'), list)


    @patch('random.randint', return_value=3)
    def test_random_value(self, mocked_randint):
        actual = random_value(['a', 'b', 'c', 'd', 'e', 'f'])
        mocked_randint.assert_called_with(0, 5)
        self.assertEqual(actual, 3)
        self.assertIsInstance(actual, int)


    def test_pick_random_ringer(self):
        result = validators.url(pick_random_ringer(['https://www.youtube.com/watch?v=ontU9cOg354',
                                                    'https://www.youtube.com/watch?v=UrGS_6_HglU',
                                                    'https://www.youtube.com/watch?v=g5qU7p7yOY8',
                                                    'https://www.youtube.com/watch?v=Um7pMggPnug', ]))
        self.assertEqual(result, True)


    @patch('clock.play_alarm')
    def test_play_alarm(self, mock_play_alarm):
        pass
        self.assertFalse(mock_play_alarm.called)
        mock_play_alarm()
        self.assertTrue(mock_play_alarm.called)
        mock_play_alarm.assert_called_with()  


    @patch('clock.set_alarm')
    def test_set_alarm(self, mock_set_alarm):
        mock_set_alarm.play_alarm()
        self.assertTrue(mock_set_alarm.play_alarm.called)


if __name__ == '__main__':
    unittest.main()
