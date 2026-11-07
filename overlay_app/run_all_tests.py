"""Unified Test Suite Runner for YouTube Desktop Lyrics Overlay.
Executes all unit, security, and schema tests using standard library unittest.
"""

import unittest
import sys
import os

def run_all_tests():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=current_dir, pattern="test_*.py")

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "=" * 65)
    print(f"Test Run Completed: {result.testsRun} tests executed.")
    print(f"Status: {'PASSED (All Green)' if result.wasSuccessful() else 'FAILED'}")
    print(f"Failures: {len(result.failures)}, Errors: {len(result.errors)}")
    print("=" * 65)

    return 0 if result.wasSuccessful() else 1

if __name__ == "__main__":
    sys.exit(run_all_tests())
