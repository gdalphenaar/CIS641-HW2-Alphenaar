import sys
from flask_bootstrap import (
    Bootstrap,
)
from flask import (
    Flask,
    render_template,
    redirect,
    render_template_string,
    Markup,
)
from flask_flatpages import (
    FlatPages,
    pygmented_markdown
)
from flask_frozen import (
    Freezer,
)


# setup stuff
app = Flask(__name__)
Bootstrap(app)
pages = FlatPages(app)
freezer = Freezer(app)
repo = 'CIS641-HW2-Alphenaar' # change to github repo name


# configuration stuff
def prerender_jinja(text):
    prerendered_body = render_template_string(Markup(text))
    return pygmented_markdown(prerendered_body)
app.config['FLATPAGES_HTML_RENDERER'] = prerender_jinja
app.config['FLATPAGES_EXTENSION'] = '.md'
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
app.config['FREEZER_DESTINATION'] = './docs'


# home page
@app.route('/')
def index():
    return render_template('index.html', title='Home')


# about me page
@app.route('/about-me/')
def about():
    return render_template('about-me.html', title='About Me')


# page to hold ''blog posts''
@app.route('/projects/')
def projects():
    latest = sorted(pages, reverse=True, key=lambda p: p.meta['date'])
    published = (p for p in latest if 'published' in p.meta)
    return render_template('projects.html', pages=published)


# markdown ''blog'' pages
@app.route('/projects/<path:path>/')
def page(path):
    template = pages.get_or_404(path)
    return render_template('page.html/', title=template['short-title'], page=template)


# freezes app and serves static files - to run normally, use Flask run
if __name__ == '__main__':
    app.config['FREEZER_BASE_URL'] = 'http://localhost{}'.format('/'+repo)
    freezer.freeze()  # freeze
    freezer.run(debug=True)  # serve
