#!/usr/bin/python
#emacs: -*- mode: python-mode; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*- 
#ex: set sts=4 ts=4 sw=4 noet:
#------------------------- =+- Python script -+= -------------------------
"""
 @file      ipythonians.py
 @date      Fri Aug 19 15:25:56 2011
 @brief


  Yaroslav Halchenko                                            Dartmouth
  web:     http://www.onerussian.com                              College
  e-mail:  yoh@onerussian.com                              ICQ#: 60653192

 DESCRIPTION (NOTES):

 COPYRIGHT: Yaroslav Halchenko 2011

 LICENSE: MIT

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
  THE SOFTWARE.
"""
#-----------------\____________________________________/------------------

__author__ = 'Yaroslav Halchenko'
__revision__ = '$Revision: $'
__date__ = '$Date:  $'
__copyright__ = 'Copyright (c) 2011 Yaroslav Halchenko'
__license__ = 'GPL'

import re
from debian import deb822

f = '/var/lib/apt/lists/debian.lcs.mit.edu_debian_dists_sid_main_binary-amd64_Packages'
f = '/var/lib/apt/lists/ftp.debian.de_debian_dists_sid_main_binary-amd64_Packages'

pkgs = {}
for p in deb822.Deb822.iter_paragraphs(open(f)):
    depends = ','.join((p.get('Depends', ''), p.get('Recommends','')))
    if ('python-numpy' in depends) \
           or ('python-scipy' in depends) \
           or p['Package'] in ('python-numpy', 'ipython', 'python-matplotlib', 'python-sphinx'):
        p['depends'] = [re.sub(" *\(.*\)?", "", x) for x in depends.split(',')]
        pkgs[p['Package']] = p

# now lets process, filter it, and give it names

# remove leading 'python-'
for pkg in pkgs.keys():
    pkgs[pkg]['name'] = name = re.sub('^python-', '', pkg)
    con_name = re.sub('-(lib|data|dbg|doc)$', '', pkg)
    if con_name != pkg and con_name in pkgs:
        # we need to pop this beast out
        print "popping ", pkg, " having name ", name, " con_name ", con_name
        pkgs.pop(pkg)

for p in 'shogun-python', 'shogun-elwms', 'science-mathematics-dev', 'science-nanoscale-physics', 'science-numericalcomputation', 'science-nanoscale-physics', 'science-statistics':
    if p in pkgs:
        pkgs.pop(p)

# replace binary pkgs with source pkgs
for p in pkgs.keys():
    pkg = pkgs[p]
    if 'Source' in pkg:
        src = re.sub(" *\(.*\)?", "", pkg['Source'])
        pkg['source'] = src
    else:
        pkg['source'] = p

# infiltrate 'depends' and replace with source names
for p in pkgs.keys():
    #pkgs[p]['depends'] =
    pkgs[p]['depends'] = \
          sorted(set([pkgs[pd.strip()]['source']
                      for pd in pkgs[p]['depends']
                      if pd.strip() in pkgs]))
def print_uses(pkgs):
    print "package\tusers"
    for pkg in pkgs.itervalues():
        for p in pkg['depends']:
            print '%s\t%s' % (pkg['source'], p)

# print_uses(pkgs)
if False:
    # let's try graphviz to plot something fance
    import pydot
    g = pydot.Dot()

    for pkg in pkgs.itervalues():
        pkg['node'] = node = pydot.Node(pkg['source'])
        g.add_node(node)

    for pkg in pkgs.itervalues():
        for p in pkg['depends']:
            pkg['edge'] = edge = pydot.Edge(pkg['source'], p)
            g.add_edge(edge)
    g.set_resolution('300')
    g.set_size('100,100')
    open('/tmp/1.dot', 'w').write(g.to_string())
    open('/tmp/1.jpg', 'w').write(g.create(prog='twopi', format='jpe'))

def load_pkgs_popcon(fname):
    # what about just a regular tag cloud based on popcon?
    import gzip, re
    counts = {}
    for l in gzip.open(fname).readlines():
        if l.startswith('Package:'):
            es = re.split('  *', l[9:].strip())
            counts[es[0]] = sum([int(x) for x in es[1:]])
    return counts

if True:
    popcons = load_pkgs_popcon('popcon/all-popcon-results.gz')
    spopcons = {}
    for pkg in pkgs.itervalues():
        spkg = pkg['source']
        descr = pkg['Description'].split('\n')[0]
        popcon = popcons[pkg['Package']]
        old = spopcons.get(spkg, (0, None))
        if old[0] < popcon:
            spopcons[spkg] = (popcon, descr)
    #fout = open('popcon-counted.txt', 'w')
    #for n, c in sorted(spopcons.iteritems()):
    #     fout.write(' '.join([n]*c) + '\n')
    #fout.close()

    #for spkg in sorted(spopcons.keys()):
    #    print '%s"%s",\t#%s' % (' '*(20-len(spkg)), spkg, spopcons[spkg][1])
    from numpy_deps_groupped import *
    import numpy as np
    for (g,c), l in numpy_dependents.iteritems():
        for pname in l:
            pname_ = pname.replace('python-', '')
            popcon = spopcons[pname][0]
            print '%s:%s:%s' % (pname_, np.log(popcon+1), c)
