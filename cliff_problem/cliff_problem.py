#!/usr/bin/env python

class CliffProblem (object):
    '''
    Class to solve Reinforcement Learning homework programming assignment 3
    The cliff problem, q-learning and Sarsa
    '''
    def __init__ (self):
        self.world_state = self.create_initial_world_state ()
        self.robot_state = 36 # robot starts from cell 36


    def create_initial_world_state (self):
        '''
        Create initial world state
        48 element matrix 4 x 12
        '''
        world_state = []
        for i in range (0, 36):
            world_state.append ('E') # E - Empty

        world_state.append ('R') # S - Start

        for i in range (len(world_state), 47):
            world_state.append ('C') # C - cliff

        world_state.append ('G') # G - Goal
        
        return world_state


    def print_world_state (self, robot_state):
        '''
        to print in console the state of the world
        '''
        for i, cell in enumerate(self.world_state):
            if i % 12 == 0 and i != 0:
                print ('\n')
                print (cell),
            else:
                print (cell),


    def compute_reward (self, state):
        '''
        cliff      = -100
        every step = -1
        goal       = 100
        '''
        if state == 47:
            return 100
        elif state < 37:
            return -1
        else:
            return -100


    def start_cliff_problem (self):
        '''
        Solve the cliff problem
        '''
        # print the initial world state
        self.print_world_state (self.robot_state)


if __name__ == '__main__':
    cliff_problem_instance = CliffProblem ()
    cliff_problem_instance.start_cliff_problem()
