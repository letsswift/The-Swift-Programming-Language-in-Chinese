#!/usr/bin/python
#coding=
#Filename:build.py
import glob,os,sys,shutil

cmd_template={'html':"pandoc %s -o output/html/%s.html --template=default.html",
              'pdf':'pandoc -N --toc --template=default.latex --latex-engine=xelatex %s -o output/pdf/%s.pdf',
              'beamer': 'pandoc -N -t beamer --toc --template=default.beamer --latex-engine=xelatex %s -o output/beamer/%s.pdf',
              'epub': 'pandoc %s -o output/epub/%s.epub'
             }

if __name__ == '__main__':
    if len(sys.argv) > 2:
        print 'Usage: build.py [pdf|html|epub|beamer]'
    else:
        out_type = 'html' if len(sys.argv) == 1 else sys.argv[1]
        assert(out_type in cmd_template)

    os.system('cat *.md > swift_book.mkd')
    cmd = [os.system(cmd_template[out_type] %(path, os.path.splitext(path)[0])) for path in glob.glob("*.md")]
    cmd += [os.system(cmd_template[out_type] %('swift_book.mkd', 'swift_book'))]
    print cmd

    if out_type == 'html':
        shutil.rmtree('output/html/pic')
        shutil.copytree("pic",'output/html/pic')
