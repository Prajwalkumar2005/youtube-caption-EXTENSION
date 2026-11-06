import unittest
import secrets
from bridge_server import generate_secure_token

class TestSecurityToken(unittest.TestCase):
    def test_token_format_and_entropy(self):
        token1 = generate_secure_token()
        token2 = generate_secure_token()

        # Must be 32 hex characters (128 bits of cryptographic entropy)
        self.assertEqual(len(token1), 32)
        self.assertEqual(len(token2), 32)
        self.assertTrue(all(c in "0123456789abcdef" for c in token1.lower()))
        self.assertTrue(all(c in "0123456789abcdef" for c in token2.lower()))

        # Must be distinct random tokens
        self.assertNotEqual(token1, token2)

    def test_constant_time_comparison(self):
        token = generate_secure_token()
        matching = token
        tampered = token[:-1] + ("0" if token[-1] != "0" else "1")

        self.assertTrue(secrets.compare_digest(token, matching))
        self.assertFalse(secrets.compare_digest(token, tampered))
        self.assertFalse(secrets.compare_digest(token, ""))

if __name__ == "__main__":
    unittest.main()

