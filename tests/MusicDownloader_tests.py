import unittest
import os
from MusicDownloader import MusicDownloader

class MultiplicationTestCase(unittest.TestCase):
    
    def setUp(self):
        self.urls = ["https://www.youtube.com/watch?v=gFJzWG_-EKE"]
        self.download_path = "songs\\"
        self.faild_file = "faild.txt"

    def test_download(self):
        """Test download"""

        # Download 'Wankelmut & Emma Louise - My Head Is A Jungle (MK Remix)' in songs folder
        MusicDownloader.download(self.urls,self.download_path,self.faild_file)
        self.assertEqual(os.path.exists(self.download_path+'Wankelmut & Emma Louise - My Head Is A Jungle (MK Remix).mp3'), True)


if __name__ == '__main__':
    unittest.main()