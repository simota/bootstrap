import errno
import os

from jinja2 import Environment, PackageLoader, select_autoescape


class Generator:

    env = Environment(
        loader=PackageLoader('bootstrap', 'templates'),
        autoescape=select_autoescape(['html'])
    )

    def __init__(self,
                 directory=None,
                 name=None,
                 version=None,
                 description=None,
                 author=None,
                 email=None,
                 url=None):
        self.directory = directory
        self.name = name
        self.version = version
        self.description = description
        self.author = author
        self.email = email
        self.url = url

    def generate(self):
        self.create_directories()
        self.create_license()
        self.create_readme()
        self.create_manifest()
        self.create_requirements()
        self.create_setup()
        self.create_makefile()

        files = [
            'tests/__init__.py',
            'docs/__init__.py',
            '{}/__init__.py'.format(self.name)
        ]

        for file in files:
            self.create_file(file)

        self.create_test()

    def get_template(self, name):
        return self.env.get_template(name)

    def render_template(self, template_name=None, output=None, **kwargs):
        template = self.get_template(template_name)
        data = template.render(**kwargs)
        with open('{}/{}'.format(self.directory, output), 'w') as f:
            f.write(data)

    def create_directories(self):
        try:
            os.makedirs('{}/{}'.format(self.directory, self.name))
            os.makedirs('{}/docs'.format(self.directory))
            os.makedirs('{}/tests'.format(self.directory))
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

    def create_file(self, filename):
        with open('{}/{}'.format(self.directory, filename), 'w') as f:
            f.write('')

    def create_license(self):
        self.render_template(template_name='LICENSE.tpl',
                             output='LICENSE',
                             author=self.author,
                             year=2018)

    def create_readme(self):
        self.render_template(template_name='README.md.tpl',
                             output='README.md')

    def create_manifest(self):
        self.render_template(template_name='MANIFEST.in.tpl',
                             output='MANIFEST.in')

    def create_requirements(self):
        self.render_template(template_name='requirements.txt.tpl',
                             output='requirements.txt')

    def create_setup(self):
        self.render_template(template_name='setup.py.tpl',
                             output='setup.py',
                             name=self.name,
                             version=self.version,
                             description=self.description,
                             author=self.author,
                             email=self.email,
                             url=self.url)

    def create_makefile(self):
        self.render_template(template_name='Makefile.tpl', output='Makefile')

    def create_test(self):
        self.render_template(template_name='test_example.py.tpl',
                             output='tests/test_example.py')
