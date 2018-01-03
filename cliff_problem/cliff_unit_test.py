#!/usr/bin/env python
import unittest
import cliff_problem

class TestStringMethods(unittest.TestCase):
    '''
    Class to test the cliff problem
    '''
    def setUp(self):
        '''
        Function that gets executed only once
        '''
        self.cliff_problem_instance = cliff_problem.CliffProblem ()
    
    def test_robot_is_in_cliff1 (self):
        '''
        is robot on the cliff?, test the critical points
        '''
        expected_value = False
        output_value = self.cliff_problem_instance.robot_is_in_cliff (36)
        self.assertEqual(expected_value, output_value)
        #--
        expected_value = True
        output_value = self.cliff_problem_instance.robot_is_in_cliff (37)
        self.assertEqual(expected_value, output_value)
        #--
        expected_value = True
        output_value = self.cliff_problem_instance.robot_is_in_cliff (41)
        self.assertEqual(expected_value, output_value)
        #--
        expected_value = True
        output_value = self.cliff_problem_instance.robot_is_in_cliff (46)
        self.assertEqual(expected_value, output_value)
        #--
        expected_value = False
        output_value = self.cliff_problem_instance.robot_is_in_cliff (47)
        self.assertEqual(expected_value, output_value)
        #--
        expected_value = False
        output_value = self.cliff_problem_instance.robot_is_in_cliff (0)
        self.assertEqual(expected_value, output_value)
    
    def test_execute_action_left_2 (self):
        expected_value = 3
        output_value = self.cliff_problem_instance.execute_action (4, 'left')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        #--
        expected_value = 0
        output_value = self.cliff_problem_instance.execute_action (0, 'left')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        #--
        expected_value = 12
        output_value = self.cliff_problem_instance.execute_action (12, 'left')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        #--
        expected_value = 24
        output_value = self.cliff_problem_instance.execute_action (24, 'left')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        #--
        expected_value = 36
        output_value = self.cliff_problem_instance.execute_action (36, 'left')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        #--
        expected_value = 28
        output_value = self.cliff_problem_instance.execute_action (29, 'left')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        #--
        expected_value = 36
        output_value = self.cliff_problem_instance.execute_action (47, 'left')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-100, output_value[1]) # reward test
        #--
        expected_value = 22
        output_value = self.cliff_problem_instance.execute_action (23, 'left')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        #--
        expected_value = 5
        output_value = self.cliff_problem_instance.execute_action (6, 'left')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
    
    def test_execute_action_right_3 (self):
        expected_value = 11
        output_value = self.cliff_problem_instance.execute_action (11, 'right')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        #--
        expected_value = 23
        output_value = self.cliff_problem_instance.execute_action (23, 'right')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        #--
        expected_value = 35
        output_value = self.cliff_problem_instance.execute_action (35, 'right')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        #--
        expected_value = 47
        output_value = self.cliff_problem_instance.execute_action (47, 'right')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(100, output_value[1]) # reward test
        #--
        expected_value = 29
        output_value = self.cliff_problem_instance.execute_action (28, 'right')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        #--
        expected_value = 15
        output_value = self.cliff_problem_instance.execute_action (14, 'right')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        #--
        expected_value = 1
        output_value = self.cliff_problem_instance.execute_action (0, 'right')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        #--
        expected_value = 23
        output_value = self.cliff_problem_instance.execute_action (22, 'right')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        #--
        expected_value = 36
        output_value = self.cliff_problem_instance.execute_action (36, 'right')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-100, output_value[1]) # reward test
        
    def test_execute_action_down_4 (self):
        expected_value = 12
        output_value = self.cliff_problem_instance.execute_action (0, 'down')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        #--
        expected_value = 36
        output_value = self.cliff_problem_instance.execute_action (25, 'down')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-100, output_value[1]) # reward test
        #--
        expected_value = 36
        output_value = self.cliff_problem_instance.execute_action (28, 'down')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-100, output_value[1]) # reward test
        #--
        expected_value = 36
        output_value = self.cliff_problem_instance.execute_action (31, 'down')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-100, output_value[1]) # reward test
        #--
        expected_value = 47
        output_value = self.cliff_problem_instance.execute_action (35, 'down')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(100, output_value[1]) # reward test
        #--
        expected_value = 23
        output_value = self.cliff_problem_instance.execute_action (11, 'down')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        #--
        expected_value = 27
        output_value = self.cliff_problem_instance.execute_action (15, 'down')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        #--
        expected_value = 47
        output_value = self.cliff_problem_instance.execute_action (47, 'down')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(100, output_value[1]) # reward test
        #--
        expected_value = 36
        output_value = self.cliff_problem_instance.execute_action (36, 'down')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        
    def test_execute_action_up_5 (self):
        expected_value = 0
        output_value = self.cliff_problem_instance.execute_action (0, 'up')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        #--
        expected_value = 5
        output_value = self.cliff_problem_instance.execute_action (5, 'up')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        #--
        expected_value = 10
        output_value = self.cliff_problem_instance.execute_action (10, 'up')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        #--
        expected_value = 11
        output_value = self.cliff_problem_instance.execute_action (11, 'up')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        #--
        expected_value = 24
        output_value = self.cliff_problem_instance.execute_action (36, 'up')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        #--
        expected_value = 18
        output_value = self.cliff_problem_instance.execute_action (30, 'up')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        #--
        expected_value = 2
        output_value = self.cliff_problem_instance.execute_action (14, 'up')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        #--
        expected_value = 21
        output_value = self.cliff_problem_instance.execute_action (33, 'up')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test
        #--
        expected_value = 35
        output_value = self.cliff_problem_instance.execute_action (47, 'up')
        self.assertEqual(expected_value, output_value[0])
        self.assertEqual(-1, output_value[1]) # reward test

if __name__ == '__main__':
    unittest.main()
