#!/usr/bin/python
#coding=
#Filename:build.py
import glob,os,sys

cmd_template={'html':'pandoc %s -o output/%s.html --template=default.html',
              'pdf':'pandoc -N --toc --template=default.latex --latex-engine=xelatex %s -o %s.pdf',
              'beamer': 'pandoc -N -t beamer --toc --template=default.beamer --latex-engine=xelatex %s -o %s.pdf'
             }

if __name__ == '__main__':
    if len(sys.argv) > 2:
        print 'Usage: build.py [pdf|html]'
    else:
        out_type = 'html' if len(sys.argv) == 1 else sys.argv[1]
        assert(out_type in cmd_template)
    cmd = [os.system(cmd_template[out_type] %(path, os.path.splitext(path)[0])) for path in glob.glob("*.md")]
    print cmd
