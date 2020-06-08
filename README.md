# Image Processing
A compilation of Image Processing programs that I've worked on.

## Motivation
This entire repository has been built on the documentation provided, and the guidance offered by **Professor Sibi Chakkaravarthy**, from the years I've studied in the university, Vellore Institute of Technology AP, and he has guided me through the learning process of Image Processing, and it's use cases.

This repository was made to self-evaluate and debug errors in the programs, since there are significant issues with changing programs from Python 2 to Python 3.

## Index

**Chapter 1** : [Basics of Computer Vision](#chapter-1)<br>
**Chapter 2** : [Image Descriptor](#chapter-2)<br>
**Chapter 3** : [Building your own custom object detector](#chapter-3)<br>
**Chapter 4** : [Working with Raspberry Pi](#chapter-4)<br>
**Chapter 5** : [Image Classification and Machine Learning](#chapter-5)<br>
**Chapter 6** : [Case Studies](#chapter-6)<br>

## Chapter 1

This section of the programs essentially teaches you the basic concepts of computer vision and the usage of opencv, and cv2.
Through the code's execution, you learn essential aspects such as,
```
- Loading and writing images to disks
- Manipulating pixels to change images
- Drawing using OpenCV and Numpy
- Basic operations on images - translation, rotation, resizing, flipping, and cropping
- Arithmatic operations performed on images
- Bitwise operations using Numpy and OpenCV
- Masking images to retrieve certain aspects of the image
- Splitting and merging color channels present in an image
- Utilizing kernels in order to perform morphological operations on images
- Smoothing and blurring images through different methods
- Working with color and colorspaces
- Thresholding images using different methods
- Gradient orientation and Sobel kernels
- Edge detection and Contour identification
- Contour properties
- Case Studies - Tic Tac Toe, and Tetris
- Contour Approximation and Sorting Contours
- Histogram Masks and Histogram Equalization
- Connected Component Labelling
```

Link to the the [chapter](https://github.com/dat-adi/image-processing/tree/master/basics_of_computer_vision).

## Chapter 2

This section is dedicated to the programs which are useful for learning the usage of feature vectors, image descriptors, and feature descriptors.

Throughout this section you will learn about the concepts such as,
```
- Color channel statistics
- Image description using color histograms
- Local binary pattern usage
- Utilization of histogram of Oriented Gradients
- Keypoint Detection using FAST, Harris, and Difference of Gaussian methods
- SIFT Feature Descriptor
```

Link to the [chapter](https://github.com/dat-adi/image-processing/tree/master/image_descriptor).

## Chapter 3

This section is to help you build your own custom model of an object detector, some programs in order to train your detector while other programs to test them.

In this section, there are multiple case studies, and most of the programs will be focusing on real world items, and detection.

```
- Training your object detector to detect stop signs
- Utilising image pyramids for testing images
- Using Sliding windows to figure out the exact location where an image resides
- Building a custom object detector for training and testing
```

Link to the [chapter](https://github.com/dat-adi/image-processing/tree/master/building_custom_detectors).

## Chapter 4

This section of the programs are to be utilised in order to test their functionality in Raspberry Pi, and whether OpenCV can be used with projects on small and simple boards to make technical projects.

This section is very short, concentrating more on taking input from the surroundings, rather than using computing or detecting algorithms.

```
- Home Surveillance and Motion Detection
- Face Detection in Images
- Detecting faces through a Video
```

Link to the [chapter](https://github.com/dat-adi/image-processing/tree/master/working_with_raspberry_pi).

## Chapter 5

This section is for learning the implementation and integration between OpenCV and Machine Learning, testing Supervised Learning algorithms.

The programs in this section are useful to realise the concepts, such as,
```
- Using supervised learning to train and test datasets, using MNIST as a platform
- Using Logistic Regression as a measure to implement machine learning, and image classification
- Support Vector machine for image classification
- Using the KMeans algorithm in order to display and classify images based on their properties
```

Link to the [chapter](https://github.com/dat-adi/image-processing/tree/master/image_classification).

## Chapter 6

This section is dedicated to specific case studies, on implementing OpenCV and Machine Learning to experiment with datasets and image classification.

The case studies which will be tried and tested are,
```
- Video Object Tracking
- Book Cover Identification
- Plant Classification
```

Link to the [chapter](https://github.com/dat-adi/image-processing/tree/master/case_studies).