# What is this project?
This is a program for recognizing hand gestures, and you are able to save coordinates of hand joints for extracting data if you like (by pressing 'f'). You can quit using 'q'.

# What is it going to turn into
Since this is a solo project for me and a kind of show-off of my knowledge, I'm going to have to have my approach to solving which I will explain.

# The First Approach
My first idea is to use MediaPipe to recognize the hand with coordinate data so I can extract coordinates and train the model around that data to recognize hand gestures.
For that, I first made the vision part using OpenCV and MediaPipe (Google library and framework). After I was done with that, I went and implemented my own way of saving coordinates to a JSON file (for convenience and ease of use in case of using an API).
I couldn't just put the coordinates into the model raw, so I had to normalize and transform it. For that, I also did some pattern checking, and with some insights, I also implemented that.
So the only thing that is left is to make the model for it.

# What about the model?
I do know how to work with TensorFlow and Keras (thanks to Kaggle), but I'm still thinking about how I should get an output from a model.

Any help for saving coordinate data for different gestures is appreciated.
