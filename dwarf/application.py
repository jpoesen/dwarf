#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, url_for
from datetime import datetime
import hashlib, markdown, operator, pagination, os, sys

app = Flask(__name__)

app.config.from_object('config.ProductionConfig')
app.template_folder = app.config['TEMPLATE_PATH']

# --- routes

@app.errorhandler(404)
def page_not_found():
    # TODO: write to log
    data = content_load('pages/404.md')
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
    data = content_load("blog/{0}.md".format(slug))
    markup = md.convert(data.decode('utf-8'))
    meta = _md_meta_to_dict(md)
    post = {'meta': meta, 'content': markup}
    return render_template('post.tpl.html', post=post)

@app.route('/', defaults={'page': 1})
@app.route('/page/<int:page>')
def index(page):
     files=content_list('blog')
     newest_first = sorted(files,
                           key=operator.itemgetter("date"),
                           reverse=True)
     count        = len(newest_first)
     newest_first = get_newest_first_for_page(
         newest_first , page, pagination.PER_PAGE)
     if not newest_first and page != 1:
        raise
     pagination_ = pagination.Pagination(
         page, pagination.PER_PAGE, count)
     return render_template('posts.tpl.html',
                    pagination=pagination_,
                            posts=newest_first )
     
def get_newest_first_for_page(newest_first , page, per_page):
    if page == 1 :return newest_first[:per_page]
    start = (page-1) * per_page
    try:
        return newest_first[start : start + per_page ]
    except :
        return None

def content_load(filename):
    # TODO check if file exists, if exist: open, if not, open content/404.
    with open(app.config['CONTENT_PATH'] + filename, "r") as f:
        data = f.read()
    return data

def content_list(content_type):
    md = markdown.Markdown(extensions = ['meta'])
    files = os.listdir(app.config['CONTENT_PATH'] + content_type)

    content_items = []
    for fname  in files:
        data = content_load("{0}/{1}".format(content_type, fname))
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
    data = content_load("pages/{0}.md".format(slug))
    page = {'content': markdown.markdown(data)}
    return render_template(template, page=page)

# --- context processors

@app.context_processor
def utility_processor():
    def inject_author(identifier=''):
        md = markdown.Markdown(extensions = ['meta'])
        data = content_load("authors/{0}.md".format(identifier))
        markup = md.convert(data.decode('utf-8'))
        
        author = {}
        for key in md.Meta.keys():
            author[key] = md.Meta[key][0]
    
        author['bio'] = markup
        # store md5 hash of email so the template can use it to fetch gravatar image
        author['hash'] = hashlib.md5(author['email']).hexdigest()
        return author
    return dict(inject_author=inject_author)

# Returns the 4 most recent blog posts
@app.context_processor
def recent_posts():
    files=content_list('blog')
    newest_first = sorted(files, 
                    key=operator.itemgetter("date"), 
                    reverse=True)
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

def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)
    
app.jinja_env.globals['url_for_other_page'] = url_for_other_page

if __name__ == "__main__":
    app.run()
