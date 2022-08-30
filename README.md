# MluKhiyah_API_Django

# Business requirements as per the mockup 

1- Meals list screen has the foloowing information
    - Meal name
    - Meal number of stars 
    - Meals average rate 
    - Login 
    - Register
    - showing already logged in user 

2- Popup error if the user already rated 

3- Add rate scree, stars 1 to 5 only and SAVE


# Technical requirements 
Using Django REST frame work please implement the followings

1- Models 
    - Meal
    - Stars 
    - User
    - Restaurant

2- validation if the user already rated the meal 

3- validation to rate min 1 and max 5 

4- CRUD API for Meals 
    http://127.0.0.1:8000/meal_list/
    it should return the average rating and number of rating a long with the meal name and detail

5- CRUD API for Stars 
    http://127.0.0.1:8000/rate_list/
    no one should be able to use this crud for rating !!

6-  CRUD API for Meals 
    http://127.0.0.1:8000/restaurant_list/
    it should return  number of restaurant 

7- Token authentication 

8- Login and register API 

9- Token request API 



