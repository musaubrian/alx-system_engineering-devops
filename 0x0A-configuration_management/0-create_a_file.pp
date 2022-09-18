#creates a file with permissions and groups

file {'/tmp/school':
    content => 'I love puppet'
    recursive => false,
    owner => 'www-data',
    group => 'www-data',
    mode => 0744,
    

}
