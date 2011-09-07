#!/usr/bin/python
#emacs: -*- mode: python-mode; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*- 
#ex: set sts=4 ts=4 sw=4 noet:
#------------------------- =+- Python script -+= -------------------------
"""
 @file      plot_popcons.py
 @date      Fri Aug 19 09:53:24 2011
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

import gzip, re
import numpy as np
import pylab as pl
deb_fname = 'debian-popcon-numscipy-20110818.gz'
ubu_fname = 'ubuntu-popcon-numscipy-20110818.gz'

RE_LINE = re.compile("""^(?P<date>[-0-9]*)(?P<crap>.txt)? *(?P<submissions>\d*) """)
RE_PKG = re.compile("""python-(?P<name>[a-z]*py) +(?P<n1>\d+) +(?P<n2>\d+) +(?P<n3>\d+) +(?P<n4>\d+)""")

def get_data(fname):
    dates, data = [], []
    for l in gzip.open(fname).readlines():
        res = RE_LINE.search(l)
        if res:
            #print res.groupdict()
            start = 0
            pkgs = {}
            while True:
                res_pkgs = RE_PKG.search(l[start:])
                if not res_pkgs:
                    break
                d = res_pkgs.groupdict()
                pkgs[d['name']] = [int(d['n%s'%x]) for x in xrange(1,5)]
                start += res_pkgs.span()[-1]
            #print pkgs
            if len(pkgs) == 2:           # need both numpy and scipy
                dates.append(res.groupdict()['date'])
                data.append([int(res.groupdict()['submissions']),
                             sum(pkgs['numpy']), sum(pkgs['scipy'])])
    return [pl.num2date(pl.datestr2num(x)) for x in dates], np.asarray(data)

plot_f = pl.plot
deb_dates, deb_data = get_data(deb_fname)
ubu_dates, ubu_data = get_data(ubu_fname)

dcolor = 'r' # '#cd013e'
ucolor = 'b' # '#dc4c00'
sd_n = dict(linewidth=3, color=dcolor)
sd_s = dict(linewidth=2, color=dcolor, linestyle='--')
su_n = dict(linewidth=3, color=ucolor)
su_s = dict(linewidth=2, color=ucolor, linestyle='--')

kfs = dict(figsize=(10, 7))
if True:
    fig = pl.figure(**kfs); ax = pl.gca()
    deb_line_numpy = plot_f(deb_dates, deb_data[:, 1], label="NumPy (Debian)"   , **sd_n)
    deb_line_scipy = plot_f(deb_dates, deb_data[:, 2], label="SciPy (Debian)"   , **sd_s)
    ubu_line_numpy = plot_f(ubu_dates, ubu_data[:, 1]/10, label="NumPy (Ubuntu)", **su_n)
    ubu_line_scipy = plot_f(ubu_dates, ubu_data[:, 2]/10, label="SciPy (Ubuntu)", **su_s)
    pl.ylabel('# of Debian installations')
    pl.legend(loc='upper left')
    #xlim = ax.get_xlim()
    #years_ticks = [x.get_text() for x in ax.xaxis.get_ticklabels()]
    #ax.hold()
    pl.grid()
    ax2 = ax.twinx()
    #ax.xaxis.reset_ticks()
    ax.xaxis.set_major_locator(
        pl.matplotlib.dates.YearLocator()
        )
    ax.xaxis.set_major_formatter(
        #pl.matplotlib.dates.DateFormatter('%a %d\n%b %Y')
        pl.matplotlib.dates.DateFormatter('%Y')
        )
    #fig.autofmt_xdate()
    ax2.set_ylabel('# of Ubuntu installations')
    def update_ax2(ax):
        y1, y2 = ax.get_ylim()
        ax2.set_ylim(y1*10, y2*10)
        ax2.figure.canvas.draw()
    # automatically update ylim of ax2 when ylim of ax1 changes.
    ax.callbacks.connect("ylim_changed", update_ax2)
    update_ax2(ax)
    fig.savefig('pyes_counts.svg')

if True:
    fig = pl.figure(**kfs)
    line_numpy     = plot_f(deb_dates, 100.0*deb_data[:, 1]/deb_data[:, 0], label="NumPy (Debian)", **sd_n)
    line_scipy     = plot_f(deb_dates, 100.0*deb_data[:, 2]/deb_data[:, 0], label="SciPy (Debian)", **sd_s)
    ubu_line_numpy = plot_f(ubu_dates, 100.0*ubu_data[:, 1]/ubu_data[:, 0], label="NumPy (Ubuntu)", **su_n)
    ubu_line_scipy = plot_f(ubu_dates, 100.0*ubu_data[:, 2]/ubu_data[:, 0], label="SciPy (Ubuntu)", **su_s)
    pl.ylabel('% of all installations')
    pl.legend(loc='upper left')
    pl.grid()
    fig.savefig('pyes_percents.svg')
    fig.gca().set_ylim(0, 3)
    fig.gca().set_xlim(732398+(734367-732398)*0.6), 734367)
    ax = pl.gca()
    ax.xaxis.set_major_locator(
        pl.matplotlib.dates.YearLocator()
        )
    ax.xaxis.set_major_formatter(
        #pl.matplotlib.dates.DateFormatter('%a %d\n%b %Y')
        pl.matplotlib.dates.DateFormatter('%Y')
        )

    fig.savefig('pyes_percents_zoom.svg')

print fig.gca().get_xlim()
pl.show()
