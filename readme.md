# DWARF, a tiny content publishing engine.

Dwarf is an out-in-the-open exercise in building a content publishing tool with [python](http://python.org) and [Flask]().

Dwarf currently wants to be a static site generator very much like its heroes [Jekyll](http://jekyllrb.com/) and [Pelican](http://blog.getpelican.com/). 

It has been mentioned that this is entirely possible in 50 lines of code with [Flask-FlatPages](http://pythonhosted.org/Flask-FlatPages/) and [FrozenFlask](http://pythonhosted.org/Frozen-Flask/). There is truth to this. But no fun.

**But Darf is still a pipsqueek!**

Quite right, Dwarf is in its very early stages. It's in no way stable, scalable, secure, or a good idea. 

**Installation**

Core requirements: python 2.7 + pip

OPTION 1: use pip
<pre>
  $ pip install Dwarf
</pre>
--> note: package may not be 100% up-to-date

OPTION 2: the long and laborious hard way: 

* git clone dwarf

* create a virtual environment with virtualenv

  <pre>
  $ cd /path/to/my/dwarf
  $ virtualenv venv_dwarf
  </pre>

* activate the virtual env

  <pre>
  $ source venv_dwarf/bin/activate
  </pre>

* set up Dwarf's dependencies within your virtual environment

  <pre>
  $ cd /path/to/my/dwarf/location
  $ pip install -r requirements.txt
  </pre>

* run dwarf

  <pre>
  $ python dwarf/application.py
  </pre>

**Where does Dwarf keep its stuff?**

No SQL. No NOSQL. All source content is stored in flat markdown files:

<pre>
  /content/  
  /content/authors/  
  /content/authors/alice.md  
  /content/authors/_bob.md  
  /blog/example.md  
  /pages/about.md  
</pre>

(Files starting with an underscore are assumed to be draft content and won't be
rendered publicly.)


**Your Dwarf is so pretty.**

Oh you. Out of the box Dwarf uses [Twitter's Bootstrap](http://getbootstrap.com) to make itself purdy for gentleman callers.  Any lipstick will do though. Go nuts.

**What about pictures and discussions and such?**

Dwarf has lots of specialized friends, like [Gravatar](http://en.gravatar.com/) for author avatars and [Disqus](http://disqus.com/) to power comments, all ready to go.

Multimedia content will have to be hosted elsewhere for now - Dwarf has no intention of handling all that himself, though some kind of ajaxy wizardy interface to those third party thingies may be cooked up later.

**What holds the future?**

Right now we are assuming a lot of things and hiding behind 'convention over configuration' to justify lots of magicking about. We need to move stuff into a simple config file, write unit tests and produce documentation. Stabilize now, add features later. 

**Licence?**

Good question. How about the [BSD Licence](http://flask.pocoo.org/docs/license/), the same one [Flask](http://flask.pocoo.org) uses?
