*** Settings ***
Library           RequestsLibrary
Library           Collections

Suite Setup       Create Session    foodapi    http://127.0.0.1:5006

*** Variables ***
${BASE_URL}       /api/v1

${RESTAURANT_NAME}    Test Restaurant
${CATEGORY}           Fast Food
${LOCATION}           Nodia
${IMAGES}             ["img1.jpg"]
${CONTACT}            9999999999

${USER_NAME}          John
${USER_EMAIL}         john@test.com
${PASSWORD}           123456

${DISH_NAME}          Burger
${DISH_TYPE}          Veg
${PRICE}              150
${TIME}               Lunch
${IMAGE}              burger.jpg

${RATING}             5
${COMMENT}            Excellent

*** Test Cases ***

Register Restaurant
    ${body}=    Create Dictionary
    ...    name=${RESTAURANT_NAME}
    ...    category=${CATEGORY}
    ...    location=${LOCATION}
    ...    images=${IMAGES}
    ...    contact=${CONTACT}

    ${response}=    POST On Session    foodapi    ${BASE_URL}/restaurants    json=${body}
    Should Be Equal As Integers    ${response.status_code}    201

    ${json}=    Set Variable    ${response.json()}
    Set Suite Variable    ${RESTAURANT_ID}    ${json["id"]}


Add Dish
    ${body}=    Create Dictionary
    ...    name=${DISH_NAME}
    ...    type=${DISH_TYPE}
    ...    price=${PRICE}
    ...    available_time=${TIME}
    ...    image=${IMAGE}

    ${response}=    POST On Session    foodapi    ${BASE_URL}/restaurants/${RESTAURANT_ID}/dishes    json=${body}
    Should Be Equal As Integers    ${response.status_code}    201

    ${json}=    Set Variable    ${response.json()}
    Set Suite Variable    ${DISH_ID}    ${json["id"]}


Register User
    ${body}=    Create Dictionary
    ...    name=${USER_NAME}
    ...    email=${USER_EMAIL}
    ...    password=${PASSWORD}

    ${response}=    POST On Session    foodapi    ${BASE_URL}/users/register    json=${body}
    Should Be Equal As Integers    ${response.status_code}    201

    ${json}=    Set Variable    ${response.json()}
    Set Suite Variable    ${USER_ID}    ${json["id"]}


Place Order
    ${dish_list}=    Create List    ${DISH_ID}

    ${body}=    Create Dictionary
    ...    user_id=${USER_ID}
    ...    restaurant_id=${RESTAURANT_ID}
    ...    dishes=${dish_list}

    ${response}=    POST On Session    foodapi    ${BASE_URL}/orders    json=${body}
    Should Be Equal As Integers    ${response.status_code}    201

    ${json}=    Set Variable    ${response.json()}
    Set Suite Variable    ${ORDER_ID}    ${json["id"]}


Give Rating
    ${body}=    Create Dictionary
    ...    order_id=${ORDER_ID}
    ...    rating=${RATING}
    ...    comment=${COMMENT}

    ${response}=    POST On Session    foodapi    ${BASE_URL}/ratings    json=${body}
    Should Be Equal As Integers    ${response.status_code}    201


Approve Restaurant (Admin)
    ${response}=    PUT On Session    foodapi    ${BASE_URL}/admin/restaurants/${RESTAURANT_ID}/approve
    Should Be Equal As Integers    ${response.status_code}    200


View All Orders (Admin)
    ${response}=    GET On Session    foodapi    ${BASE_URL}/admin/orders
    Should Be Equal As Integers    ${response.status_code}    200
