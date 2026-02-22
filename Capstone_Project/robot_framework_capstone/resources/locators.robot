*** Variables ***

# ---------------- REGISTER PAGE ----------------

${FIRSTNAME_INPUT}    id=input-firstname
${LASTNAME_INPUT}     id=input-lastname
${EMAIL_INPUT}        id=input-email
${PHONE_INPUT}        id=input-telephone
${PASSWORD_INPUT}     id=input-password
${CONFIRM_INPUT}      id=input-confirm

${AGREE_LABEL}        xpath=//label[@for="input-agree"]

${CONTINUE_BUTTON}    css=input.btn.btn-primary[type="submit"][value="Continue"]

${SUCCESS_TEXT}       xpath=//h1[contains(text(),"Your Account Has Been Created")]

#  My Account Menu (Correct HTML Based Locator)
${MY_ACCOUNT_MENU}    xpath=//a[contains(@href,"route=account/account") and contains(@class,"dropdown-toggle")]

#  Login Link
${LOGIN_LINK}         xpath=//a[contains(@href,"route=account/login") and contains(text(),"Login")]

# Register Link
${REGISTER_LINK}      xpath=//a[contains(@href,"route=account/register") and contains(text(),"Register")]

# ---------------- LOGIN PAGE ----------------

${LOGIN_URL}       https://ecommerce-playground.lambdatest.io/index.php?route=account/login
${EMAIL_INPUT}        id=input-email
${PASSWORD_INPUT}     id=input-password

${LOGIN_BUTTON}       css=input.btn.btn-primary[value="Login"]

# ---------------- SUCCESS VALIDATION ----------------

${MY_ACCOUNT_HEADING}    xpath=//h2[contains(text(),"My Account")]


# ---------------- SEARCH ----------------

${SEARCH_BOX}        name=search

# ---------------- SEARCH RESULTS ----------------

${FIRST_PRODUCT}     xpath=(//div[contains(@class,"product-thumb")]//h4/a)[1]

# ---------------- PRODUCT DETAILS ----------------

${PRODUCT_TITLE}     css=h1


# ---------------- ADD TO CART ----------------
${ADD_TO_CART}       css=div#entry_216842 button[title='Add to Cart']

${VIEW_CART_BTN}     xpath=//a[normalize-space()="View Cart"]

# ---------------- SUCCESS MESSAGE ----------------
${CART_SUCCESS_MSG}  xpath=//p[contains(text(),"Success: You have added")]



# ---------------- CART PAGE ----------------
${CART_HEADING}      xpath=//h1[contains(text(),"Shopping Cart")]

${QTY_BOX}           xpath=//input[contains(@name,"quantity")]

#  Update Button (Exact Button 1)
${UPDATE_BTN}        xpath=//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/div/button[1]

# Remove Button (Exact Button 2)
${REMOVE_BTN}        xpath=//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/div/button[2]

# ---------------- LOGOUT ----------------
${LOGOUT_LINK}     xpath=//a[contains(@href,"route=account/logout") and contains(text(),"Logout")]

${LOGOUT_TEXT}     xpath=//h1[contains(text(),"Account Logout")]