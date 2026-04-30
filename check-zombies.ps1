# check-zombies.ps1 - Run before git push
\ = @('/services/', '/products/', '/Service/', '/shop/', '/wp-')
\ = Get-ChildItem -Filter "*.html" -Recurse | Get-Content -Raw

foreach (\(?s)(Service Areas.*?commercial specialisation.*?)(?=\n\s*<) in \) {
  if (\ -match [regex]::Escape(\(?s)(Service Areas.*?commercial specialisation.*?)(?=\n\s*<))) {
    Write-Host "⚠️ Found old WordPress pattern: \(?s)(Service Areas.*?commercial specialisation.*?)(?=\n\s*<)" -ForegroundColor Yellow
    exit 1
  }
}
Write-Host "✅ No zombie URL patterns found" -ForegroundColor Green
