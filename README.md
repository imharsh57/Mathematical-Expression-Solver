# Mathematical-Expression-Solver
A complete web application which solves the mathematical expression
* It scrapped the expression from Image and provide the result.
* Expression written either in Computerized Text or Handwritten Text.
* It can also solve Differentiation, Integration or Multi-Variable expression.
* Designed a UI with the help of Flask for taking expression as input in form of Image or Text.

# Implementation
* Input image is divided into 2 parts -> Segmentation & Recognition
  (Segmentation-> Seperate text into individual character.....Recognition-> recognise each seperated character through suitable Algorithm)
* We have used convolutional neural network  and OpenCV for the recognition of handwritten text and flask for the user interface. 
* CNN is a neural network that has one or more convolutional layers and are used mainly for image processing, classification, segmentation.
* OpenCV (Open Source Computer Vision) is a library of programming functions mainly aimed at  real-time computer vision. In simple language it is library used for Image Processing. It is mainly used to do all the operation related to Images.
* Flask is a web framework. This means flask provides you with tools, libraries, and technologies that allow you to build a web application.

See Architecture diagram & Text recognition process in image --> MES_Architecture_Diagram.png & MES_Text_recognition_process.png
