#!/bin/bash

fontsdir="fonts"
version="2.34"
filename="dejavu-fonts-$version.tar.bz2"
source="http://sourceforge.net/projects/dejavu/files/dejavu/$version/$filename"
wget "$source"
tar xjfv "$filename"

echo "Converting fonts"
mkdir -p "$fontsdir"
for font in "DejaVuSans dejavu-sans" "DejaVuSerif dejavu-serif" \
            "DejaVuSansMono dejavu-sans-mono"
do
   set -- $font
   from="dejavu-fonts-$version/src/$1.sfd"
   for format in svg ttf woff
   do
       to="$fontsdir/$2.$format"
       echo "$from > $to"
       ./generate.pe $from $to &> /dev/null
   done
   from="$fontsdir/$2.ttf"
   to="$fontsdir/$2.eot"
   echo "$from > $to"
   ttf2eot < $from > $to
done
