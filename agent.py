from config import *
import time
import random
"""

DO not modify the structure of "class Agent".
Implement the functions of this class.
Look at the file run.py to understand how evaluations are done. 

There are two phases of evaluation:
- Training Phase
The methods "registered_reset_train" and "compute_action_train" are invoked here. 
Complete these functions to train your agent and save the state.

- Test Phase
The methods "registered_reset_test" and "compute_action_test" are invoked here. 
The final scoring is based on your agent's performance in this phase. 
Use the state saved in train phase here. 

"""


class Agent:
    def __init__(self, env, discount_rate=0.97, learning_rate=0.7):
        self.env_name = env
        self.config = config[self.env_name]

        if (self.env_name =='taxi'):

            self.state_size = self.config[0]
            print("State size:", self.state_size)
            self.action_size = self.config[1]
            self.eps = 1.0
            self.discount_rate = discount_rate
            self.learning_rate = learning_rate
            self.q_table = 1e-4 * np.random.random([self.state_size, self.config[1]])
            self.p_state = 0
            self.p_action = 0

        pass








    def register_reset_train(self, obs):
        if(self.env_name=='taxi'):

            q_action = random.choice(np.arange(self.action_size))
            self.state = obs
            self.p_action = q_action

        return self.p_action




    def compute_action_train(self, obs, reward, done, info):
        next_state = obs
        #print('prev =', self.p_state, 'next state=', next_state)
        q_next = self.q_table[next_state]
        q_next = np.zeros([self.action_size]) if done else q_next
        q_target = reward + self.discount_rate * np.max(q_next)

        q_update = q_target - self.q_table[self.p_state, self.p_action]
        self.q_table[self.p_state, self.p_action] += self.learning_rate * q_update

        if done:
            self.eps = self.eps * 0.99

        self.p_state = obs

        action_greedy = np.argmax(next_state)
        action_random = random.choice(np.arange(self.action_size))
        next_action = action_random if random.random() < self.eps else action_greedy

        #print('prev Act =', self.p_action, 'next act=', next_action)
        self.p_action = next_action
        if done:
          self.eps = self.eps * 0.99999

        return  next_action



    def register_reset_test(self, obs):
        """
        Use this function in the test phase
        This function is called at the beginning of an episode. 
        PARAMETERS  : 
            - obs - raw 'observation' from environment
        RETURNS     : 
            - action - discretized 'action' from raw 'observation'
        """
        q_state = self.q_table[obs]
        action_greedy = np.argmax(q_state)


        return action_greedy

    def compute_action_test(self, obs, reward, done, info):
        """
        Use this function in the test phase
        This function is called at all subsequent steps of an episode until done=True
        PARAMETERS  : 
            - observation - raw 'observation' from environment
            - reward - 'reward' obtained from previous action
            - done - True/False indicating the end of an episode
            - info -  'info' obtained from environment

        RETURNS     : 
            - action - discretized 'action' from raw 'observation'
        """
        q_state = self.q_table[obs]
        action = np.argmax(q_state)


        return action













