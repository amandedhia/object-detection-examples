# object-detection-examples
Object detection small example projects using only OpenCV on python and no ML and Deep Learning.

This includes a few object detection projects that I made during my (currently ongoing) process of learning Computer Vision. All the current projects are only made using OpenCV on python and no ML and/or Deep Learning is invloved.

Projects in this repository:
>colour_ball.py: This program tracks any coloured ball (currently tuned to red) from a webcam input stream. Refer this project to understand concepts of object detection which uses thresholding, morphology, contours, polygon approximation, etc. It's a basic method that I figured from refering different sources of which I'll list down the ones I links for in the reference section below. Also, check out Hough Circles to detect circular objects. I have not tried to implement it but it could be useful for people trying to work mainly with circular objects. Watershed is another very interesting algorithm and I'd advice people to check it out. I did try implementing it initially but I was not able to implement it in a way that would/could provide better results for the program so I decided to omit it from the code. Would appreciate if someone can share sources and/or implementation to explain rightly execute it in a beneficial way (especially with respect to this program). I will link the sources I refered to in the reference section below. 

>dice_value.py: This is another example of object detection using OpenCV build on the concepts of thresholding, morphology, contours. It takes a single image as input (not exactly, you need to mention the file name in the code, I would update it such that it takes input later). It uses hierarchy of contours to acheive the desired result and is a simple project to understand and work with hierarchy of contours. OpenCV's documentation on hierarchy is sufficient to understand the concepts of contours hierarchy and I  would suggest to refer it before refering this program. Link in resources. (space, space)

Resources:
>Image segmentation and thresholding: https://datacarpentry.org/image-processing/07-thresholding/

>Contours: https://datacarpentry.org/image-processing/09-contours/

>Contour Hierarchy: https://docs.opencv.org/trunk/d9/d8b/tutorial_py_contours_hierarchy.html

>Morphological Transformation: https://docs.opencv.org/trunk/d9/d61/tutorial_py_morphological_ops.html

>Polygon approximation: https://pysource.com/2018/09/25/simple-shape-detection-opencv-with-python-3/

>Watershed: https://docs.opencv.org/master/d3/db4/tutorial_py_watershed.html
