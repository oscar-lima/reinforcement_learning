#!/usr/bin/env python

import sys,tty,termios # for moving the agent with the keyboard
from random import randint # to genarate random int numbers

class CliffProblem (object):
    '''
    Class to solve Reinforcement Learning homework programming assignment 3
    The cliff problem, q-learning and Sarsa
    '''
    def __init__ (self):
        self.goal_state = 47
        self.initial_state = 36 # robot starts from cell 36
        # ---
        self.robot_state = self.initial_state
        self.world_state = self.create_initial_world_state ()


    def create_initial_world_state (self):
        '''
        Create initial world state
        48 element matrix 4 x 12
        '''
        world_state = []
        for i in range (0, 37):
            world_state.append ('E') # E - Empty

        for i in range (len(world_state), self.goal_state):
            world_state.append ('C') # C - cliff

        world_state.append ('G') # G - Goal
        
        return world_state


    def print_world_state (self, robot_state):
        '''
        to print in console the state of the world
        '''
        for i, cell in enumerate(self.world_state):
            if i % 12 == 0 and i != 0:
                if robot_state == i:
                    print '\n'
                    print 'R',
                else:
                    print '\n'
                    print (cell),
            else:
                if robot_state == i:
                    print 'R',
                else:
                    print (cell),
        print '\n------------------------'


    def robot_is_in_cliff (self, state, output=True):
        '''
        return true if robot is in the cliff
        '''
        if state > 36 and state < self.goal_state:
            if output:
                print 'Oh boy! you have fallen into the cliff !'
            return True
        else:
            return False


    def select_random_action (self, possible_actions):
        '''
        select a random action among a given list
        '''
        return possible_actions[randint(0, len(possible_actions))]


    def execute_action (self, state, action, world_width=12, output=True):
        '''
        Execute an action: up, down, left, right.
        Change the agent state and get a reward
        '''
        # ensure state is different than the cliff
        assert not self.robot_is_in_cliff(state, output)

        # most states provide with this reward so it makes sense to set it now and only modify if needed
        reward = -1

        if action == 'up':
            if state < world_width:
                if output:
                    print 'agent cant go up because it is at the higher level already, doing nothing'
            else:
                state = state - world_width
        elif action == 'down':
            if state < self.goal_state - world_width + 1:
                state = state + world_width
        elif action == 'left':
            # handle particular cases
            if state % world_width == 0:
                if output:
                    print 'robot is at a extreme left cell, executing left will lead to the same position'
            else:
                state = state - 1
        elif action == 'right':
            # handle particular cases
            if state == 11 or state == 23 or state == 35 or state == 47:
                if output:
                    print 'robot is at extreme right cell, executing right will lead to the same position'
            else:
                state = state + 1
        else:
            if output:
                print 'Action is not known, admissible values are: up, down, left, right'
            return None
        
        if output:
            # if robot is in cliff then send it to initial state (36)
            if self.robot_is_in_cliff (state, output):
                reward = -100
                state = self.initial_state # 36
        
        # ensure state to be between range 0 - goal state
        assert state < self.goal_state + 1
        assert state >= 0
        
        # if goal is reached after executing action then reward with 100
        if state == self.goal_state:
            reward = 100
        
        return [state, reward]


    def get_char (self):
        '''
        taken from: https://stackoverflow.com/questions/22397289/finding-the-values-of-the-arrow-keys-in-python-why-are-they-triples
        input a char from the keyboard
        '''
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


    def read_arrow_from_keyboard (self):
        '''
        Use function get_char () to read a key and compare it to match a known arrow
        '''
        arrow = None
        key = self.get_char ()

        if key == '\x1b[A':
            arrow = 'up'
        elif key == '\x1b[B':
            arrow = 'down'
        elif key == '\x1b[C':
            arrow = 'right'
        elif key == '\x1b[D':
            arrow = 'left'
        else:
            print 'not an arrow key!'

        assert arrow != None

        return arrow


    def move_robot_with_keyword (self):
        '''
        Read arrows from keyboard to move the robot around the cliff world manually
        for testing purposes
        '''
        print 'Move the robot around the environment 20 times with the keyboard'
        # move the agent around the environment with the keyboard
        for i in range(0, 20):
            # get action from keyword (only arrows are allowed
            action = self.read_arrow_from_keyboard ()
            # execute action
            self.robot_state, reward = self.execute_action(self.robot_state, action)
            print 'Because of the previous action, you got a reward of : %d\n'%(reward)
            # print the world
            self.print_world_state(self.robot_state)


    def print_corner_state (self, qup, qdown, qleft, qright, robot=False):
        '''
        print upper left corner state
        input boolean robot: whether robot is in this state or not
        '''
        print '--------------------------------'
        print '|   ' + str(qup) + '   |'
        if robot:
            print '|' + str(qleft) + ' R ' + str(qright) + '|'
        else:
            print '|' + str(qleft) + '   ' + str(qright) + '|'
        print '|   ' + str(qdown) + '   |'
        print '--------------------------------'


    def print_state_with_q_values (self):
        '''
        prints q matrix in a nice way:
        -----------------
        |       5.6       |
        |4.5          7.8 | = S
        |       4.3       |
        -----------------
        Being 5.6 the reward being on state S and choosing up action
        '''
        pass
        


    def teleop_demo (self):
        '''
        Test the functions in this file with an interactive demo
        '''
        # print the initial world state
        self.print_world_state (self.robot_state)
        
        # demo robot keyboard teleoperation
        self.move_robot_with_keyword ()
        
        # print q
        #self.print_corner_state (5.6, 4.3, 4.5, 7.8, robot=False)


if __name__ == '__main__':
    cliff_problem_instance = CliffProblem ()
    cliff_problem_instance.teleop_demo ()
