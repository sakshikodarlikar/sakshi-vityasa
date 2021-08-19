# vityasa-task
https://github.com/vityasa/hiring-2021


Code deployed on Heroku: https://vityasa-sakshi.herokuapp.com/



## Task 1

POST a list in text format on ```https://vityasa-sakshi.herokuapp.com/items``` 
eg: 
```javascript
[1, 4, -1, "hello", "world", 0, 10, 7]
```



## Task 2


POST on ```https://vityasa-sakshi.herokuapp.com/booking``` to create a booking.
eg:
```javascript
{
  "slot": 1, "name": "John"
}
```
Use GET method on ```https://vityasa-sakshi.herokuapp.com/booking``` to see all bookings.

POST on ```https://vityasa-sakshi.herokuapp.com/cancel``` to cancel a booking.
eg:
```javascript
{
  "slot": 1, "name": "John"
}
```



## Task 3


POST on ```https://vityasa-sakshi.herokuapp.com/plot``` continuously x and y co-ordinates 
eg:
```javascript
{
  "x": 1, "y": 1
}
```
After formation of perfect square it returns the co-ordinates of all the four points and deletes all the points posted before.
