git --version
git add .
git commit -m " Ensure plot window works in the frozen .exe"
git push origin main

:: === Tagging for GitHub Actions Release Build ===
git tag v2.8
git push origin v2.8
pause
