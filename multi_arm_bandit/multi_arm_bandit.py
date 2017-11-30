#!/usr/bin/env python

'''
Reinforcement Learning Homework
Prof: Francisco Melo
problem: multi-arm bandit
'''

import numpy as np
import math
import matplotlib.pyplot as plt
from numpy.random import choice

class MultiArmBandit(object):
    '''
    Solution to homework 1 of RL
    '''
    def __init__(self):
        # homework (fixed) parameters
        self.number_of_bandits = 10 # the amount of bandit machines that we have
        self.bandits_mean_reward = 0.0 # in average the bandits will give you no reward (might loose, might win)
        self.bandits_variance = 1.0 # bandit average reward is allowed to deviate this much w.r.t. self.bandits_mean_reward
        self.reward_variance = 1.0 # bandit reward is allowed to deviate this much w.r.t. the bandit mean (self.bandit_average_rewards[bandit_number])
        self.large_optimistic_init_value = 100.0 # the optimistic initialization (big) value
        self.number_of_times_to_play = 1000 # the number of times to play the bandits
        self.e = 0.3 # the tradeoff between explotation and exploration e-greedy parameter. it will allow for this much percentage of exploration (e.g. 30%)
        self.eta = 0.01 # botlzman policy param: control the tradeoff between uniform and greedy policy

        # compute n random rewards for all bandits (n=number_of_bandits)
        self.bandit_average_rewards = self.compute_multiple_bandit_average_reward(self.number_of_bandits)
        print 'Bandits will provide in average this rewards :'
        print self.bandit_average_rewards
        
        # initialize bandit values
        self.q_na_estimate = self.optimistic_init(self.large_optimistic_init_value)
        print 'Bandits initial values :'
        print self.q_na_estimate
        
        # to store the maximum amount of iterations per bandit for plotting purposes
        self.max_x_range = 0


    def sample_gaussian(self, mean, variance):
        '''
        generate a random number with gaussian dist, mean = 0 and variance = 1
        This number is meant to be the average return value of a bandit
        '''
        standard_deviation = math.sqrt(variance)
        return round(np.random.normal(mean, standard_deviation, 1).tolist()[0], 4)


    def compute_multiple_bandit_average_reward(self, number_of_bandits):
        '''
        call sample_gaussian function n times
        n being the number of bandits and store its values on a dictionary
        '''
        bandit_rewards = []
        for i in range(0, 10):
            random_reward = self.sample_gaussian(self.bandits_mean_reward, self.bandits_variance)
            bandit_rewards.append(random_reward)
        return bandit_rewards


    def compute_reward(self, bandit_number):
        '''
        returns a random variable with a gaussian distribution
        '''
        mean = self.bandit_average_rewards[bandit_number]
        return self.sample_gaussian(mean, self.reward_variance)


    def optimistic_init(self, large_value):
        '''
        All equal and set to large values
        '''
        bandit_init_values = []
        for i in range(0, self.number_of_bandits):
            bandit_init_values.append(large_value)
        return bandit_init_values


    def update_q_a_estimate(self, new_sample, na, bandit_index):
        '''
        Q^(a) : expected value function
        new_sample = r na + 1 = the new reward
        na - number of times that particular bandit has been played
        '''
        old_estimate = self.q_na_estimate[bandit_index]
        step_size = 1.0 / (na + 1.0)
        error = (new_sample - old_estimate)
        return old_estimate + step_size * error


    def pick_best_action(self, array_of_values):
        '''
        pick a* among an array_of_values
        input - an array of values, (e.g. a = [1, 2, 7, 7, 4, 5])
        Examine which is the maximum average reward (e.g. 7)
        and get the first associated bandit index (e.g. 2)
        '''
        max_value = max(array_of_values)
        a_star = None
        for i, value in enumerate(array_of_values):
            if value == max_value:
                a_star = i - 0
                break
        return a_star


    def plot_bandit_rewards(self, y_list, color):
        '''
        method that plots the bandit rewards
        '''
        # generate x axis values
        x_list = []
        for i in range(0, len(y_list)):
            x_list.append(i)
        
        # store the maximum range in x
        if max(x_list) > self.max_x_range:
            self.max_x_range = max(x_list)
        
        plt.plot(x_list, y_list, color)
        plt.axis([-0.15, self.max_x_range + 0.15, -10., max(y_list) + 10.])


    def select_bandit(self, policy):
        '''
        select the bandit to play based upon a policy:
        greedy, e-greedy, etc.
        '''
        if policy == 'greedy':
            return self.pick_best_action(self.q_na_estimate)
        elif policy == 'e-greedy':
            # generate random uniformely distributed number between 0-1
            random_uniform = round(np.random.uniform(0.0, 1.0), 4)
            # ensure that the generated number if greater than 0
            assert random_uniform >= 0.0
            # if random number is less than "e" then select random action, best action otherwise
            if random_uniform < self.e:
                # random action (allow some exploration)
                #print 'e-greedy : exploring'
                return int(np.random.uniform(0, self.number_of_bandits))
            else:
                # best action (greedy)
                #print 'e-greedy : exploiting'
                return self.pick_best_action(self.q_na_estimate)
        elif policy == 'boltzman':
                # compute probability distribution
                prob_dist = []
                
                # compute sum of all q_a ' * eta
                denominator = 0.0
                for q_na in self.q_na_estimate:
                    denominator += np.exp(self.eta * q_na)
                
                for q_na in self.q_na_estimate:
                    numerator = np.exp(self.eta * q_na)
                    prob_dist.append(numerator / denominator)
                
                print 'boltzman probability distribution'
                print prob_dist
                print 'sum : %f, (must be 1)' %(sum(prob_dist))
                
                # generate an array of 1 - num of bandits
                bandit_index_array = [i for i in range(0, self.number_of_bandits)]
                # draw a weighted random choice
                return choice(bandit_index_array, size=1, replace=True, p=prob_dist)
                # e.g. print choice(['a','b','c','d'], size=10, replace=True, p=[0.97, 0.01, 0.01, 0.01])
        else:
            print 'ERROR: policy not known, admissible values are: greedy, e-greedy, boltzman'
            return None

    def start(self):
        '''
        solve homework 1 by combining all class functions
        '''

        # initialize the number of times played for each bandit to 0
        number_of_times_played = []
        for i in range(0, self.number_of_bandits):
            number_of_times_played.append(1)
        
        # for plotting purposes
        bandit_rewards = []
        
        # save initial estimates in bandit_rewards empty list
        for bandit_index in range(0, self.number_of_bandits):
            bandit_rewards.append([self.q_na_estimate[bandit_index]])

        for epoc in range(1, self.number_of_times_to_play):
            
            # greedy : get the index of the bandit with the maximum reward
            #selected_bandit = self.select_bandit('greedy')
            
            # e-greedy : allow for some exploration, controled by parameter "e"
            #selected_bandit = self.select_bandit('e-greedy')

            # boltzman : probability of selecting a depends on the 
            selected_bandit = self.select_bandit('boltzman')

            # play bandit and get a reward
            reward = self.compute_reward(selected_bandit)
            
            # update value
            updated_value = self.update_q_a_estimate(reward, number_of_times_played[selected_bandit], selected_bandit)
            
            # increase the number of times played of the winner bandit by one
            number_of_times_played[selected_bandit] = number_of_times_played[selected_bandit] + 1
            
            # update bandit estimate based on the obtained reward
            print '%d. Played bandit %d , gained reward of %f, updating value from %f to %f'% (epoc, selected_bandit, reward, self.q_na_estimate[selected_bandit], updated_value)
            self.q_na_estimate[selected_bandit] = updated_value
            
            # save bandit updated_value in memory for plotting purposes
            bandit_rewards[selected_bandit].append(updated_value)


        print 'Bandit rewards after %d iterations'% (self.number_of_times_to_play)
        print self.q_na_estimate
        
        print 'True (hidden) bandit average rewards : '
        print self.bandit_average_rewards
        
        print 'Best bandit as found by RL algorithm : %d' % (self.pick_best_action(self.q_na_estimate))
        print 'True (hidden) best bandit : %d' % (self.pick_best_action(self.bandit_average_rewards))
        
        # plot bandit 0 average rewards
        colors_array = ['b--', 'g--', 'r--', 'c--', 'm--', 'y--', 'k--', 'w--', 'b-', 'g-']
        for i in range(0, self.number_of_bandits):
            self.plot_bandit_rewards(bandit_rewards[i], colors_array[i])
        
        # setup labels and show plot
        plt.xlabel('steps')
        plt.ylabel('reward')
        plt.show()


if __name__ == '__main__':
    print 'Multi-arm bandit problem started...'
    print '-------'
    my_bandit_instance = MultiArmBandit()
    my_bandit_instance.start()
