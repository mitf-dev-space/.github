# Rewrite pubspec path/git deps to GitHub URLs (package-first multi-repo)
param(
    [Parameter(Mandatory)][string]$RepoPath,
    [string]$Ref = "develop",
    [switch]$WhatIf
)

$ErrorActionPreference = "Stop"
$map = @{
    '../payment-core' = 'https://github.com/mitf-dev-space/mitf-payment-core.git'
    '../sharedcomponents' = 'https://github.com/mitf-dev-space/mitf-sharedcomponents.git'
    '../core-mobile-banking' = 'https://github.com/mitf-dev-space/mitf-core-mobile-banking.git'
    '../mobile-widgets' = 'https://github.com/mitf-dev-space/mitf-mobile-widgets.git'
    'http://10.10.20.51/front-end/banking/packages/ozmobile.git' = 'https://github.com/mitf-dev-space/mitf-ozmobile.git'
    'http://10.10.20.51/front-end/banking/packages/mitf-ocr.git' = 'https://github.com/mitf-dev-space/mitf-mobile-ocr.git'
    'http://10.10.20.51/front-end/banking/mobile-widgets.git' = 'https://github.com/mitf-dev-space/mitf-mobile-widgets.git'
}

$pubspecs = Get-ChildItem -Path $RepoPath -Filter pubspec.yaml -Recurse -File |
    Where-Object { $_.FullName -notmatch '\\\.git\\' }

foreach ($file in $pubspecs) {
    $content = Get-Content $file.FullName -Raw
    $original = $content

    foreach ($legacy in $map.Keys) {
        $gh = $map[$legacy]
        if ($content -match [regex]::Escape($legacy)) {
            Write-Host "Patching $($file.FullName): $legacy -> $gh"
        }
        # path: ../foo  -> git block
        $pathPattern = "(?m)^(\s+)(\w+):\s*\r?\n\1\s+path:\s*$([regex]::Escape($legacy))\s*$"
        $gitBlock = "`$1`${2}:`n`$1  git:`n`$1    url: $gh`n`$1    ref: $Ref"
        $content = [regex]::Replace($content, $pathPattern, $gitBlock)

        # git url replacement inside existing git blocks
        $content = $content.Replace($legacy, $gh)
    }

    # Remove commented PAT lines (security)
    $content = [regex]::Replace($content, '.*glpat-[A-Za-z0-9_-]+.*\r?\n', '')

    if ($content -ne $original) {
        if ($WhatIf) {
            Write-Host "[WhatIf] Would update $($file.FullName)"
        } else {
            Set-Content -Path $file.FullName -Value $content -NoNewline
        }
    }
}

Write-Host "Pubspec rewrite complete. Run: flutter pub get && flutter analyze"
