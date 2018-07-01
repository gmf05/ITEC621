# ITEC621: Predictive Analytics

# Setting Up (Locally)

## 1. Download [Cygwin](https://cygwin.com/install.html) (Windows users): 
Run the setup file and choose a mirror. Then find and double click the following additional Cygwin packages to install them:

* openssh

* git (optional for cloning, below)

* R (optional)


## 2. Get the course repo:

### Clone:

#### Cygwin Terminal (Windows)
```
cd /cygdrive/c/Users/$USER/Documents/ITEC621
git clone https://github.com/gmf05/ITEC696.git repo
```

#### Unix Terminal (Mac/Linux)
```
cd ~/Documents/ITEC621
git clone https://github.com/gmf05/ITEC696.git repo
```

### Download:

Download the repo as a `.zip` file and unpack it into your working directory.


#### Cygwin Terminal (Windows)
```
cd /cygdrive/c/Users/$USER/Documents/ITEC621
unzip /cygdrive/c/Users/$USER/Downloads/ITEC621-master.zip
mv ITC621-master repo
rm /cygdrive/c/Users/$USER/Downloads/ITEC621-master.zip
```

#### Unix Terminal (Mac/Linux)
```
cd ~/Documents/ITEC621
unzip ~/Downloads/ITEC621-master.zip
mv ITC621-master repo
rm ~/Downloads/ITEC621-master.zip
```

## 3. Download R:

* [Windows](http://lib.stat.cmu.edu/R/CRAN/bin/windows/base/release.htm)

* [Mac](http://lib.stat.cmu.edu/R/CRAN/bin/macosx/)

* [Linux](http://lib.stat.cmu.edu/R/CRAN/bin/linux)


## 4. Download [RStudio Desktop](https://www.rstudio.com/products/rstudio/download/#download)


##

# Setting Up (Remotely)

## 1. Download and move key

Start a Terminal (Mac/Linux) or Cygwin Terminal (Windows). Make a folder `.ssh` inside of your home directory. Then move the key from Downloads (or wherever you saved it) to this new folder `.ssh`.

#### Cygwin Terminal (Windows)
```
mkdir ~/.ssh # if it doesn't exist already
mv /cygdrive/c/Users/$USER/Downloads/AUstudent.pem ~/.ssh/
```

#### Unix Terminal (Mac/Linux)
```
mkdir ~/.ssh # if it doesn't exist already
mv $HOME/Downloads/AUstudent.pem ~/.ssh/
```

## 2. Start an SSH tunnel

`ssh -i ~/.ssh/AUstudent.pem -f -N -L 8889:localhost:8889 remote@neurocoding.info`

## 3. Connect to RStudio Server

Open a web browser and navigate to `localhost:8889`

Type in your username and password



