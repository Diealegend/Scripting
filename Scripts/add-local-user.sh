#!/bin/bash

# This script creates an account on the local system.
# You will be prompted for the account name and password.

#Make sure the script is being executed with superuser privileges.
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# Ask for the username
read -p 'Enter Username: ' USER_NAME

# Ask for the real name
read -p 'Enter THE NAME OF THE PERSON: ' COMMENT

# Ask for the password
read -s -p 'Enter THE PASSWORD TO USE FOR THIS USER ACCOUNT: ' PASSWORD
echo

# Create the user
useradd -c "${COMMENT}" -m "${USER_NAME}"

#Check if the user creation was successful 
#then we know that the exit status of the most previously executed command is stored in dollar sign question mark.
#And so again, as convention holds, if it's an exit status of zero, that means everything went well,
#the command succeeded, and if it's not zero, then something went wrong.
# So if the exit status is not equal to zero, that's what the dash e stands for.

#Then we're going to display an error message.And then we're going to exit our script with a non zero exit status.
#Now, assuming that we get past the if statement in the script, that means the user ad command succeeded.
if [ $? -ne 0 ]; then
echo "Failed to create user ${USER_NAME}"
exit 1
fi

# Set the password for the user
echo "${USER_NAME}:${PASSWORD}" | chpasswd

# Force password change on first login
passwd -e "${USER_NAME}"

# Change the user's shell to /bin/bash
usermod -s /bin/bash "${USER_NAME}"

# Display the username, password, and the host where the user was created.
echo "Username: ${USER_NAME}"
echo "Password: ${PASSWORD}"
echo "Host: $(hostname)"
