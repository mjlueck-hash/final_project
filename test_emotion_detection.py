"""Unit tests for the emotion detector."""

import unittest

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Check that each sample statement yields the expected emotion."""

    def test_dominant_emotion(self):
        """Every sample should be dominated by one known emotion."""
        samples = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear",
        }
        for statement, expected in samples.items():
            with self.subTest(statement=statement):
                result = emotion_detector(statement)
                self.assertEqual(result["dominant_emotion"], expected)

    def test_blank_entry(self):
        """A blank statement should come back as all None."""
        result = emotion_detector("")
        self.assertIsNone(result["dominant_emotion"])
        self.assertIsNone(result["anger"])


if __name__ == "__main__":
    unittest.main()
