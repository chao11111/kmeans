# K-means
Python Implementation Of Color Reduction Using K-Means Clustering

## Example - Paris Street
### Original
![Paris Street](./assets/demo.jpg)
### K = 3
![Paris Street Reduced to 3](./assets/demo_reduced_3.bmp)
### Original to K = 3
![Paris Street original to 3](./assets/demo_18to3.gif)

## Abstract
This gets a list of RGB color tuples from a given image and treats them as 3-dim vectors. Group those vectors regarding to how far they are from one another by Euclidean measure. And assign the avarage color to each group, and apply it to the original image.

## Usage
```bash
$ git clone git@github.com:honake/kmeans.git
$ # If you haven't installed pillow
$ pip3 install pillow
$ cd kmeans
$ # Put an image file in this directory
$ python3 main.py demo.jpg 5
$ # => Converting...
$ # => Almost There...
$ # => Finished !
```
First argument is the image's path, and second is parameter K, which denotes how many colors the image will be reduced to.

## References
- wikipedia
 - https://en.wikipedia.org/wiki/K-means_clustering
- gifcreator
 - http://gifcreator.me/
