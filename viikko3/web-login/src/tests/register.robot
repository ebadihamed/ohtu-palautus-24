*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle1234567
    Set Password Confirmation  kalle1234567
    Submit Register
    Page Should Contain  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle12345678
    Set Password Confirmation  kalle12345678
    Submit Register
    Page Should Contain  Username does not pass the test

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  kalle12
    Set Password Confirmation  kalle12
    Submit Register
    Page Should Contain  Password does not pass the test

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  kallekallekalle
    Set Password Confirmation  kallekallekalle
    Submit Register
    Page Should Contain  Password does not pass the test

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle12345678
    Set Password Confirmation  kalle123456789
    Submit Register
    Page Should Contain  Passwords do not match

Register With Username That Is Already In Use
    Set Username  hamedebadi
    Set Password  kalle12345678
    Set Password Confirmation  kalle123456789
    Submit Register
    Page Should Contain  Username is already taken

*** Keywords ***

Set Password Confirmation
    [Arguments]  ${password}
    Input Text  password_confirmation  ${password}

Submit Register
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  hamedebadi  hamed123123123
    Go To Register Page