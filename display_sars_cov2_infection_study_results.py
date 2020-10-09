'''display_sars_cov2_infection_study_results.py

This script is executed using the CMD tag in the Dockerfile
in order to display modeling study results to the console and
to an html site allocated on the host machine.
'''
from flask import Flask, render_template
from shutil import move
from os import getcwd

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('sars_cov2_modeling_study_results.html')

if __name__ == '__main__':
    import configure_flask_organization
    import simulation
    move(getcwd() + '/curated_k7_sars_cov2_infection_simulation.jpg', getcwd() + '/static')
    move(getcwd() + '/parameter_fitting_sars_cov2_infection_simulation.jpg', getcwd() + '/static')
    import gen_html_display
    move(getcwd() + '/sars_cov2_modeling_study_results.html', getcwd() + '/templates')
    from waitress import serve
    serve(app, listen='*:80')