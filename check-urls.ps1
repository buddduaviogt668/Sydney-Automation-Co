# check-urls.ps1 - Run before git push
\ = "https://sydneyautomationco.com.au"
\ = Get-ChildItem -Filter "*.html" | Where-Object { \.BaseName -ne "index" } | Select-Object -First 10

Write-Host "🔍 Testing 10 key pages..." -ForegroundColor Cyan
foreach (\ in \) {
  \https://search.google.com/search-console/inspect?url=https://sydneyautomationco.com.au/guides = "\/\"
  try {
    \ = Invoke-WebRequest -Uri \https://search.google.com/search-console/inspect?url=https://sydneyautomationco.com.au/guides -UseBasicParsing -TimeoutSec 10 -MaximumRedirection 0
    if (\.StatusCode -ne 200) {
      Write-Host "❌ \https://search.google.com/search-console/inspect?url=https://sydneyautomationco.com.au/guides → \" -ForegroundColor Red
      exit 1
    }
  } catch {
    Write-Host "❌ \https://search.google.com/search-console/inspect?url=https://sydneyautomationco.com.au/guides → \" -ForegroundColor Red
    exit 1
  }
}
Write-Host "✅ All pages returning 200 OK" -ForegroundColor Green
