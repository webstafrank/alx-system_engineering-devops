# Ensure Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Define a custom Nginx configuration file
file { '/etc/nginx/conf.d/custom_headers.conf':
  ensure  => present,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    # Define custom HTTP header X-Served-By
    location / {
        add_header X-Served-By $hostname;
        root /var/www/html;
        index index.html index.htm;
    }
}",
  require => Package['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/conf.d/custom_headers.conf'],
}
