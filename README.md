# manpage-du-jour

##RTFM!!!

Twitter bot to promote learning of Linux functions through the circulation of a 'Man page' a day. Link: https://twitter.com/manpagedujour

With thanks to @andreakbyrne whose passion for learning through the Linux manual led to the development of the service. 

##Information

A tweet is created daily with a link to a Linux manual page. Generated from an index of Man pages, the specific page is generated at random and so there is a potential for collision every once in a while. 

The index is based on the Man pages available on Ubuntu 14.04. 

##Index generation

Index generation can be done through two commands:

     apropos . 
     
or

     whatis -r . 
     
