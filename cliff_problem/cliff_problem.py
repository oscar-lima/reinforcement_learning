#!/usr/bin/env python

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


    def robot_is_in_cliff (self, state):
        '''
        return true if robot is in the cliff
        '''
        if state > 36 and state < self.goal_state:
            return True
        else:
            return False
        

    def execute_action (self, state, action, world_width=12):
        '''
        Execute an action: up, down, left, right.
        Change the agent state and get a reward
        '''
        # ensure state is different than the cliff
        assert not self.robot_is_in_cliff(state)

        # most states provide with this reward so it makes sense to set it now and only modify if needed
        reward = -1

        if action == 'up':
            if state < world_width:
                print 'agent cant go up because it is at the higher level already, doing nothing'
            else:
                state = state - world_width
        elif action == 'down':
            if state < self.goal_state - world_width + 1:
                state = state + world_width
        elif action == 'left':
            # handle particular cases
            if state % world_width == 0:
                print 'robot is at a extreme left cell, executing left will lead to the same position'
            else:
                state = state - 1
        elif action == 'right':
            # handle particular cases
            if state == 11 or state == 23 or state == 35 or state == 47:
                print 'robot is at extreme right cell, executing right will lead to the same position'
            else:
                state = state + 1
        else:
            print 'Action is not known, admissible values are: up, down, left, right'
            return None
        
        # if robot is in cliff then send it to intial state (36)
        if self.robot_is_in_cliff (state):
            reward = -100
            state = self.initial_state # 36
        
        # ensure state to be between range 0 - goal state
        assert state < self.goal_state + 1
        assert state >= 0
        
        # if goal is reached after executing action then reward with 100
        if state == self.goal_state:
            reward = 100
        
        return [state, reward]


    def compute_reward (self, state):
        '''
        cliff      = -100
        every step = -1
        goal       = 100
        '''
        if state == self.goal_state:
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
