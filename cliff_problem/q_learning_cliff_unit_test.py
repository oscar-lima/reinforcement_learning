#!/usr/bin/env python
import unittest
import q_learning_cliff

class TestQLearningCliff(unittest.TestCase):
    '''
    Class to test the cliff problem
    '''
    def setUp(self):
        '''
        Function that gets executed only once
        '''
        self.q_learning_problem_instance = q_learning_cliff.QLearning ()


    def test_follow_policy (self):
        '''
        test if the robot is following the policy properly
        q matrix template
        q_matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\ # 0-5
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\ # 6-11
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\ # 12-17
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\ # 18-23
                    [0,0,0,0],[0,0,0,0],[4,1,5,2],[0,0,0,0],[0,0,0,0],[0,0,0,0],\ # 24-29
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\ # 30-35
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\ # 36-41
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] # 42-47
        '''
        expected_value = 'right'
        robot_state = 26
        # up, down, right, left
        q_matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[4,1,5,2],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        output_value = self.q_learning_problem_instance.follow_policy (robot_state, q_matrix)
        self.assertEqual(expected_value, output_value)
        #---
        expected_value = 'up'
        robot_state = 26
        # up, down, right, left
        q_matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[6,1,5,2],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        output_value = self.q_learning_problem_instance.follow_policy (robot_state, q_matrix)
        self.assertEqual(expected_value, output_value)
        #---
        expected_value = 'left'
        robot_state = 26
        # up, down, right, left
        q_matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[4,1,5,7],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        output_value = self.q_learning_problem_instance.follow_policy (robot_state, q_matrix)
        self.assertEqual(expected_value, output_value)
        ##---
        expected_value = 'down'
        robot_state = 26
        # up, down, right, left
        q_matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[4,8,5,2],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        output_value = self.q_learning_problem_instance.follow_policy (robot_state, q_matrix)
        self.assertEqual(expected_value, output_value)

    def test_compute_max_future_q_value (self):
        '''
        test if max future reward function is working properly
        '''
        robot_state = 26
        # up, down, right, left
        q_matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[4,8,5,2],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],\
                    [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        expected_value = 8
        output_value = self.q_learning_problem_instance.compute_max_future_q_value (robot_state, q_matrix)
        self.assertEqual(expected_value, output_value)


if __name__ == '__main__':
    unittest.main()