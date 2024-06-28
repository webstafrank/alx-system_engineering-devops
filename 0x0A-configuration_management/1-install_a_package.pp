# Ensuring pip3 is installed
package { 'python3-pip':
  ensure => 'present',
}

# Installing Flask version 2.1.0 using pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => ['/bin', '/usr/bin'],
  unless  => 'pip3 show flask | grep Version | grep -q 2.1.0',
  require => Package['python3-pip'],
}
