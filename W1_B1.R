# Run the following command:
.libPaths()

# This prints the list of paths where RStudio looks
# for packages. Note there are multiple folders.

# 1. What do you think the following two lines do?
print(.libPaths()[1])
keras_dir = paste(.libPaths()[1], '/keras', sep='')

# 2. Try both of these ways to print the variable keras_dir.
# Do they give the same output?
print(keras_dir)
keras_dir

# 3. Try running the following command to load the library keras
# What does the error message say? What does it mean?
library(keras)

# 4. Run the following command to list the contents of a directory:
# What does it return?
list.dirs(keras_dir)

# 5. Now try installing the package keras
# What happens in the Console as it installs?
install.packages(keras)

# 6. What happens now? Why does this work compared to the previous line?
install.packages('keras')