import importlib

env_settings = {
    'A2C':dict(agent_class=importlib.import_module('algorithms.A2C'),
               id="-8",
               env_name='FloorPlan224',
               seed=2,
               record=True,
               data_collection_params = {'min_batch_size':500,
                                         'min_episodes':3, 
                                         'episode_adapt_rate':3},
               training_params = {'total_timesteps':1000000,  
                                  'adaptive_lr':True, 
                                  'desired_kl':1e-3},
               network_params = {'value_network':['fully_connected_network','medium'], 
                                 'policy_network':['fully_connected_network','medium']},
               algorithm_params = {'gamma':0.97, 
                                   'learning_rate':1e-3,
                                   'number_of_suggestions':0,
                                   'std_dev':['fixed', 0.3], 
                                   'target_update_rate':1.0},
               logs_path="/home/user/workspace/logs/"
               ),
    'A2S':dict(agent_class=importlib.import_module('algorithms.A2S'),
               id="-9",
               env_name='RoboschoolHumanoid-v1',
               seed=0,
               record=True,
               data_collection_params = {'min_batch_size':5000,
                                         'min_episodes':3, 
                                         'episode_adapt_rate':1},
               training_params = {'total_timesteps':1000000,  
                                  'adaptive_lr':True, 
                                  'desired_kl':1e-3},
               network_params = {'q_network':['fully_connected_network','xlarge'], 
                                 'value_network':['fully_connected_network','xlarge'], 
                                 'policy_network':['fully_connected_network','xlarge']},
               algorithm_params = {'gamma':0.99, 
                                   'learning_rate':1e-3,
                                   'number_of_suggestions':50, 
                                   'q_target_estimate_iteration':3,
                                   'std_dev':['fixed', 0.1], 
                                   'PER_size':100000, 
                                   'PER_batch_size':32, 
                                   'PER_iterations':30,
                                   'PER_alpha':0.6, 
                                   'PER_epsilon':0.01,
                                   'target_update_rate':1.0},
               logs_path="/home/user/workspace/logs/"
               )
}
