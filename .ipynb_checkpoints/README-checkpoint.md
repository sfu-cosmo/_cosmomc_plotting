_cosmomc_plotting
====================
This repo contains the code to make contour plots from CosmoMC. 

I'm collecting a set of scripts for plots out of CosmOMC, for example [this plot here](plots/test_plot.png).

## 1. Usage
This should be [syzygy](https://sfu.syzygy.ca) friendly. There are two options to use this repo.

1. On your local machine, provided you have installed a `python` interpreter with the `PyPI` package installer. 
2. On [syzygy](https://sfu.syzygy.ca).

### 1.1 Running on local
On your local machine first clone the repo, 
```bash
git clone https://github.com/sfu-cosmo/_cosmomc_plotting.git
```

Then 
```bash
cd _cosmomc_plotting

pip install -r requirements.txt
```

Then you, if you have `jupyter notebook` you can use the [`example_notebook.ipynb`](./example_notebook.ipynb), or from a Python console
```python
import sfu_cosmo_plots as splots
import numpy as np
import matplotlib.pyplot as plt

dir_root = './example_data/'
file_root = 'example_1_mu_sigma'
out_root = './plots/'
splots.plot_contour_2D(dir_root, file_root, out_root)
```
### 1.2 Running on SYGYZY
Log in on [syzygy](https://sfu.syzygy.ca) with SFU credentials.

Then press `New -> Terminal` and you will be prompted to a terminal window. From there, clone the repo:
```
git clone https://github.com/sfu-cosmo/_cosmomc_plotting.git
```
Then on the previous file explorer window, you'll see appearing the directory `_cosmomc_plotting`. Click on it.

You'll see a notebook icon, `example_notebook.ipynb`, click on it and you will run the Jupyter notebook for the example_notebook. 

Run each cell with `SHIFT+ENTER`.