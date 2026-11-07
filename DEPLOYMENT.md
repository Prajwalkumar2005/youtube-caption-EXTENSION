# Deployment & Release Workflow 📦

This guide outlines deployment procedures for open-source maintainers publishing **YouTube Desktop Lyrics Overlay**.

---

## 1. Release Checklist

1. **Version Synchronization**: Verify version numbers in:
   - `extension/manifest.json`
   - `CHANGELOG.md`
   - `overlay_app/main_overlay.py`
2. **Automated Test Validation**: Run all unit and integration tests:
   ```cmd
   python overlay_app/run_all_tests.py
   ```
3. **Build Artifacts**:
   - Package Chrome extension: `package_extension.bat`
   - Compile Windows standalone: `build_exe.bat`
4. **Publishing**:
   - Tag commit: `git tag v1.2.0`
   - Push tags: `git push origin --tags`
   - Upload `dist/yt-lyrics-overlay-extension.zip` and `overlay_app/dist/YT_Lyrics_Overlay.exe` to the GitHub Release.
