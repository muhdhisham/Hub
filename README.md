| :zap:        Hacktoberfest 2021 is here! Contribute and win Activeloop swag. Grab an issue in our  <a href="https://github.com/activeloopai/Hub/projects/11"><b>Hacktoberfest dashboard</b></a>! :zap: |
|-----------------------------------------|

<img src="https://static.scarf.sh/a.png?x-pxid=bc3c57b0-9a65-49fe-b8ea-f711c4d35b82" /><p align="center">
    <img src="https://www.linkpicture.com/q/hub_logo-1.png" width="35%"/>
    </br>
    <h1 align="center">Dataset Format for AI
 </h1>
<p align="center">
    <a href="https://pypi.org/project/hub/"><img src="https://badge.fury.io/py/hub.svg" alt="PyPI version" height="18"></a>
    <a href="https://pepy.tech/project/hub"><img src="https://static.pepy.tech/personalized-badge/hub?period=month&units=international_system&left_color=grey&right_color=orange&left_text=Downloads" alt="PyPI version" height="18"></a>
    <a href="https://app.circleci.com/pipelines/github/activeloopai/Hub">
    <img alt="CircleCI" src="https://img.shields.io/circleci/build/github/activeloopai/Hub?logo=circleci"> </a>
     <a href="https://github.com/activeloopai/Hub/issues">
    <img alt="GitHub issues" src="https://img.shields.io/github/issues/activeloopai/Hub"> </a>
    <a href="https://codecov.io/gh/activeloopai/Hub/branch/main"><img src="https://codecov.io/gh/activeloopai/Hub/branch/main/graph/badge.svg" alt="codecov" height="18"></a>
  <h3 align="center">
   <a href="https://docs.activeloop.ai/?utm_source=github&utm_medium=readme&utm_campaign=docsbutton&utm_id=docs/"><b>Documentation</b></a> &bull;
   <a href="https://docs.activeloop.ai/getting-started-with-hub/?utm_source=github&utm_medium=readme&utm_campaign=docsbutton&utm_id=docs/%22%3E"><b>Getting Started</b></a> &bull;
      <a href="https://github.com/activeloopai/examples"><b> Examples </b></a> &bull; 
      <a href="https://api-docs.activeloop.ai/"><b>API Reference</b></a> &bull;  
  <a href="http://slack.activeloop.ai"><b>Slack Community</b></a> &bull;
  <a href="https://twitter.com/intent/tweet?text=The%20fastest%20way%20to%20access%20and%20manage%20PyTorch%20and%20Tensorflow%20datasets%20is%20open-source&url=https://activeloop.ai/&via=activeloopai&hashtags=opensource,pytorch,tensorflow,data,datascience,datapipelines,activeloop,dockerhubfordatasets"><b>Twitter</b></a>
 </h3>

## Why use Hub?
**ML engineers spend the majority of their time building infrastructure, transferring data, and writing boilerplate code. The Hub format + API simplifies these tasks so that users can focus on building amazing machine learning models 💻.**

Hub enables users to stream unlimited amounts of data from the cloud to any machine without sacrificing performance compared to local storage 🚀. In addition, Hub connects datasets to PyTorch and TensorFlow with minimal boilerplate code, and it has powerful tools for dataset version control, building ML pipelines, and running distributed workloads.

Hub is best suited for unstructured datasets such as images, videos, point clouds, or text. It works locally or on any cloud.

Google, Waymo, Red Cross, Omdena, and Rarebase use Hub.

## How does Hub work?

Databases, data lakes, and data warehouses are best suited for tabular data and are not optimized for deep-learning applications using images, videos, and text. By storing data as chunked compressed arrays, Hub significantly increases data transfer speeds between network-connected machines. This eliminates the need to download entire datasets before running code, because computations and data streaming can occur simultaneously without increasing the total runtime.

Hub also significantly reduces the time to build machine learning workflows, because its API eliminates boilerplate code that is typically required for data wrangling ✌️.

## Features 
### Current Release
* Easy dataset creation and hosting on Activeloop Cloud, S3, or Google Cloud
* Rapid dataset streaming to any machine
* Simple dataset integration to PyTorch and TensorFlow with no boilerplate code
* Rapid data processing using transformations on distributed compute
* Data pipelines
* Dataset version control (alpha)

### Coming Soon
* Dataset hosting on Azure
* Dataset query without having to download the entire dataset
* Rapid visualization of image datasets via integration with Activeloop Platform
 <p align="center">
    <br>
    <img src="https://raw.githubusercontent.com/activeloopai/Hub/master/docs/visualizer%20gif.gif" width="75%"/>
    </br>
Visualization of a dataset uploaded to Hub

