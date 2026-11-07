# Contributing to YouTube Desktop Lyrics Overlay 🤝

Thank you for your interest in contributing to **YouTube Desktop Lyrics Overlay**!

---

## Code of Conduct
We are committed to providing a welcoming, productive, and harassment-free experience for everyone.

---

## Development Setup

1. **Fork and clone the repository**:
   ```cmd
   git clone https://github.com/Prajwalkumar2005/EXTENSION.git
   cd EXTENSION
   ```
2. **Install development requirements**:
   ```cmd
   pip install -r overlay_app\requirements.txt
   ```
3. **Execute the automated test suite**:
   ```cmd
   python overlay_app\run_all_tests.py
   ```

---

## Commit Guidelines
We follow the Conventional Commits specification:
- `feat(component): add new user-facing functionality`
- `fix(component): resolve a defect or bug`
- `docs: update documentation or architecture guides`
- `test(component): expand automated test coverage`
- `refactor(component): code structural changes with no behavior alteration`
- `security(component): security hardening, auth, or boundary enforcement`

---

## Submitting Pull Requests
1. Create a descriptive feature branch (`git checkout -b feat/my-improvement`).
2. Verify that all tests pass (`python overlay_app/run_all_tests.py`).
3. Commit your changes with atomic, descriptive commit messages.
4. Push your branch and open a Pull Request against `main`.
