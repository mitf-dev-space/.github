# Mirror a GitLab repository to mitf-dev-space (mobile track)
param(
    [Parameter(Mandatory)][string]$GitLabUrl,
    [Parameter(Mandatory)][string]$GitHubName,
    [string]$Organization = "mitf-dev-space",
    [switch]$SkipCreate
)

$ErrorActionPreference = "Stop"

if (-not $GitLabUrl.EndsWith(".git")) { $GitLabUrl += ".git" }

$workDir = [System.IO.Path]::GetFullPath((Join-Path $env:TEMP "mitf-mirror-$GitHubName"))
$mirrorDir = Join-Path $workDir "mirror.git"

if (Test-Path $workDir) { Remove-Item -Recurse -Force $workDir }
New-Item -ItemType Directory -Path $workDir | Out-Null

Write-Host "Cloning mirror from $GitLabUrl ..."
git clone --mirror $GitLabUrl $mirrorDir
if ($LASTEXITCODE -ne 0) { throw "git clone --mirror failed" }

if (-not $SkipCreate) {
    $exists = gh repo view "$Organization/$GitHubName" 2>$null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Creating GitHub repo $Organization/$GitHubName ..."
        gh repo create "$Organization/$GitHubName" --private `
            --description "Migrated from GitLab: $GitLabUrl" `
            --team mobile
    } else {
        Write-Host "Repo $Organization/$GitHubName already exists — pushing mirror"
    }
}

Write-Host "Pushing mirror to GitHub ..."
$pushTarget = "https://github.com/$Organization/$GitHubName.git"
git -C $mirrorDir push --mirror $pushTarget
if ($LASTEXITCODE -ne 0) { throw "git push --mirror failed" }

Write-Host "Done: https://github.com/$Organization/$GitHubName"
Write-Host "Next: normalize branches, migrate secrets, add flutter-ci.yml"
