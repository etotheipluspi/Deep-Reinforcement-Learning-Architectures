## Code

Let's start running experiments.

## Cart-Pole Architectures

Set up a directory to store all the data for this experiment by making a directory structure that looks like this:
`data/cartpole/initial_exepriment/architecture_name/`. Where `architecture_name` is what you decide to call a given
neural netowrk architecture. 

Now, let's move the GymWrapper to its own file, call it `gym_wrapper.py` or something similar. Anytime you want to use
the wrapper just move that file to the directory you are working in. Put `import gym_wrapper` at the top of the file you
are running experiments from, and you should be good to go.

Set up and run some experiments with the cart pole probelm. Start with a two layer architecture, and try different
neuron combinations: `1-1`, `5-5`, `10-10`, `15-15`, `20-20`. 
