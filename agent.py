from config import *
import time
import random
import numpy as np
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
    def __init__(self, env):
        self.env_name = env
        self.config = config[self.env_name]

        if (self.env_name =='taxi'):

            self.state_size = self.config[0]
            print("State size:", self.state_size)
            self.action_size = self.config[1]
            self.eps = 1

            self.discount_rate = 0.97
            self.learning_rate = 0.62
            self.q_table =  1e-4*np.zeros([self.state_size, self.action_size])
            self.p_state = 0
            self.p_action = 0

        if (self.env_name =='kbca' or self.env_name =='kbcb' or self.env_name =='kbcc'):

            self.state_size = self.config[0]
            print("State size:", self.state_size)
            self.action_size = self.config[1]
            self.eps = 1

            self.discount_rate = 1
            self.learning_rate = 0.8 if self.env_name=='kbca' else 0.8 if self.env_name=='kbcb' else 0.8
            self.get_qTableKBC()
            self.state_list =[]
            self.lam = 0.9

            self.p_state = 0
            self.p_action = 0
            self.track =0
            self.stage = 0






    def get_qTableKBC(self):
        self.q_table = np.zeros([self.state_size,self.action_size])
        self.q_table[0][0] = 0
        for i in range(0, 16):
            self.q_table[i+1][0] = 1000 * (2 ** i)










    def register_reset_train(self, obs):
        if(self.env_name=='taxi'):

            action_random = random.choice(np.arange(self.action_size))

            q_action = action_random
            self.p_state = obs
            self.p_action = q_action

            return self.p_action

        if (self.env_name == 'kbca'):

            state = obs.count(1)
            print(state)

            action_greedy = np.argmax(self.q_table[state])
            action_random = random.choice(np.arange(self.action_size))

            q_action = action_random if random.random() < self.eps else action_greedy
            self.p_state = state
            self.p_action = 1

            return self.p_action

        if (self.env_name == 'kbcb'):

            state = obs.count(1)
            print(state)

            action_greedy = np.argmax(self.q_table[state])
            action_random = random.choice(np.arange(self.action_size))

            q_action = action_random if random.random() < self.eps else action_greedy
            self.p_state = state
            self.p_action = 1

            return self.p_action

        if (self.env_name == 'kbcc'):

            state = obs.count(1)
            print(state)

            action_greedy = np.argmax(self.q_table[state])
            action_random = random.choice([1,2])

            q_action = action_random if random.random() < self.eps else action_greedy
            self.p_state = state
            self.p_action = q_action

            return self.p_action




    def compute_action_train(self, obs, reward, done, info):
        if(self.env_name=='taxi'):
            next_state = obs
            print('reward',reward)
            print('prev =', self.p_state, 'next state=', next_state)
            q_next = self.q_table[next_state]
            q_next = np.zeros([self.action_size]) if done else q_next
            q_target = reward + self.discount_rate * np.max(q_next)

            q_update = q_target - self.q_table[self.p_state, self.p_action]
            self.q_table[self.p_state, self.p_action] += self.learning_rate * q_update



            self.p_state = next_state

            action_greedy = np.argmax(q_next)
            action_random = random.choice(np.arange(self.action_size))
            next_action = action_random if random.random() < self.eps else action_greedy

            print('prev Act =', self.p_action, 'next act=', next_action)
            self.p_action = next_action
            if done:
              self.eps = self.eps * 0.85



            return  next_action


        if (self.env_name == 'kbca' or self.env_name =='kbcb'):

            next_state = obs.count(1)
            print('prev =', self.p_state, 'next state=', next_state)

            q_next = self.q_table[next_state]
            q_next = np.zeros([self.action_size]) if done else q_next
            q_target = reward + self.discount_rate * np.max(q_next)

            q_update = q_target - self.q_table[self.p_state, self.p_action]
            self.q_table[self.p_state, self.p_action] += self.learning_rate * q_update

            self.p_state = next_state

            action_greedy = np.argmax(q_next)
            action_random = random.choice(np.arange(self.action_size))
            #next_action = action_random if random.random() < self.eps else action_greedy
            next_action = 1

            print('prev Act =', self.p_action, 'next act=', next_action)
            print('reward', reward)
            self.p_action = next_action
            if done:
                self.eps = self.eps * 1

            return 1


        if (self.env_name == 'kbcc'):

            next_state = obs.count(1)
            print('prev =', self.p_state, 'next state=', next_state,'reward=',reward)

            q_next = self.q_table[next_state]
            q_next = np.zeros([self.action_size]) if done else q_next
            q_target = reward + self.discount_rate * np.max(q_next)

            q_update = q_target - self.q_table[self.p_state, self.p_action]
            self.q_table[self.p_state, self.p_action] += self.learning_rate * q_update

            self.p_state = next_state

            action_greedy = np.argmax(q_next[1:3])
            action_random = random.choice([1,2])
            next_action = action_random if random.random() < self.eps else action_greedy


            print('prev Act =', self.p_action, 'next act=', next_action)
            print('reward', reward)
            self.p_action = next_action
            if done:
                self.eps = self.eps * .9999

            return next_action





    def register_reset_test(self, obs):
        """
        Use this function in the test phase
        This function is called at the beginning of an episode. 
        PARAMETERS  : 
            - obs - raw 'observation' from environment
        RETURNS     : 
            - action - discretized 'action' from raw 'observation'
        """
        if (self.env_name == 'taxi'):

            q_state = self.q_table[obs]
            action_greedy = np.argmax(q_state)

        if (self.env_name == 'kbca' or self.env_name == 'kbcb' or  self.env_name == 'kbcc' ):
            state = obs.count(1)
            q_state = self.q_table[state]
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
        if (self.env_name == 'taxi'):
            q_state = self.q_table[obs]
            action = np.argmax(q_state)
            #comitted

        if (self.env_name == 'kbca' or self.env_name == 'kbcb' or self.env_name == 'kbcc' ):
            state = obs.count(1)
            q_state = self.q_table[state]
            action= np.argmax(q_state)
            print("state:{},action:{}".format(q_state,action))
            if(done):
                print(self.q_table)

        return action













