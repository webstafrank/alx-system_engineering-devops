# 0-strace_is_your_friend.pp
# This Puppet manifest fixes a 500 error caused by incorrect permissions on the WordPress directory

exec { 'fix-wordpress-permissions':
  command => '/bin/chown -R www-data:www-data /var/www/html',
  onlyif  => '/usr/bin/test $(stat -c %U /var/www/html) != www-data',
}

exec { 'install-missing-php-modules':
  command => '/usr/bin/apt-get install -y php-mysql',
  unless  => '/usr/bin/php -m | grep -q mysql',
}

