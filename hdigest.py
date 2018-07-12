#!/bin/env python3

from subprocess import *
import sys, re


def error_print(*args, **kwargs):
    exit = kwargs.pop('do_exit', False)
    print(*args,**kwargs, file=sys.stderr)
    if exit:
        sys.exit(1)

def main():
    gcc_exists = run(args=['which', 'gcc', 'grep'], stderr=STDOUT, stdout=DEVNULL)

    if (gcc_exists.returncode > 0):
        error_print('install gcc :.:', do_exit=True)
    elif ('-h' in sys.argv) or (len(sys.argv) < 3):
        error_print('uage: ./script [-I dirs] sourcefile.c <perl_regex_pattern>', do_exit=True)
    moar_include_dirs,source_file,pattern = sys.argv[1:-2] , sys.argv[-2], sys.argv[-1]

    headers_job = run(['gcc', *moar_include_dirs, '-H', source_file, '-o', '/dev/null'], stderr=STDOUT, stdout=PIPE  )
    headers_out = headers_job.stdout.decode('utf-8','ignore')

    header_files = set()

    for hline in headers_out.split('\n'):
        if '!' in hline:
            error_print('BROKEN HEADER THING: {}'.format(hline))
            continue
        else:
            path_match = re.search("/.+", hline)
            if path_match:
                header_files.add( path_match.group(0) )

    for hpath in header_files:
        temp_process = run(args=['grep', '-P', pattern, hpath], stderr=STDOUT, stdout=DEVNULL)
        if temp_process.returncode == 0:
            print(hpath)

    debug = False
    if debug:
        print(*header_files, sep='\n||')



if __name__=='__main__':
    main()
    
