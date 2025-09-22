from jinja2 import Environment, FileSystemLoader
import os

def generate_summary(incident):
    template_loader = FileSystemLoader(searchpath=os.path.join(os.path.dirname(__file__), 'templates'))
    template_env = Environment(loader=template_loader)
    template = template_env.get_template('analyst_summary.md.j2')

    summary = template.render(incident=incident)
    return summary