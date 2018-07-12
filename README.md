# hdigest

a simple script that uses GCC's header listing capability and grep to find where the hell definitions are

### arguments:
    ./hdigest.py [-I extra_include_dir] <sourcefile> <PERL-like regex pattern>

###usage example:
    $> ./hdigest.py -I /usr/include/ pipe.c 's\w+ stat'

    /usr/include/bits/waitstatus.h
    /usr/include/stdlib.h
    /usr/include/bits/types/__mbstate_t.h
