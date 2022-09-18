#creates a file with permissions and groups

file {'school':
    path    => '/tmp/school',
    content => 'I love Puppet',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    ensure  => 'present'
}
