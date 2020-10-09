'''model_fitting.py

This file contains a class, model_fitting, with helper functions to enable
the parameter estimation stage of the COMBINE_2020_reproducibility_tutorial.
While these routines enable basic functionality for the tutorial, please
consider using the Python parameter fitting package, SBstoat, in your work
with Tellurium. Development of SBstoat is still underway.

Alternatively, pyPESTO could be used.'''
import tellurium as te
import numpy as np
import scipy
import random

class model_fitting:
    def __init__(self, data_file, antimony_str, parameter_list, seed_val = None):
        self.data = np.genfromtxt(data_file, dtype=float, delimiter=',')[1:,:]
        self.model = te.loada(antimony_str)
        self.time_start = self.data[0, 0]
        self.time_end = self.data[len(self.data) - 1, 0]
        self.timepoints = len(self.data)
        self.parameter_list = parameter_list
        self.seed_val = seed_val

    def simulate_model(self, s):
        '''model() takes an input parameter set, s, and performs a simulation of the model'''
        self.model.reset()
        for index, p in enumerate(self.parameter_list):
            self.model.setValue(p, s[index])
        return self.model.simulate(self.time_start, self.time_end, self.timepoints)

    def rmse(self, s):
        '''rmse() is the objective function to be minimized using differential evolution.
         rmse() takes a set of parameters, s, computes the output of the model using that set of parameters
         and calculates the root mean square error by computing the sum of the squared differences between
         each datapoint and the predicted model value, divided by the number of datapoints.'''
        model_prediction = self.simulate_model(s)
        species_sum = sum((self.data - model_prediction) ** 2) / len(self.data)
        return sum(species_sum)

    def residuals(self, s):
        '''residuals() calculates the deviations between experimental data used for model fitting
        and the simulated trajectory of the model.'''
        return self.data - self.simulate_model(s)

    def differential_evolution(self):
        '''This is simply an implementation of scipy's differential evolution function.
        It is used only for the purpose of demonstrating an optimization routine for
        the COMBINE 2020 reproducibility tutorial and is not the author's work.'''
        return scipy.optimize.differential_evolution(self.rmse, [(0.00001, 20)] * len(self.parameter_list), strategy='best1bin',
                                              maxiter=None, seed = self.seed_val,
                                              popsize=15, tol=0.01, mutation=(0.5, 1), recombination=0.7)

    def monte_carlo(self, num_itr = 10):
        '''Monte Carlo - this function will repeat differential evolution for
        a specified number of iterations and store the minimized parameter
        values from each iteration so that the user can determine how confident
        they are in the initial predicted parameter values. Each iteration in
        Monte Carlo produces new training data.'''
        parameter_lists = []
        model_fit_params = self.differential_evolution()
        for itr in range(num_itr):
            converged = False
            random_residual_matrix = np.zeros((np.shape(self.data)[0], np.shape(self.data)[1]))
            for row in range(np.shape(self.data)[0]):
                random_residual_matrix[row] = random.choice(self.residuals(model_fit_params.x))
            self.data = random_residual_matrix + self.simulate_model(model_fit_params.x)
            self.model.reset()
            while not converged:
                try:
                    model_fit_params = self.differential_evolution()
                    parameter_lists.append(list(model_fit_params.x))
                    converged = True
                    self.model.reset()
                except:
                    continue
        return parameter_lists

    def fitted_percentile(self, percentile = 95, num_itr = 10):
        '''fitted_percentile - this function executes Monte Carlo simulations to
        optimize the model parameters, and returns the confidence interval
        for the specified percentile.'''
        mc_parameters = self.monte_carlo(num_itr=num_itr)
        parameter_upper_bound = np.percentile(mc_parameters, (100-percentile)/2 + percentile, axis=0)
        parameter_lower_bound = np.percentile(mc_parameters, percentile - (100-percentile)/2, axis=0)
        fitted_parameter_data = dict([('CI_lower', list(parameter_lower_bound)), ('CI_upper', list(parameter_upper_bound)), ('Fitted_parameter_sets', mc_parameters)])
        return fitted_parameter_data