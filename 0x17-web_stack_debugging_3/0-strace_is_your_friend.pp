# fix file extension typo
exec { 'replace phpp with php':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}

#restart apache2
exec { 'restart apache2 service':
  command  => 'service apache2 restart',
  provider => shell
}
