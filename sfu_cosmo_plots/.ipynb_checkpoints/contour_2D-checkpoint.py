# Importing the plotting libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
import matplotlib as mpl
import pylab as pil




def contour_2D_plot(root_dir, 
                   file_root, 
                   out_root, 
                   x_label, 
                   y_label, 
                   labels,
                   n_datasets, 
                   x_lim=None,
                   y_lim=None,
                   use_latex_font=True,
                   hlines=None,
                   vlines=None,
                   legend_loc='upper right',
                   figsize=(8, 6),
                   alpha=0.65):
    """
    This function creates the contour plot.
    """
    
    # some output
    print('Plotting:', n_datasets, 'data sets.')
    
    # this set the LaTeX font
    if use_latex_font:
        from matplotlib import rc
        rc('font', **{'size': 16, 'family': 'serif', 'serif': ['Computer Modern Roman']})
        rc('text', usetex=True)
    
    
    # check the length of the file_root if it's a list
    #if file_root is list:
    #    print('file_root has length:', len(file_root))
    if len(file_root) != n_datasets:
        raise RunTimeError('len of file_root should be = to n_datasets')    
    #else:
    #    file_root = [file_root]
            
    # set up the figure
    fig = plt.figure(figsize=figsize)
           
    cs = []
    css = []
    
    color_map = [('#d98c8c', 'darkred'), ('moccasin', 'orange')]
    
    for idd in range(len(file_root)): 
        fr = file_root[idd]
        # load the data
        print(idd, fr)
        x  = np.loadtxt(root_dir+fr+'_x')
        y  = np.loadtxt(root_dir+fr+'_y')
        Z  = np.loadtxt(root_dir+fr)
        lev = np.loadtxt(root_dir+fr+'_cont')


        lev = [lev[1], lev[0], 1]
        lev1= [lev[1], 1]

        X,Y = np.meshgrid(x,y)
        

        CS = plt.contourf(X, Y, Z, lev, colors=color_map[idd], alpha=alpha)
        CSS = plt.contour(X, Y, Z, lev, colors=color_map[idd][1], alpha=alpha)
        #CS2 =plt.contourf(X2, Y2, Z2, lev2, colors = ('moccasin', 'orange'), alpha=0.5)#, extend='max',)#, 10, [0.68, 0.95])#,)
        #CS22=plt.contour(X2, Y2, Z2, lev2, colors = ('orange'), alpha = 0.5 )#, label=r"Planck ")

        cs.append(CS)
        css.append(CSS)

    ## mu_0 / Sigma_0
    if x_lim is not None:
        plt.xlim(x_lim)
    if y_lim is not None:
        plt.ylim(y_lim)
        
        
    plt.xlabel(x_label, fontsize=20)
    plt.ylabel(y_label, fontsize=20)


    # legend
    lines=[c.collections[0] for c in css]
    
    #if labels is not list:
    #    labels = [labels]
        
    #labels=['model 1','model 2']
    leg = plt.legend(lines, labels, loc=legend_loc)# bbox_to_anchor=(0.5, -0.15),
    #          fancybox=True, shadow=True)#, ncol=5)
    for legobj in leg.legendHandles:
        legobj.set_linewidth(15.0)


    # horizontal-vertical lines
    if hlines is not None:
        for hy in hlines:
            plt.axvline(hy, linewidth = 0.75, color='black', alpha=0.25, linestyle='--')
            
    if vlines is not None:
        for vx in vlines:
            plt.axhline(vx, linewidth = 0.75, color='black', alpha=0.25, linestyle='--')
    

    pil.savefig('./plots/'+out_root+'.pdf', bbox_inches='tight')
    pil.savefig('./plots/'+out_root+'.png', bbox_inches='tight')
    plt.show()
