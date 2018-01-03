#!/usr/bin/env python

import cliff_problem
import numpy as np
import random

class QLearning (object):
    '''
    Class to solve Reinforcement Learning homework programming assignment 3
    The cliff problem, q-learning and Sarsa
    '''
    def __init__ (self):
        self.goal_state = 47
        maximum_amount_of_states = 47
        self.initial_state = 36 # robot starts from cell 36
        # create object of cliff problem class
        self.cliff_world = cliff_problem.CliffProblem ()
        # init q vector to zeros
        self.q = []
        for i in range (0, maximum_amount_of_states + 1):
            self.q.append ([0.0, 0.0, 0.0, 0.0])
        # set gamma parameter discount
        self.gamma = 1.0
        # to keep track of the robot state
        self.robot_state = self.initial_state
        # possible robot actions
        self.possible_actions = ['up', 'down', 'right', 'left']
        # learning rate or step size
        self.learning_rate = 0.5
        # epsilon greedy parameter, exploration vs exploitation
        self.e = 0.0001


    def format_q_number (self, number):
        '''
        limit number to a certain range, convert to in then convert to string
        '''
        max_spaces = 4
        if number > 100:
            number = 99.0
        elif number < -100:
            number = -99.0
        
        return str(int(number)).ljust(max_spaces)
        

    def print_q_line (self, start, end):
        '''
        print 1 line of q
        '''
        print '------------------------------------------------------------------------------------------------------------------------'
        line1 = ''
        line2 = ''
        line3 = ''
        space = '  '
        
        max_spaces = 4 # the amount of spaces that the largest number has
        for i in range(start, end):
            line1 = line1 + '   ' + self.format_q_number(self.q[i][0]) + space + '|'
            if i == self.robot_state:
                robot = 'R'
            else:
                robot = ' '
            line2 = line2 + self.format_q_number(self.q[i][3]) + robot + self.format_q_number(self.q[i][2]) + '|'
            line3 = line3 + '   ' + self.format_q_number(self.q[i][1]) + space + '|'
            
        print line1
        print line2
        print line3


    def print_q (self):
        '''
        print q matrix in a pretty way
        '''
        self.print_q_line (0, 12)
        self.print_q_line (12, 24)
        self.print_q_line (24, 36)
        self.print_q_line (36, 48)
        print '------------------------------------------------------------------------------------------------------------------------'


    def action_to_index (self, action):
        '''
        convert action word into number (index)
        '''
        return self.possible_actions.index(action)
        

    def update_q (self, robot_state, action, reward):
        # rule to update q
        # Q(s,a) <- Q(s,a) + alpha * [R(state, action) + Gamma * Max[Q(next state, all actions)]
        self.q [robot_state][self.action_to_index (action)] += self.learning_rate * (reward + self.gamma * self.compute_max_future_q_value (self.robot_state, self.q))
        

    def compute_max_future_q_value (self, future_robot_state, q_matrix):
        '''
        get the maximum future reward (one step ahead)
        '''
        print future_robot_state
        possible_q_values = []
        for q in q_matrix [future_robot_state]:
            possible_q_values.append (q)
        return max(possible_q_values)


    def follow_policy (self, robot_state, q_matrix):
        '''
        query q matrix to selext next best action, if it does not have
        a best action then select random
        '''
        q_values = q_matrix[robot_state]
        # get index of max q values
        m = max (q_values)
        max_values_index = [i for i, j in enumerate(q_values) if j == m]
        # print for debug purposes
        if len(max_values_index) > 1:
            print 'random selection'
        else:
            print 'it exists a q dominant value, action choice will not be random'
        # select a random value from the list
        random_index = random.choice(max_values_index)
        # return action that has the max q value
        return self.possible_actions[random_index]


    def run_one_episode (self):
        '''
        Follow policy until agent reaches goal updating q matrix on the way
        '''
        print '=========== episode 1 ==========='
        print 'pretty q print:'
        self.print_q ()
        print '********************************'
        # put the robot in the start position
        self.robot_state = self.initial_state
        while self.robot_state != self.goal_state:
            # follow policy with epsilon greeedy = 0.15
            # generate a random number between 0 and 1 rounded up to 4 decimals
            random_uniform = round(np.random.uniform(0.0, 1.0), 4)
            if random_uniform < self.e:
                print 'e-greedy: exploration'
                action = random.choice(self.possible_actions)
            else:
                # best action (greedy), exploiting
                action = self.follow_policy (self.robot_state, self.q)
            #action = self.follow_policy (self.robot_state, self.q)
            print 'action:',
            print action
            current_robot_state = self.robot_state
            # move the robot to the best q value (or random if they are all same)
            self.robot_state, reward = self.cliff_world.execute_action(self.robot_state, action)
            print 'robot state:',
            print self.robot_state
            # get maximum q (of next step)
            max_q_next_step = self.compute_max_future_q_value (self.robot_state, self.q)
            print 'max_q_next_step:',
            print max_q_next_step
            # update q
            self.update_q (current_robot_state, action, reward)
            print '********************************'
        print 'pretty q print:'
        self.print_q ()


    def q_learning_algorithm (self):
        '''
        run 500 episodes
        '''
        for i in range (0, 500):
            self.run_one_episode ()


if __name__ == '__main__':
    cliff_problem_instance = QLearning ()
    cliff_problem_instance.q_learning_algorithm ()
