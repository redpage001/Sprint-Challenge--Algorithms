#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)O(n) The function runs "n" amount of actions which increases the runtime linearly with respect to "n".


b)0(n*2) The function runs "n" amount of actions twice because of the loop nested inside another loop.


c)0(n) The function runs "n" amount of actions, one for each recursive call until n = 0

## Exercise II

We would have to use a binary search of the floors, checking the pidpoint of the list of floors and checking to see if the egg breaks. Then if the egg breaks on the midpoint, we set the new top floor one floor below the middle floor and set the middlepoint again and check to see if the egg breaks. We run the test again until the egg doesn't break. If the egg does not break on the midpoint then we set the new bottom to be one floor above the middle and we set up the new middlepoint where we check if the egg breaks. This continues until there are no more floors to check. If the egg breaks on the last check then the last floor is "f" and if the egg doesn't break then the floor above the last floor will be "f". We are halving the number of floors each time so the function only log(n) actions so the complexity is O(log n).
