#Princess Finder for MQO
Miden Quest Online (MQO: midenquest.com) is a multiplayer persistent browser based game.
The game features a global quest where a Lost Princess spawns randomly on the 1000x1000 tile map.
Players search the map for clues and are notified when they are within certain distances of the princess's location (100,25,10, and 5)
This script aims to help players by generating a feasible set of tiles that may contain the princess based on their location and
the distance clues they are given. Overlapping sets are combined to further reduce the set of feasible locations.

##How it Works
(coming soon)
###The Map and Distances
###Feasible Sets

##To Do
- [x] confirm distance metric
- [x] confirm min/max distance
- [x] support for maximum distance modifiers
- [ ] support for negative clues
- [ ] suggest random location in set
- [ ] intelligently suggest locations
- [ ] suggestions based on travel distance
- [x] port to javascript
- [x] github.io page
- [ ] visualize feasible sets
- [ ] interactive visualization
- [ ] testing and demonstration script