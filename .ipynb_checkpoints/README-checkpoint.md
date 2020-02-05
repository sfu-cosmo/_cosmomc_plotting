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
import sfu_cosmo_plots.contour_2D as splots

# root_dir is the directory where the data is stored
root_dir = './example_data/'

# root_file is a list of files with the root of the dataset analyzed
root_file = ["MG_2_DE0_mnu_DES_std_2D_sigma0m1_mu0m1", "MG_2_DE2_mnu_DES_std_2D_sigma0m1_mu0m1"]

# output image name (without .pdf or .png)
out_root = 'test_plot'

# labels for the daasets (length has to match that of root_file)
labels = [r'$\Lambda$CDM', r'$(w_0, w_a)$']

splots.contour_2D_plot(root_dir=root_dir, 
                       file_root=root_file, 
                       out_root=out_root, 
                       x_label=r'$\mu_0 - 1$',
                       y_label=r'$\Sigma_0 -1$',
                       labels=labels, 
                       n_datasets=2, 
                       x_lim=(-1,1), 
                       y_lim=(-0.3,0.3), 
                       use_latex_font=True, 
                       hlines=None, 
                       vlines=None,
                       legend_loc='upper right', 
                       figsize=(8,6), 
                       alpha=0.65)
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