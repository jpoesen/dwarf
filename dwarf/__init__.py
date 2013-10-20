# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from datetime import datetime
import hashlib, markdown, operator, os, sys

app = Flask(__name__)

# --- routes

@app.errorhandler(404)
def page_not_found():
    # TODO: write to log
    data = content_load(os.path.join(os.path.dirname(__file__), 'content/pages/404.md'))
    md = markdown.markdown(data)
    return render_template('page.tpl.html', page=md), 404

# @app.route("/")
# def index():
#     return dwarf_render_page('index')

# @app.route("/about/")
# def about():
#     return dwarf_render_page('about')

@app.route("/posts/<slug>")
def blogpost(slug):
    md = markdown.Markdown(extensions = ['meta'])
    data = content_load(os.path.join(os.path.dirname(__file__),"content/blog/{0}.md".format(slug)))
    markup = md.convert(data.decode('utf-8'))
    meta = _md_meta_to_dict(md)
    post = {'meta': meta, 'content': markup}
    return render_template('post.tpl.html', post=post)

@app.route("/")
def index():
     files=content_list('blog')
     newest_first = sorted(files, key=operator.itemgetter("date"), reverse=True)
     return render_template('posts.tpl.html', posts=newest_first)

def content_load(file):
    # TODO check if file exists, if exist: open, if not, open content/404.
    with open(file, "r") as f:
        data = f.read()
    return data

def content_list(content_type):
    md = markdown.Markdown(extensions = ['meta'])
    full_path = os.path.join(os.path.dirname(__file__), "content/{0}".format(content_type))
    files = os.listdir(full_path)

    content_items = []
    for fname  in files:
        data = content_load(os.path.join(os.path.dirname(__file__), "content/{0}/{1}".format(content_type, fname)))
        md.convert(data.decode('utf-8'))
        meta = _md_meta_to_dict(md)
        
        if 'date' in meta:
            meta['date'] = _jinja2_filter_datetime(meta['date'], '%Y-%m-%d')
        
        #Fall back to a default slug (straight filename) if necessary
        if not 'slug' in meta:
            meta['slug'] = fname[0: fname.find('.')] #filename without extension
          
        # Only add this item to the list if we're not currently looking at it.
        # 
        # Rationale: if we call this function from a route decorator, we're 
        # looking at a page view listing of content items (/posts), and the request object
        # will not contain views_arg 'slug'. 
        # 
        # However, if we're looking at a page view
        # of a specific content item (/posts/foo), the 'slug' views_arg will be 
        # set. This means that this function is probably called from a context
        # processor (for instance to show a sidebar block of content), in which 
        # case we want to exclude the item we're looking at (/posts/foo) from 
        # the list of content we're generating.
            
        if not meta['slug'] == request.view_args.get('slug', ''):
            content_items.append(meta) 
    
    return content_items

def dwarf_render_page(slug, template='page.tpl.html'):
    data = content_load(os.path.join(os.path.dirname(__file__), "content/pages/{0}.md".format(slug)))
    page = {'content': markdown.markdown(data)}
    return render_template(template, page=page)

# --- context processors

@app.context_processor
def utility_processor():
    def inject_author(identifier=''):
        md = markdown.Markdown(extensions = ['meta'])
        data = content_load(os.path.join(os.path.dirname(__file__), "content/authors/{0}.md".format(identifier)))
        markup = md.convert(data.decode('utf-8'))
        
        author = {}
        for key in md.Meta.keys():
            author[key] = md.Meta[key][0]
    
        author['bio'] = markup
        # store md5 hash of email so the template can use it to fetch gravatar image
        author['hash'] = hashlib.md5(author['email']).hexdigest()
        return author
    return dict(inject_author=inject_author)

@app.context_processor
def foo():
    return dict(foo='foo world')

# Returns the 4 most recent blog posts
@app.context_processor
def recent_posts():
    files=content_list('blog')
    newest_first = sorted(files, key=operator.itemgetter("date"), reverse=True)
    return dict(recent_posts=newest_first[:4])

@app.context_processor
def authors():
    files=content_list('authors')
    return dict(authors=files)


# --- template filters

@app.template_filter('strftime')
def _jinja2_filter_datetime(date, format='%b %d, %Y'):
    d = datetime.strptime(date, "%Y-%m-%d").date()
    return d.strftime(format)

# --- helpers

# grab markdown meta info and store in simple dict, key for key
# (to automatically make all meta items available in the template later on)
def _md_meta_to_dict(md):
    items = {}
    for key in md.Meta.keys():
        items[key] = md.Meta[key][0]
    return items


if __name__ == "__main__":
    app.run()
