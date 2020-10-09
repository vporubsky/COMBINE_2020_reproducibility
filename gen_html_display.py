'''gen_html_display.py

This script is used to generate the html specifications for
displaying modeling study results in the Docker container.
'''
from os import getcwd
from shutil import move

f = open('sars_cov2_modeling_study_results.html', 'w')

message = """<!DOCTYPE html>
<html>
<style>
.textbox{
border:1px 	#A9A9A9;
border-radius: 10px;
display:inline-block;
width:auto;
height:auto;   
padding: 20px;
background-color: #A9A9A9;
}
.tb1 {}
}
}
</style>
<head></head>
<body style="background-color:black;">
<h1 style="font-family:Arial; color:#A9A9A9"> COMBINE 2020 Reproducible Biochemical Modeling Tutorial </h1>
<br>
<textbox class = "textbox tb1"; style="font-family:Arial; font-size:20px"; >Results of executing simulation.py:</textbox>
<br>
<br>
<img src="/static/curated_k7_sars_cov2_infection_simulation.jpg" alt="curated k7 sars-cov2 infection model simulation results" width="700" height="500">
<br>
<br>
<textbox class = "textbox tb1"; style="font-family:Arial; font-size:20px"; >Results of executing parameter_estimation.py:</textbox>
<br>
<br>
<img src="/static/parameter_fitting_sars_cov2_infection_simulation.jpg" alt="simulation with fitted parameters displayed on experimental data" width="700" height="500">
</body>
</html>"""

f.write(message)
f.close()