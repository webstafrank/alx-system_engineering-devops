# Killong the process named killmenow using pkill
exec { 'kill_killmenow_process':
  command => '/usr/bin/pkill -f killmenow',
  path    => ['/bin', '/usr/bin'],
  onlyif  => '/usr/bin/pgrep -f killmenow',
}
