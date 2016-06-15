# Deep-Reinforcement-Learning-Architectures
Repo containing to-dos and instructions for DRL architectures project. 


# Getting Started

If you are new to reinforcement learning, and decision making under uncertatiny in general, let's first get you up to speed on the fundamentals. 

## Reinforcement Learning

Watch parts 1, 2, 9, and 10 from the Udacity course below:

https://www.udacity.com/course/intro-to-artificial-intelligence--cs271

The course covers many topics, but the ones we care about are the funcdamentals of AI, probability, MDPs, and Reinforcement Learning.

## Deep Learning

Let's get started by watching some videos that explain deep learning at a high level (for best results watch them in order):

[TedX talk](https://www.ted.com/talks/fei_fei_li_how_we_re_teaching_computers_to_understand_pictures?language=en) by Fei-Fei Li on describing images with neural networks. 

[Video Explanations](https://www.youtube.com/channel/UC9OeZkIwhzfv-_Cb7fCikLQ/videos) of Deep Learning. Watch episodes 2-20.

[Talk](https://www.youtube.com/watch?v=l2dVjADTEDU&feature=youtu.be) by Geoff Hinton on how neural networks really work. 

[Tutorial](http://karpathy.github.io/neuralnets/) on neural networks by Andrej Karpathy. 

https://www.udacity.com/course/intro-to-artificial-intelligence--cs271

## Deep Reinforcement Learning

Read Andrej Karpathy's [blog](http://karpathy.github.io/2016/05/31/rl/) on Policy Gradient method.


Watch the John Schulman lecture (advanced):
https://www.youtube.com/watch?v=aUrX-rP_ss4


# Setup

## Chainer

Install [chainer](https://github.com/pfnet/chainer) by running: 

```
pip install chainer 
```

Try the chainer [tutorial](http://docs.chainer.org/en/stable/tutorial/basic.html)


## Tensor Flow

Installation on a Mac:

See instructions [here](https://www.tensorflow.org/versions/r0.9/get_started/os_setup.html#anaconda-installation). In my expereince, using conda environments is the easiest way to go.

* Install [anacodna](https://www.continuum.io/downloads)
* Run: `conda create -n tensorflow python=2.7`
* Run: `source activate tensorflow`
* Run: `export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/tensorflow-0.9.0rc0-py2-none-any.whl`
* Run: `sudo pip install --upgrade $TF_BINARY_URL`
* Run: `conda install ipython`

To deactivate the environemnt, run: `source deactivate`, to activate it again run: `source activate tensorflow`.

Once tensorflow is installed, follow the MNIST tutorials [here](https://www.tensorflow.org/versions/r0.9/tutorials/mnist/beginners/index.html)


## Chimp

Check out the repo [here](https://github.com/sisl/Chimp/graphs/traffic)

Go through the examples, and try trianing a cart-pole model.

# Things to Try

After you're comfortable with the Chimp interface, try running a few experiments:

* 2-Layer neural netowrk controllers for cart-pole problem. Vary the number of neurons in each layer, and compare the convergance rates, and quality of solution
* MLP comparison. Try making the networks deeper while keeping their width the same and compare results.
* Try adding batch normalizaiton for a few of the above architectures and compare the results.
