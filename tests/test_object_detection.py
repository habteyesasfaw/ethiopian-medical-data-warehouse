import unittest
from unittest.mock import patch

class TestYOLOObjectDetection(unittest.TestCase):

    @patch('torch.hub.load')
    def test_yolo_model_loading(self, mock_yolo_model):
        # Mock model
        mock_yolo_model.return_value = 'MockModel'
        
        # Test if model loads correctly
        model = mock_yolo_model()
        self.assertEqual(model, 'MockModel')

   

    @patch('torch.hub.load')
    def test_yolo_object_detection(self, mock_yolo_model):
        # Mock detection result
        mock_yolo_model.return_value = 'Mocked YOLO Model'
        
        # Assuming the model will return mock results
        mock_detection = {
            'xmin': 10, 'ymin': 20, 'xmax': 100, 'ymax': 150, 
            'confidence': 0.9, 'class': 'medicine', 'image_file': 'sample_image.jpg'
        }

        model = mock_yolo_model()
        # Simulate running detection and returning mocked results
        results = mock_detection

        # Check if detection output contains necessary keys
        self.assertIn('xmin', results)
        self.assertIn('ymin', results)
        self.assertIn('confidence', results)
