$users = gci c:\users\
foreach ($user in $users) {
  $userpath = "c:\users\$user\appdata\local\temp\dbutil_2_3.sys"
  $1 = test-path $userpath
  if ($1) {
    Remove-Item $userpath
  }
}