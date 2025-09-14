# alu-AirBnB_clone

## Project Description
This is the first step to build the AirBnB clone web application. 
In this stage, we have a command interpreter that manages AirBnB objects such as 'User', 'State', 'City', 'Place', and so on.

The command interpreter allows us to:
- Create a new object(for example, a new user)
- Retrieve an object from storage
- Perform operations on objects(count, compute stats, etc.)
- Modify object properties
- Remove an  object

This project provides a foundation for eventual activities such as HTML/CSS templating, database storage, APIs, and front-end integration.

## Command interpreter

### How to start
1. Clone the repository:
https://github.com/Linda5-umwali/alu-AirBnB_clone.git

cd AirBnB_clone

3. Run the console in interactive mode

   ./console.py
   
   you will see the prompt (hbnb).
   
   type commands and press Enter:

   scss
   
   copy code
   
   (hbnb) help
   
   (hbnb) create User
   
   (hbnb) show User <id>
   
   (hbnb) quit
   
5. Examples

(hbnb) create User
1234-5678-9012-3456

(hbnb) show User 1234-5678-9012-3456
[User] (1234-5678-9012-3456) {'id': '1234-5678-9012-3456', 'created_at': '2025-09-14T19:00:00', 'updated_at': '2025-09-14T19:00:00'}

(hbnb) all User
["[User] (1234-5678-9012-3456) {...}"]

(hbnb) update User 1234-5678-9012-3456 email "user@example.com"

(hbnb) destroy User 1234-5678-9012-3456

(hbnb) quit

