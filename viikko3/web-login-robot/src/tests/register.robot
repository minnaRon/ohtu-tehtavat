*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  validUsername
    Set Password  validPassword123
    Set Password Confirmation  validPassword123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  sh
    Set Password  validPassword123
    Set Password Confirmation  validPassword123
    Submit Credentials
    Register Should Fail With Message  Username should be longer than 2 characters

Register With Valid Username And Too Short Password
    Set Username  validUsername
    Set Password  short3
    Set Password Confirmation  short3
    Submit Credentials
    Register Should Fail With Message  Password should be at least 8 characters and also contains other characters than letters

Register With Nonmatching Password And Password Confirmation
    Set Username  validUsername
    Set Password  NonMatchPassword123
    Set Password Confirmation  NonMatchPassword456
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation are different

*** Keywords ***
Submit Credentials
    Click Button  Register
    
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password} 
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
