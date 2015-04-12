# manpage-du-jour

##RTFM!!!

Twitter bot to promote learning of Linux functions through the circulation of a 
'Man page' a day. Link: https://twitter.com/manpagedujour

With thanks to [@andreakbyrne](https://twitter.com/andreakbyrne) whose passion for learning through the Linux manual 
led to the development of the service. 

##Information

A tweet is created daily with a link to a Linux manual page. Generated from an 
index of Man pages, the specific page is generated at random and so there is a 
potential for collision every once in a while. 

The index is based on the Man pages available on the Man Pages Online project: 
http://man7.org/linux/man-pages/

##Shout-outs

During the course of my reseach I discovered that this type of Twitter feed was 
previously attempted here: https://twitter.com/manpageaday

There may be other options for those shopping around. 

##Index generation within Linux

To see the manpages available to you in your own distro, two commands can be 
followed:

     apropos . 
     
or

     whatis -r . 
