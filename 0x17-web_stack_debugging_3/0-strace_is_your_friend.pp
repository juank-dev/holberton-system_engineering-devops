# Strace is your friend and fix the error

exec { 'Strace':
  command  => 'sed -i "s/class-wp-locale.phpp/class-wp-locale.php/" /var/www/html/wp-settings.php',
  provider => 'shell',
}
