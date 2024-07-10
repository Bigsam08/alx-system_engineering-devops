# Update package
exec { 'apt-update':
  command => '/usr/bin/apt-get -y update',
  path    => ['/usr/bin', '/bin']
}

# Install Nginx package
package { 'nginx':
  ensure => installed
}

# HTML file
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# add the custom HTTP header in nginx config
file_line { 'add custom header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By ${hostname};",
  after  => 'server_name _;',
}

service { 'nginx':
  ensure => running,
}
