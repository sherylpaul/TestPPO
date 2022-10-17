# TestPPO
Testing single and multi agent ppo



grid_world.py and agent_learning.py correspond to multi agent ppo

grid_world_test.py and agent_learning_test.py correspond to single agent ppo

(They are the same otherwise)

in both(grid_world.py and grid_world_test.py), you can change the 'map_name' to '50x50_map' or '100x100_map' - pkl files are available
self.n_agents in grid_world_test.py = number of agents
You need to change the path of the pkl file when you download and run it on your machine

Issue I'm running into:
1.) 50x50 and 100x100 work fine for single agent
2.) 50x50 works fine for 2 agents with 100k training timesteps, with 3 agents- it's okayish.
3.) 100x100 does not work well at all with 2 agents or more- I've tried running it with 500k and 1M timesteps and it still doesn't do well at all.

