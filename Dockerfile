FROM python:3.8

ENV PYTHONUNBUFFERED 1

# set working directory
WORKDIR /COMBINE_2020_reproducibility_tutorial

# add COMBINE 2020 modeling workflow files to Docker image
COPY . .

# install software dependencies within Docker image
RUN pip3 install tellurium
RUN pip3 install flask
RUN pip3 install waitress

# specify commands to execute simulations
CMD ["python", "./display_sars_cov2_infection_study_results.py"]