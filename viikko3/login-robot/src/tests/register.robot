*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  NewUsername  NewPassword
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  Username already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  newPassword
    Output Should Contain  Username should be longer than 2 characters

Register With Valid Username And Too Short Password
    Input Credentials  newPassword  short2
    Output Should Contain  Password should be at least 8 characters and also contains other characters than letters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  newPassword  onlyletters
    Output Should Contain  Password should be at least 8 characters and also contains other characters than letters

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command
