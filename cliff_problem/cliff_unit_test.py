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


    def test_compute_reward1 (self):
        # test -1 rewards
        expected_reward = -1
        for state in range (0, 37):
            reward = self.cliff_problem_instance.compute_reward (state)
            self.assertEqual(reward, expected_reward)
        # test -100 rewards
        expected_reward = -100
        for state in range (37, 47):
            reward = self.cliff_problem_instance.compute_reward (state)
            self.assertEqual(reward, expected_reward)
        # test 100 rewards
        expected_reward = 100
        reward = self.cliff_problem_instance.compute_reward (47)
        self.assertEqual(reward, expected_reward)


    def test_compute_reward2 (self):
        '''
        test only critical reward cells
        '''
        reward = self.cliff_problem_instance.compute_reward (36)
        expected_reward = -1
        self.assertEqual(reward, expected_reward)
        #--
        reward = self.cliff_problem_instance.compute_reward (37)
        expected_reward = -100
        self.assertEqual(reward, expected_reward)
        #--
        reward = self.cliff_problem_instance.compute_reward (46)
        expected_reward = -100
        self.assertEqual(reward, expected_reward)
        #--
        reward = self.cliff_problem_instance.compute_reward (47)
        expected_reward = 100
        self.assertEqual(reward, expected_reward)
        

if __name__ == '__main__':
    unittest.main()
