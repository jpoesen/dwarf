This is demo content.

To get you started, either:

1. Rename the '_content' directory to 'content'  
   --> This will allow you to keep and manage the Dwarf app and its content
       in the same repository.

OR

2. create a content folder outside of the Dwarf app and symlink to it.
   Example:
     /var/www/example.com/content
     /var/www/example.com/content/authors/
     /var/www/example.com/content/blog/
     ...
     /var/www/example.com/dwarf/dwarf/
     /var/www/example.com/dwarf/dwarf/content <-- symlink to /var/www/example.com/content

   --> This will allow you to keep the Dwarf app in one repository and your
       content in another. Handy if you don't want to give your content team
       access to your code repository.


