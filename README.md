# ITEC621: Predictive Analytics

## 1. Download R:

* [Windows](http://lib.stat.cmu.edu/R/CRAN/bin/windows/base/release.htm)

* [Mac](http://lib.stat.cmu.edu/R/CRAN/bin/macosx/)

* [Linux](http://lib.stat.cmu.edu/R/CRAN/bin/linux)


## 2. Download [RStudio Desktop](https://www.rstudio.com/products/rstudio/download/#download)

## 3. Clone the course repo

### 3a. Windows users: Download [Cygwin Terminal](https://cygwin.com/install.html)

Run the setup file and choose a mirror. When you get to the package selection prompt, use the search bar at the top to type in the following package names. For each package, search for the matching name, description, and category, then click the package to select it.

* *git: Distributed version control system* Category: Devel. For file version control.

* *openssh: The OpenSSH server and client programs*. Category: Net. For remote computing. (Optional)

* *vim: Vi IMproved Text Editor.* Category: Editors (Optional)

### 3b. Clone repo

Open a terminal, navigate to a folder where you want to save your work for ITEC 621, and use `git clone` to get the repo:

```bash
# windows users only:
ln -s /cygdrive/c/Users/$USER/Code ~/Code

# all users:
cd ~/Code
git clone https://github.com/gmf05/ITEC696.git
```

## 4. Install R libraries

Run the file `requirements.R`, which will install a series of libraries.

## 5. Explore [`HW1-Example.Rmd`](https://raw.githubusercontent.com/gmf05/ITEC621/master/HW1-Example.Rmd), try knitting (optional)



