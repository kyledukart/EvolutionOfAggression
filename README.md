# EvolutionOfAggression
A Python project to simulate the evolution of aggression.

Created by Kyle Dukart and William Simcox

This project was created using repl.it
https://repl.it/@Shucadoodle/Project2#main.py


<b>Simulation Overview</b>: Simulate a population of N agents in competition over limited resources. Each agent has a game theory strategy.

Iterate over X number of generations:
Each agent goes to a random resource (max of 2 per resource)
If multiple agents arrive at the same resource, the resource is divided between the agents depending on the strategy of each agent
This process is repeated 40 times, as each agent is able to “react” to the other agent’s moves as defined in each agent’s strategy
Agents die or reproduce depending on how many resources they have received.

The program then graphs the populations of the agents, showing which strategy is dominant, or what ratio gives us equilibrium.
