#Get-ChildItem -Path C:\Users -Filter dbutil_2_3.sys -Recurse -ErrorAction SilentlyContinue -Force
#$users = gci c:\users
#Write-host $users
$found = @()
$users = gci c:\users\
foreach ($user in $users) {
  $userpath = "c:\users\$user\appdata\local\temp\dbutil_2_3.sys"
  $1 = test-path $userpath
  if ($1) {
    $found += $userpath
  }
}
$systemPath = "c:\windows\temp\dbutil_2_3.sys"
$2 = test-path $systemPath
if ($2) {
  $found += $2
}
$found | %{ write-host $_ }