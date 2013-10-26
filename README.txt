========================================
DWARF, a tiny content publishing engine.
========================================

Dwarf is an out-in-the-open exercise in building a content publishing tool with `Python <http://python.org>`_ and `Flask <http://http://flask.pocoo.org/>`_ .

Dwarf currently wants to be a static site generator much like its heroes `Jekyll <http://jekyllrb.com/>`_ and `Pelican <http://blog.getpelican.com/>`_ . 

It has been mentioned that this is entirely possible in 50 lines of code with `Flask-FlatPages <http://pythonhosted.org/Flask-FlatPages/>`_ and `FrozenFlask <http://pythonhosted.org/Frozen-Flask/>`_ . There is truth to this. But no fun.

:strong:`But Darf is still a pipsqueek!`

Quite right, Dwarf is in its very early stages. It's in no way stable, scalable, secure, or a good idea in any way. 

:strong:`Where does Dwarf keep its stuff?`

No SQL. No NOSQL. All source content is stored in flat markdown files:


  /content/  

  /content/authors/  

  /content/authors/alice.md  

  /content/authors/_bob.md  

  /blog/example.md  

  /pages/about.md  


(Files starting with an underscore are assumed to be draft content and won't be
rendered publicly.)


:strong:`Your Dwarf is so pretty.`

Oh you. Out of the box Dwarf uses `Twitter's Bootstrap <http://getbootstrap.com>`_ to make itself purdy for gentleman callers.  Any lipstick will do though. Go nuts.


:strong:`What about pictures and discussions and such?`

Dwarf has lots of specialized friends, like `Gravatar <http://en.gravatar.com/>`_ for author avatars and `Disqus <http://disqus.com/>`_ to power comments, all ready to go.

Multimedia content will have to be hosted elsewhere for now - Dwarf has no intention of handling all that himself, though some kind of ajaxy wizardy interface to those third party thingies may be cooked up later.

:strong:`What holds the future?`

Right now we are assuming a lot of things and hiding behind 'convention over configuration' to justify lots of magicking about. We need to move stuff into a simple config file, write unit tests and produce documentation. Stabilize now, add features later. 

:strong:`Licence?`

Good question. How about the `BSD License <http://flask.pocoo.org/docs/license/>`_ , the same one `Flask <http://http://flask.pocoo.org/>`_ uses?
