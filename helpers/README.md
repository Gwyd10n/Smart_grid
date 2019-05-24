__Algorithms__
---


### Random algorithm
---
- Connects houses and batteries randomly, with capacity of the batteries in mind.

### Greedy
---
- This greedy connects every house to the nearest battery, that has enough available capacity.

### Greedy2
---
- This is a greedy algorithm which connects the closest houses to the battery.

### Hillclimber
---
- This algorithm needs an initial valid solution.
- Calculate total length of cables.
- Get two random connections (cable from house to battery) from this solution.
- Calculate the total length of cables with the new configuration.
- Check which one is better and keep the better one (shorter cable length is better).
- Repeat n times.

### Simulated annealing
---
- This algorithm needs an initial valid solution.
- Calculate total length of cables.
- Get two random connections (cable from house to battery) from this solution.
- Calculate the total length of cables with the new configuration.
- Assign acceptance chance to new configuration.
- Accept new configuration based on acceptance change.

### K-means
- This algorithm will assign points to clusters via an iterative procedure based on the distance of the point to these clusters.
- The position of the cluster is moved, based on the average of the points assigned to the cluster.
- The points are then assigned again to the cluster based on the manhattan distance.
- This process will repeat, until there is no other change.
- In short there are two steps:
  - Cluster assignment
  - Move step of the centroids