## Getting Started with Hub
### Installation
Hub is written in 100% python and can be quickly installed using pip.
```sh
pip3 install hub
```
### Loading Datasets
Accessing datasets in Hub requires a single line of code. Run this snippet to get the first image in the [Objectron Bikes Dataset](https://github.com/google-research-datasets/Objectron) in the numpy array format:
```python
import hub

ds = hub.load('hub://activeloop/objectron_bike_train')
image_arr = ds.image[0].numpy()
```
To access and train a classifier on your own Hub dataset stored in cloud, run:
```python
import hub

ds = hub.load("s3://bucket_name/dataset_folder")
data_loader = ds.pytorch(batch_size = 16, num_workers = 4)

for batch in data_loader:
    print(batch)

## Training Loop Here ##
```
### Creating Datasets
To upload your own dataset to Hub:
```python
import hub

fns = my_images # List of image files in dataset

# Define empty dataset
ds = hub.empty("gcp://bucket_name/dataset_folder")

# Upload data
with ds:

    # Create tensors
    ds.create_tensor('images', htype = 'image', sample_compression = 'jpg')
    ds.create_tensor('labels', htype = 'class_label')
    
    # Append data
    for fn in fns:
        ds.images.append(hub.read(fn))
        ds.labels.append(my_label_parser(fn))
```

## Documentation
Getting started guides, examples, tutorials, API reference, and other usage information can be found on our [documentation page](http://docs.activeloop.ai/?utm_source=github&utm_medium=repo&utm_campaign=readme). 

## 🎓 For Students and Educators
Hub users can access and visualize a variety of popular datasets through a free integration with Activeloop's Platform. Users can also create and store their own datasets and make them available to the public. Free storage of up to 300 GB is available.


## Comparisons to Familiar Tools
### Hub and DVC
Hub and DVC offer dataset version control similar to git for data, but their methods for storing data differ significantly. Hub converts and stores data as chunked compressed arrays, which enables rapid streaming to ML models, whereas DVC operates on top of data stored in less efficient traditional file structures. The Hub format makes dataset versioning significantly easier compared to a traditional file structures by DVC when datasets are composed of many files (i.e. many images). An additional distinction is that DVC primarily uses a command line interface, where as Hub is a python package. Lastly, Hub offers an API to easily connect datasets to ML frameworks and other common ML tools.

### Hub and TensorFlow Datasets (TFDS)
Hub and TFDS seamlessly connect popular datasets to ML frameworks. Hub datasets are compatible with both PyTorch and TensorFlow, whereas TFDS are only compatible with TensorFlow. A key difference between Hub and TFDS is that Hub datasets are designed for streaming from the cloud, whereas TFDS must be downloaded locally prior to use. In addition to providing access to popular publicly-available datasets, Hub also offers powerful tools for creating custom datasets, storing them on a variety of cloud storage providers, and collaborating with others. TFDS is primarily focused on giving the public easy access to commonly available datasets, and management of custom datasets is not the primary focus.

### Hub and HuggingFace 
Hub and HuggingFace offer access to popular datasets, but Hub primarily focuses on computer vision, whereas HuggingFace primarily focuses on natural language processing. HuggingFace Transforms and other computational tools for NLP are not analogous to features offered by Hub.

## Community

Join our [**Slack community**](https://join.slack.com/t/hubdb/shared_invite/zt-ivhsj8sz-GWv9c5FLBDVw8vn~sxRKqQ) to learn more about unstructured dataset management using Hub and to get help from the Activeloop team and other users.

We'd love your feedback by completing our 3-minute [**survey**](https://forms.gle/rLi4w33dow6CSMcm9).

As always, thanks to our amazing contributors!    

<a href="https://github.com/activeloopai/hub/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=activeloopai/hub" />
</a>

Made with [contributors-img](https://contrib.rocks).

Please read [CONTRIBUTING.md](CONTRIBUTING.md) to get started with making contributions to Hub.


## README Badge

Using Hub? Add a README badge to let everyone know: 


[![hub](https://img.shields.io/badge/powered%20by-hub%20-ff5a1f.svg)](https://github.com/activeloopai/Hub)

```
[![hub](https://img.shields.io/badge/powered%20by-hub%20-ff5a1f.svg)](https://github.com/activeloopai/Hub)
```



## Disclaimers

### Dataset Licenses
Hub users may have access to a variety of publicly available datasets. We do not host or distribute these datasets, vouch for their quality or fairness, or claim that you have license to use the datasets. It is your responsibility to determine whether you have permission to use the datasets under their license.

If you're a dataset owner and do not want your dataset to be included in this library, please get in touch through a [GitHub issue](https://github.com/activeloopai/Hub/issues/new). Thank you for your contribution to the ML community!

### Usage Tracking
By default, we collect anonymous usage data using Bugout (here's the [code](https://github.com/activeloopai/Hub/blob/853456a314b4fb5623c936c825601097b0685119/hub/__init__.py#L24) that does it). It does not collect user data and it only logs the Hub library's own actions. This helps our team understand how the tool is used and how to build features that matter to you! After you register with Activeloop, data is no longer anonymous, but you can  opt-out of reporing using the CLI command below:

```
activeloop reporting --off
```

## Acknowledgment
This technology was inspired by our research work at Princeton University. We would like to thank William Silversmith @SeungLab for his awesome [cloud-volume](https://github.com/seung-lab/cloud-volume) tool.
