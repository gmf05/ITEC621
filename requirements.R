chooseCRANmirror()
packages = c("rmarkdown", "car", "caret", "coefplot", "corrplot", "ctv", "DataCombine", "GGally", "gbm", "ggplot2", "glmnet", "HH", "Hmisc", "ISLR", "lattice", "lm", "lmtest", "leaps", "MASS", "perturb", "pls", "pROC", "psych", "randomForest", "ROCR", "tree", "VGAM", "gam", "akima", "e1071", "stargazer", "data.table", "XML", "xlsx", "xlsxjars", "rJava")

for (package in packages) {
    install.packages(package)
    #require(package)
}
