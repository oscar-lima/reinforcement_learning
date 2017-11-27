#!/usr/bin/env python

'''
Reinforcement Learning Homework
Prof: Francisco Melo
problem: multi-arm bandit
'''

import numpy as np
import math

class MultiArmBandit(object):
    '''
    Solution to homework 1 of RL
    '''
    def __init__(self):
        # homework (fixed) parameters
        number_of_bandits = 10 # the amount of bandit machines that we have
        self.bandits_mean_reward = 0.0 # in average the bandits will give you no reward (might loose, might win)
        self.bandits_variance = 1.0 # bandit average reward is allowed to deviate this much w.r.t. self.bandits_mean_reward
        self.reward_variance = 1.0 # bandit reward is allowed to deviate this much w.r.t. the bandit mean (self.bandit_average_rewards[bandit_number])

        # compute n random rewards for all bandits (n=number_of_bandits)
        self.bandit_average_rewards = self.compute_multiple_bandit_average_reward(number_of_bandits)
        print 'Bandits will provide in average this rewards:'
        print self.bandit_average_rewards


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


    def start(self):
        print 'reward : ' + str(self.compute_reward(4))


if __name__ == '__main__':
    print 'Multi-arm bandit problem started...'
    print '-------'
    my_bandit_instance = MultiArmBandit()
    my_bandit_instance.start()
