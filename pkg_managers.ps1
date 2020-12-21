# - - - - - - Installing Scoop and Chocolatey - - - - - - - - -

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh'))


# - - - - - - - - Refresh environment variables - - - - - - - -

refreshenv

choco feature enable -n useRememberedArgumentsForUpgrades
