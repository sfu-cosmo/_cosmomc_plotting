_cosmomc_plotting
====================
This repo contains the code to make contour plots from CosmoMC.

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
