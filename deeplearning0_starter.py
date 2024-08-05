
'''

jetson_inference library is used for Image Classification tasks, specifically for Jetson
platforms.


Use ssd-mobilenet-v2 (Single Shot MultiBox Detector with MobileNet) network model, this model
is used for OD tasks.

The architecture combines two main components: 
    1. MobileNet V2 for feature extraction
    2. SSD framework for OD.


SSD is a type of OD model that predicts object classes and their corresponding bounding box
coordinates directly from a single pass of the neural network, it achieves this by using 
multiple convolutional layers with different scales to predict objects at various sizes.

MobileNet is a family of lightweight NN architectures (CNN) designed for mobile 
or other applications where real-time processing or low power consumption is crucial. In the 
context of OD, MobileNet architectures can be feature extractors for more complex 
detection frameworks like SSD, so we get efficient and real-time OD.


MobileNet on its own can indeed be used for OD, but it might not be as efficient
or accurate as specialized OD frameworks like SSD, with SSD it offers:

1. Higher-Level Features: MobileNet extracts features from the input image at different scales,
which are useful for general feature extraction tasks like image classification. However, 
OD requires features that are specifically tuned for identifying objects. SSD combines the 
multi-scale features from MobileNet with additional CNNs that are designed to
precisely predict object locations and classes.

2. Bounding Box Regression: Accurately predicting bounding box coordinates is crucial for OD.
While MobileNet can provide feature maps, SSD includes specialized layers for predicting the 
offsets needed to refine the bounding box coordinates --> object localization accuracy improved.

3. End-to-End Detection: SSD doesn't require additional steps for OD like region proposal 
generation, which is often needed in traditional two-stage OD pipelines --> faster OD.

'''

import jetson_inference as ji
import jetson_utils as ju


#create network
net = ji.detectNet('ssd-mobilenet-v2',threshold=0.5) #ssd-mobilenet is the network model to use
# lower thresh makes it recognize more, higher won't recognize much.
