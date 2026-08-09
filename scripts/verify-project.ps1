$ErrorActionPreference = "Stop"

if (-not (Test-Path "package.json")) {
    Write-Host "No package.json detected. Run the repository's native validation commands instead."
    exit 0
}

$package = Get-Content "package.json" -Raw | ConvertFrom-Json
$manager = "npm"
if (Test-Path "pnpm-lock.yaml") { $manager = "pnpm" }
elseif (Test-Path "yarn.lock") { $manager = "yarn" }

foreach ($script in @("lint", "typecheck", "test", "build")) {
    if ($package.scripts.PSObject.Properties.Name -contains $script) {
        Write-Host "==> $manager $script"
        & $manager run $script
        if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
    }
}
