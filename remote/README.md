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

