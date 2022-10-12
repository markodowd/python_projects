from unittest import main, TestCase
from unittest.mock import patch
from converter import create_directory, directory_exists, remove_extension_from_filename, convert_files


class TestDoesDirectoryExist(TestCase):
    @patch('converter.os.path.exists')
    def test_does_directory_exist_when_directory_exists(self, mock_exists):
        directory = 'test/'
        mock_exists.return_value = True
        self.assertTrue(directory_exists(directory))

    @patch('converter.os.path.exists')
    def test_does_directory_exist_when_directory_not_exist(self, mock_exists):
        directory = 'test/'
        mock_exists.return_value = False
        self.assertFalse(directory_exists(directory))


class TestCreateDirectory(TestCase):
    @patch('converter.directory_exists')
    @patch('converter.os.makedirs')
    def test_create_directory_when_directory_exists(self, mock_makedirs, mock_directory_exists):
        directory = 'test/'
        mock_directory_exists.return_value = True
        create_directory(directory)
        mock_makedirs.assert_not_called()

    @patch('converter.directory_exists')
    @patch('converter.os.makedirs')
    def test_create_directory_not_exist(self, mock_makedirs, mock_directory_exists):
        directory = 'test/'
        mock_directory_exists.return_value = False
        create_directory(directory)
        mock_makedirs.assert_called_with(directory)


class TestRemoveExtensionFromFilename(TestCase):
    def test_remove_extension_from_filename_single_word(self):
        input = remove_extension_from_filename('image.jpg')
        output = 'image'
        self.assertEqual(input, output)

    def test_remove_extension_from_filename_multiple_words(self):
        input = remove_extension_from_filename('multiple_word_image.jpg')
        output = 'multiple_word_image'
        self.assertEqual(input, output)

    def test_remove_extension_from_filename_multiple_extensions(self):
        input = remove_extension_from_filename('multiple.extensions.jpg')
        output = 'multiple.extensions'
        self.assertEqual(input, output)


class TestConvertFiles(TestCase):
    @patch('converter.Image')
    @patch('converter.os.listdir')
    def test_convert_files(self, mock_listdir, mock_pil_image):
        mock_listdir.return_value = ['image.png']

        mock_opened_image = mock_pil_image.open.return_value
        mock_opened_image.size = (42, 83)

        convert_files('old_dir', 'new_dir')

        self.assertTrue(mock_pil_image.open.called)
        self.assertTrue(mock_opened_image.save.called)


if __name__ == '__main__':
    main()
