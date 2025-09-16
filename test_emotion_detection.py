from EmotionDetection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def check_case(self, text, expect):
        result = emotion_detector(text)
        for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']:
            self.assertIn(emotion, result)

        self.assertEqual(
            result['dominant_emotion'],
            expect
        )
    
    def test_joy(self):
        self.check_case("I am glad this happened", "joy")

    def test_anger(self):
        self.check_case("I am really mad about this", "anger")

    def test_disgust(self):
        self.check_case("I feel disgusted just hearing about this", "disgust")

    def test_sadness(self):
        self.check_case("I am so sad about this", "sadness")

    def test_fear(self):
        self.check_case("I am really afraid that this will happen", "fear")

if __name__ == "__main__":
    unittest.main()
    

    