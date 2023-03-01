import unittest
from tracking_fluctuations.tracking_fluctuations import TrackingFluctuations


class TestTrackingFluctuations(unittest.TestCase):

    def setUp(self) -> None:
        self.google_excel = TrackingFluctuations(key='1ZRMLXTClSNypxb3Lk_LkEYBAwDrnqD3-opeMwiOJ0AQ', cred_file_path='tracking_fluctuations\cred.json')


    def test_wrong_user_name(self):
        
        pass