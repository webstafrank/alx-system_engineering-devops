# instructions to create /tmp/school
file { '/tmp/school':
  ensure  => 'file',                # ensuring it s a regular file
  mode    => '0744',                # setting permission to 0744
  owner   => 'www-data',            # setting owner 
  group   => 'www-data',            # setting group
  content =>  'I love Puppet',      #file content
}
