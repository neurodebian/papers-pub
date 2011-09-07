#!/bin/bash
#emacs: -*- mode: shell-script; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- 
#ex: set sts=4 ts=4 sw=4 noet:
#-------------------------- =+- Shell script -+= --------------------------
#
# @file      fetch.sh
# @date      Wed Aug 17 17:05:30 2011
# @brief
#
#
#  Yaroslav Halchenko                                            Dartmouth
#  web:     http://www.onerussian.com                              College
#  e-mail:  yoh@onerussian.com                              ICQ#: 60653192
#
# DESCRIPTION (NOTES):
#
# COPYRIGHT: Yaroslav Halchenko 2011
#
# LICENSE: MIT
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.
#
#-----------------\____________________________________/------------------
set -eu
#wget -Opopularities.html -nc 'http://distrowatch.com/stats.php?section=popularity' || :
mkdir -p distros
#echo -e "distribution\tcolor\tcount"
echo -e "distribution\tbase"

c_debian=cd013e #FF0000
c_redish=dc4c00 # ubuntu
c_redhat=0000FF
c_bluish=416fb2					# fedora
c_arch=AAAA00
c_color1=a098f6 #726c98 # gentoo
c_green=73ba25	# suse
c_color3=000000
c_color4=000000
c_color5=000000
c_color6=000000
c_pclinuxos=00AAAA
c_color8=000000
c_color9=000000
c_color10=000000
c_unknown=777777
IFS=:

function get_color() {
		case "$@" in
			*Ubuntu*)   color=$c_redish;;
			*Debian*)   color=$c_debian;;
			*Fedora*)   color=$c_bluish;;
			*Red\ Hat*) color=$c_redhat;;
			*Arch*)     color=$c_arch;;
			*rPath*)    color=$c_color6;;
			*Gentoo*)   color=$c_color1;;
			*SUSE*)     color=$c_green;;
			*Slackware*) color=$c_color4;;
			*BSD*)      color=$c_color5;;
			*PCLinuxOS*) color=$c_pclinuxos;;
			*Mandr*)    color=$c_color8;;
			*Solaris*)  color=$c_color9;;
			*Independent*) color=$c_color10;;
			*)          color=$c_unknown;;
		esac
		echo $color
}

#sed -n -e '/Last 12 months/,/Last 6/p' popularities.html \
#	| sed -n -e '/a href=/s,.*href="\([^"]*\)".*,\1,gp' \
#	| sed -n -e '/a href=/{ N; s/\n//g; s/.*href="\([^"]*\)".*>\([0-9][0-9]*\)<.*$/\1 \2/p }' \
sed -n -e '/Last 12 months/,/Last 6/p' popularities.html \
	| sed -n -e '/a href=/{ N; s/\n//g; s/.*href="\([^"]*\)">\([^<]*\)<.*>\([0-9][0-9]*\)<.*$/\1:\2:\3/p }' \
	| while read d name count; do
	    echo -n "Fetching $name which has $count, " >&2
		df=distros/$d.html
		#wget -q -nc -O $df http://distrowatch.com/table.php?distribution=$d || :
		# Figure out what it is based on
		#bases=$( sed -n -e '/Based on:/{ s,.*Based on:\(.*\)Origin:.*,\1,; s,<[^>]*>,,g; s/,//g; s/^ //g; p }' $df )
		bases=$( sed -n -e '/Based on:/{ s,.*Based on:\(.*\)Origin:.*,\1,; s,<[^>]*>,,g; s/, */:/g; s/^ //g; s/ *(.*) *//g; p }' $df )
		echo "based: $bases" >&2
		color=`get_color "$name"`
		[ $color != $c_unknown ] || color=`get_color "$bases"`
		#[ $color = unknown ] && echo "$d $bases"
		#echo -e "$d\t$color\t$count"
		for b in $bases; do
			if [ "$name" != "$b" ] && [ $b != "Independent" ] ; then
				echo -e "$name\t$b"
			fi
		done
		#[ $color = $c_debian ] || [ $color = $c_redish ] && \
		#[ $color = $c_redhat ] || [ $color = $c_bluish ] && \
		#echo -e "$name:$count:$color"
		# 135 -- debian based
		# 45 -- RedHat based
	done
