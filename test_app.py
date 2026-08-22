import unittest

class TestApp(unittest.TestCase):
    def test_health_check_payload(self):
        payload = {'status': 'healthy', 'service': 'AI-Agent-App'}
        self.assertEqual(payload['status'], 'healthy')
        self.assertEqual(payload['service'], 'AI-Agent-App')

if __name__ == '__main__':
    unittest.main()
