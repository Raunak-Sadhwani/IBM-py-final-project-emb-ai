import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def assertEmotionEqual(self, actual, expected):
        for emotion in expected:
            if emotion != 'dominant_emotion':
                self.assertEqual(round(actual[emotion]), expected[emotion], f"Mismatch in {emotion}")
            else:
                self.assertEqual(actual[emotion], expected[emotion], f"Mismatch in dominant_emotion")

    def test_joy(self):
        self.assertEmotionEqual(emotion_detector("I am glad this happened"), {'anger': 0, 'disgust': 0, 'fear': 0, 'joy': 1, 'sadness': 0, 'dominant_emotion': 'joy'})

    def test_anger(self):
        self.assertEmotionEqual(emotion_detector("I am really mad about this"), {'anger': 1, 'disgust': 0, 'fear': 0, 'joy': 0, 'sadness': 0, 'dominant_emotion': 'anger'})

    def test_disgust(self):
        self.assertEmotionEqual(emotion_detector("I feel disgusted just hearing about this"), {'anger': 0, 'disgust': 1, 'fear': 0, 'joy': 0, 'sadness': 0, 'dominant_emotion': 'disgust'})

    def test_sadness(self):
        self.assertEmotionEqual(emotion_detector("I am so sad about this"), {'anger': 0, 'disgust': 0, 'fear': 0, 'joy': 0, 'sadness': 1, 'dominant_emotion': 'sadness'})

    def test_fear(self):
        self.assertEmotionEqual(emotion_detector("I am really afraid that this will happen"), {'anger': 0, 'disgust': 0, 'fear': 1, 'joy': 0, 'sadness': 0, 'dominant_emotion': 'fear'})

if __name__ == '__main__':
    unittest.main()
