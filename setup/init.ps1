Write-Host "Fetching IAM github-action-user ARN"
$userJson = aws iam get-user --user-name github-action-user | ConvertFrom-Json
$userarn = $userJson.User.Arn

Write-Host "Downloading tool..."
Invoke-WebRequest -Uri "https://github.com/kubernetes-sigs/aws-iam-authenticator/releases/download/v0.6.2/aws-iam-authenticator_0.6.2_windows_amd64.exe" -OutFile "aws-iam-authenticator.exe"

Write-Host "Updating permissions"
$kubeconfigPath = "$env:USERPROFILE\.kube\config"
.\aws-iam-authenticator.exe add user --userarn="$userarn" --username=github-action-role --groups=system:masters --kubeconfig="$kubeconfigPath" --prompt=$false

Write-Host "Cleaning up"
Remove-Item aws-iam-authenticator.exe
Write-Host "Done!"
