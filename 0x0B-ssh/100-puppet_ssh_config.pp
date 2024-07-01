# Puppet manifest to configure SSH client settings

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => template('ssh_config.erb'),
}

# Template for ssh_config
