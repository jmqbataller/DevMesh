$ErrorActionPreference = "Stop"
Write-Host "== DevMesh: project inspection =="
Write-Host "`n-- location --"
Get-Location

if (Get-Command git -ErrorAction SilentlyContinue) {
    git rev-parse --is-inside-work-tree 2>$null | Out-Null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`n-- git status --"
        git status -sb
        Write-Host "`n-- branch --"
        git branch --show-current
        Write-Host "`n-- remotes --"
        git remote -v
    }
}

Write-Host "`n-- common project files --"
$files = @("AGENTS.md", "README.md", "package.json", "pnpm-lock.yaml", "yarn.lock", "package-lock.json", "pyproject.toml", "requirements.txt", "composer.json", "go.mod", "Cargo.toml", "vercel.json")
foreach ($file in $files) {
    if (Test-Path $file) { Write-Host $file }
}
