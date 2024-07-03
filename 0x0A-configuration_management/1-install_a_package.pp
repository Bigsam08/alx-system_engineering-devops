# Puppet manifest to install Flask using pip3
package { 'Flask':
  ensure   => '2.1.0',  # Ensure Flask is at version 2.1.0
  provider => 'pip3',   # Use pip3 as the package provider
}
# install werkzeug
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
