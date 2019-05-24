__Properties and methods__
---
*Information about how the objects are connected*

The houses and batteries are connected to each other through the cable object.
### Battery
---

*Properties:*
- ID - integer
- X-coordinate - integer
- Y-coordinate - integer
- Maximum capacity - float
  - The maximum capacity of the battery
- Capacity - float
  - Current capacity of the battery
- Type of battery - string
  - Used for the CSV files
- Price - integer

*Methods*
- All the get functions for ID, coordinates, capacity, type and price.
- Set coordinate function
  - Used for the move function in helpers
- Reduce capacity function
  - Used to reduce the capacity when a house is connected
- Reset capacity function
  - Reset the capacity of the battery to the maximum capacity


## House
---

*Properties*
- ID - integer
- X-coordinate - integer
- Y-coordinate - integer
- Maximum output - float

*Methods*
- All the get functions for ID, coordinates and maximum output

### Cable
---

*Properties*
- ID - integer
- Price - integer
- Battery_id - string
- Route - list

*Methods*
- All the get functions for id, batttery_id and price.
- A get length function
  - Used to calculate the total length of the cable
- A route function
  - Used to return the route that the cable has
- An add battery function
- An add house function
- Function to add a route between batteries and houses
- Function to change the route between batteries and houses

## Grid
---

*Properties*
- ID - integer
- X-max - integer
- Y-max - integer
- Cables - dictionary
- Batteries - dictionary
- Houses - dictionary

*Methods*
- All the get functions for id, x and y max (for the grid).
- Functions to get houses, batteries and cables as an object
- Function to calculate the total length of all the cables
- Function to calculate the total costs of the configuration
- Functions to add houses, batteries and cables to the dictionaries
- Function to remove cables from the dictionary
- Function to clear all the cable connections, while resetting the capacity of the battery
