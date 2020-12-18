# imports
import argparse
import random
import copy
import sys
import numpy as np
import matplotlib.pyplot as plt
import colorama
from colorama import init, Fore, Back, Style


def assign_agents_to_food_test():
    """This function is for testing assign_agents_to_food()"""
    # temp agent list for testing
    tests_passed = "true"
    agent_list_test = []
    agent_list_test.append(Agent("Dove"))
    agent_list_test.append(Agent("Dove"))
    agent_list_test.append(Agent("Hawk"))
    agent_list_test.append(Agent("Hawk"))
    agent_list_test = assign_agents_to_food(agent_list_test, 4)
    # Each of the 4 should have one food location (0-3) each:
    for i in range(4):
        if (agent_list_test[i].food_location in [0, 1, 2, 3]):
            tests_passed = "true"
        else:
            tests_passed = "false"
            break
    print("assign_agents_to_food_test passed =", tests_passed)


def compete_for_food_test():
    """This function is for testing compete_for_food()"""
    # temp agent list for testing
    tests_passed = "true"
    agent_list_test = []
    agent_list_test.append(Agent("Dove"))
    agent_list_test.append(Agent("Dove"))
    agent_list_test.append(Agent("Hawk"))
    agent_list_test.append(Agent("Hawk"))
    agent_list_test[0].assign_food(0)
    agent_list_test[1].assign_food(1)
    agent_list_test[2].assign_food(1)
    agent_list_test[3].assign_food(2)
    compete_for_food(agent_list_test)
    # Agent 1 and 4 should not compete but agent 2 and 3 should
    # Agent 1 = 2, 2 = ~0.5, 3 = ~1.5, 4 = 2
    for i in range(4):
        if (agent_list_test[i].food > 0):
            tests_passed = "true"
        else:
            tests_passed = "false"
            break
    print("compete_for_food_test passed =", tests_passed)


def simulate_strategies_test():
    """This function is for testing simulate_strategies()"""
    tests_passed = "true"
    test_agent1 = Agent("Dove")
    test_agent2 = Agent("Hawk")
    [test_payout1, test_payout2] = simulate_strategies(test_agent1, test_agent2)
    if (test_payout1 < 0.45 or test_payout1 > 0.55):
        tests_passed = "false"
    if (test_payout2 < 1.45 or test_payout2 > 1.55):
        tests_passed = "false"
    print("simulate_strategies_test passed =", tests_passed)


def advance_generation_test():
    """This function is for testing advance_generation()"""
    tests_passed = "true"
    agent_list_test = []
    agent_list_test.append(Agent("test1"))
    agent_list_test.append(Agent("test2"))
    agent_list_test.append(Agent("test3"))
    agent_list_test[0].food = 0
    agent_list_test[1].food = 1
    agent_list_test[2].food = 1
    agent_list_test = advance_generation(agent_list_test)
    if (len(agent_list_test) == 2):
        tests_passed = "true"
    else:
        tests_passed = "false"
    print("advance_generation_test passed =", tests_passed)


def save_statistics_test():
    """This function is for testing save_statistics"""
    tests_passed = "true"
    agent_list_test = []
    global agent1_strategy
    agent1_strategy = "Dove"
    global agent2_strategy
    agent2_strategy = "Hawk"
    agent_list_test.append(Agent("Dove"))
    agent_list_test.append(Agent("Dove"))
    agent_list_test.append(Agent("Dove"))
    agent_list_test.append(Agent("Hawk"))
    agent_list_test.append(Agent("Hawk"))
    [test_population1, test_population2] = save_statistics(agent_list_test)
    if (test_population1 != 3):
        tests_passed = "false"
    if (test_population2 != 2):
        tests_passed = "false"
    print("save_statistics_test passed =", tests_passed)


def test_cases():
    """This function is for calling test functions"""
    assign_agents_to_food_test()
    compete_for_food_test()
    simulate_strategies_test()
    advance_generation_test()
    save_statistics_test()


# define classes
class Agent:
    """ Agents are the main actors in this program.  Each is assigned a strategy
    when initiated.  When running the simulation, each agent is assigned to a
    food location, and then is assigned a food value.
    """
    food = 0
    food_location = None
    strategy = None

    def assign_food(self, food_number):
        self.food_location = food_number

    def __init__(self, strategy):
        self.strategy = strategy

    def first_move(self):
        if (self.strategy == "Dove"):
            return 1
        elif (self.strategy == "Hawk"):
            return 0
        elif (self.strategy == "Random"):
            return random.randint(0, 1)
        elif (self.strategy == "Randomdove"):
            if (random.random() > 0.8):
                return 0
            else:
                return 1
        elif (self.strategy == "Randomhawk"):
            if (random.random() > 0.2):
                return 0
            else:
                return 1
        elif (self.strategy == "Titfortat"):
            return 1
        elif (self.strategy == "Angrytitfortat"):
            return 0
        elif (self.strategy == "Grim"):
            return 1
        elif (self.strategy == "Titfortwotats"):
            return 1

    def get_next_move(self, move_history, opponent_move_history):
        if (self.strategy == "Dove"):
            return 1
        elif (self.strategy == "Hawk"):
            return 0
        elif (self.strategy == "Random"):
            return random.randint(0, 1)
        elif (self.strategy == "Randomdove"):
            if (random.random() > 0.8):
                return 0
            else:
                return 1
        elif (self.strategy == "Randomhawk"):
            if (random.random() > 0.2):
                return 0
            else:
                return 1
        elif (self.strategy == "Titfortat"):
            return (opponent_move_history[len(opponent_move_history) - 1])
        elif (self.strategy == "Angrytitfortat"):
            return (opponent_move_history[len(opponent_move_history) - 1])
        elif (self.strategy == "Grim"):
            has_opponent_defected = 1
            for i in range(len(opponent_move_history)):
                if (opponent_move_history[i] == 0):
                    has_opponent_defected = 0
            return has_opponent_defected
        elif (self.strategy == "Titfortwotats"):
            if (((opponent_move_history[
                len(opponent_move_history) - 1]) == 0) and (
                    len(opponent_move_history) > 1)):
                if ((
                        opponent_move_history[
                            len(opponent_move_history) - 2]) == 0):
                    return 0
            return 1


class Food:
    """ Food is the resource in this simulation.  Food is assigned to agents,
    and then agents die, survive, or reproduce depending on their food value.
    """
    Agent1 = None
    Agent2 = None

    def number_of_agents(self):
        # return the number of agents connected to this food
        if (self.Agent1 == None and self.Agent2 == None):
            return 0
        elif (self.Agent1 == None or self.Agent2 == None):
            return 1
        return 2

    def reset(self):
        # clears all agents connected to this food
        self.Agent1 = None
        self.Agent2 = None

    def add_agent(self, Agent):
        if (self.Agent1 == None):
            # set agent in first slot
            self.Agent1 = Agent
        elif (self.Agent2 == None):
            # set agent in second slot
            self.Agent2 = Agent
        else:
            # returns false if no room for an agent
            return False
            # returns true if food has room for an agent
        return True


# define functions
def print_available_strategies():
    """prints a list of the available strategies"""
    init(convert=True)
    print("Available strategies:")
    print(Fore.GREEN + "Dove " + Style.RESET_ALL + "(always cooperate)")
    print(Fore.GREEN + "Hawk " + Style.RESET_ALL + "(always defect)")
    print(Fore.GREEN + "TitForTat " + Style.RESET_ALL +
        "(cooperate on first round, then imitate opponent's last move)")
    print(Fore.GREEN + "AngryTitForTat " + Style.RESET_ALL +
          "(defect on first move, then imitate opponent's last move)")
    print(Fore.GREEN + "Random " + Style.RESET_ALL +
          "(50% chance to cooperate)")
    print(Fore.GREEN + "RandomDove " + Style.RESET_ALL +
          "(80% chance to cooperate)")
    print(Fore.GREEN + "RandomHawk " + Style.RESET_ALL +
          "(20% chance to cooperate)")
    print(Fore.GREEN + "Grim " + Style.RESET_ALL +
          "(cooperates until opponent defects, then always defects)")
    print(Fore.GREEN + "TitForTwoTats " + Style.RESET_ALL +
          "(if opponent defects twice in a row, then defect."
          "  Otherwise cooperate)")


def get_commandline_input():
    """asking user for input to set up simulation"""
    number_of_agent1 = int(input("Enter number of first population: "))
    number_of_agent2 = int(input("Enter number of second population: "))
    temp = 0
    help = input("Would you like to see the available strategies? (Y/N): ")
    # while loop checking if user wants to see available strategies
    while (temp == 0):
        if help == 'Y' or help == 'y':
            print_available_strategies()
            temp = 1
        elif help == 'N' or help == 'n':
            break
        else:
            help = input(
                Fore.RED + "Invalid Input - Please enter 'Y' or 'N': " +
                Style.RESET_ALL)
    agent1_strategy = input("Enter the strategy for the first agent: ").lower()
    agent2_strategy = input("Enter the strategy for the second agent: ").lower()
    agent1_strategy = agent1_strategy.capitalize()
    agent2_strategy = agent2_strategy.capitalize()

    food_amount = int(input("Enter the number of available food: "))
    # check that the food input is enough to hold the initial agent population
    while (food_amount < (number_of_agent1 + number_of_agent2) / 2):
        print(
            Fore.RED + "Food amount must be greater than half of the total"
                       " number of agents" + Style.RESET_ALL)
        food_amount = int(input("Enter the number of available food: "))
    number_of_generations = int(input("Enter the number of generations: "))
    return [number_of_agent1, number_of_agent2, agent1_strategy,
            agent2_strategy, food_amount, number_of_generations]


def assign_agents_to_food(agentList, food_amount):
    """agents are assigned to a random food
    if a food has 2 agents, no more agents can be attached to that food, so the
     agent will be assigned to a new food
    """
    foodList = []
    # create foodList
    for i in range(food_amount):
        foodList.append(Food())

    i = 0
    while (i < len(agentList)):
        # picking random food
        random_food = random.randint(0, (food_amount - 1))
        # checking if food already has an agent
        if (foodList[random_food].number_of_agents() < 2):
            foodList[random_food].add_agent(agentList[i])
            i = i + 1

    # temporary agent list
    tempList = []

    # loop for assigning agents food
    for i in range(len(foodList)):
        # if food has agent
        if (foodList[i].number_of_agents() == 1):
            foodList[i].Agent1.assign_food(i)
            tempList.append(foodList[i].Agent1)
        elif (foodList[i].number_of_agents() == 2):
            foodList[i].Agent1.assign_food(i)
            tempList.append(foodList[i].Agent1)
            foodList[i].Agent2.assign_food(i)
            tempList.append(foodList[i].Agent2)
    return tempList


def compete_for_food(agentList):
    """iterate through agentList
    #if 1 agent assigned to a food, agent.resource = 2
    #if 2 agents assigned to the same food, they compete
    """
    for i in range(len(agentList)):
        compete = 0
        for j in range(len(agentList)):
            if (agentList[i].food_location == agentList[
                j].food_location and i != j):
                [agentList[i].food, agentList[j].food] = simulate_strategies(
                    agentList[i], agentList[j])
                compete = 1
                break
        if (compete == 0):
            agentList[i].food = 2
    return agentList


def simulate_strategies(agent1, agent2):
    """follow game theory logic over specified number of iterations"""
    # initiate move history lists
    number_of_iterations = 40
    agent1_moves = []
    agent2_moves = []
    # get each agents first move
    agent1_moves.append(agent1.first_move)
    agent2_moves.append(agent2.first_move)
    # agents compete
    for i in range(number_of_iterations - 1):
        agent1_moves.append(agent1.get_next_move(agent1_moves, agent2_moves))
        agent2_moves.append(agent2.get_next_move(agent2_moves, agent1_moves))

    # assign payout
    agent1_payout = 0
    agent2_payout = 0
    # payout matrix
    cooperate_payout = 1 / number_of_iterations
    winner_payout = 1.5 / number_of_iterations
    loser_payout = .5 / number_of_iterations
    defect_payout = 0 / number_of_iterations
    for i in range(number_of_iterations):
        # compare agent1_moves[i] and agent2_moves[i]
        if (agent1_moves[i] == 1 and agent2_moves[i] == 1):
            agent1_payout += cooperate_payout
            agent2_payout += cooperate_payout
        elif (agent1_moves[i] == 1 and agent2_moves[i] == 0):
            agent1_payout += loser_payout
            agent2_payout += winner_payout
        elif (agent1_moves[i] == 0 and agent2_moves[i] == 1):
            agent1_payout += winner_payout
            agent2_payout += loser_payout
        elif (agent1_moves[i] == 0 and agent2_moves[i] == 0):
            agent1_payout += defect_payout
            agent2_payout += defect_payout
    return [agent1_payout, agent2_payout]


def advance_generation(agentList):
    """iterate through agentList checking each agents food
    if food = 1 then no change
    if food < 1 then agent has chance of dying
    if food >1 then agent has chance of reproducing
    reset each agent's food back to 0
    """
    tempList = []
    for i in range(len(agentList)):
        if (agentList[i].food < 1):
            if (random.random() < agentList[i].food):
                # agent survives
                tempList.append(agentList[i])
        elif (agentList[i].food > 1):
            tempList.append(agentList[i])
            if (random.random() < (agentList[i].food - 1)):
                # agent reproduces
                newAgent = copy.deepcopy(agentList[i])
                tempList.append(newAgent)
        elif (agentList[i].food == 1):
            tempList.append(agentList[i])
    # reset agent's food to 0
    for i in range(len(tempList)):
        tempList[i].food = 0

    return tempList


def save_statistics(agentList):
    """iterate through agent list, counting strategy1 and strategy2
    returns 2 numbers, the population of each strategy
    """
    strategy1_population = 0
    strategy2_population = 0
    for i in range(len(agentList)):
        if (agentList[i].strategy == agent1_strategy):
            strategy1_population = strategy1_population + 1
        elif (agentList[i].strategy == agent2_strategy):
            strategy2_population = strategy2_population + 1
    return [strategy1_population, strategy2_population]


def histogram_graph(strategy1_population, strategy2_population):
    """
    takes in 2 population lists of length = number_of_generations
    prints a histograph showing the changes in population numbers over time
    """
    generations = []
    for i in range(number_of_generations + 1):
        generations.append(i + 1)

    # Get values from the group and categories
    generation_amount = []
    for i in range(number_of_generations + 1):
        generation_amount.append(i)

    # The position of the bars on the x-axis
    r = range(len(generation_amount))
    barWidth = 1
    # plot bars
    plt.figure(figsize=(7, 5))
    ax1 = plt.bar(r, strategy1_population, color='#003f5c', edgecolor='white',
                  width=barWidth, label=agent1_strategy)
    ax2 = plt.bar(r, strategy2_population,
                  bottom=np.array(strategy1_population), color='#ff6361',
                  edgecolor='white',
                  width=barWidth, label=agent2_strategy)

    plt.legend()
    # Custom X axis
    plt.xticks(r, generation_amount, fontweight='bold')
    plt.ylabel("Population Size")
    plt.xlabel("Generations")
    for r1, r2 in zip(ax1, ax2):
        h1 = r1.get_height()
        h2 = r2.get_height()
        plt.text(r1.get_x() + r1.get_width() / 2., h1 / 2., "%d" % h1,
                 ha="center", va="center", color="black",
                 fontsize=10, fontweight="bold")
        plt.text(r2.get_x() + r2.get_width() / 2., h1 + h2 / 2., "%d" % h2,
                 ha="center", va="center", color="black",
                 fontsize=10, fontweight="bold")
    plt.savefig(str(number_of_agent1) + agent1_strategy + "VS" + str(
        number_of_agent2) + agent2_strategy + str(
        food_amount) + "Food" + str(number_of_generations) + "Gens")
    plt.show()


def print_agents(agentList):
    """ This function is for testing purposes.  It prints out the agentlist
     and details on each agent
    """
    for i in range(len(agentList)):
        print("Agent List #" + str(i) + " Agent Food: " + str(
            agentList[i].food) + " Agent Strategy: " + agentList[
                  i].strategy + " Food Location: " + str(
            agentList[i].food_location))


# main

# calling test case function (only for testing)
# test_cases()

# get parameters from argparse.  if no parameters then ask user for command
# line input
if (len(sys.argv) > 1):
    strategy_help = "Dove, Hawk, TitForTat, AngryTitForTat, Random," \
                    " RandomDove, RandomHawk, Grim, or TitForTwoTats."
    # initiating argparse
    parser = argparse.ArgumentParser(
        description='Simulate the evolution of aggression of two populations'
                    ' with different strategies.')
    parser.add_argument('number_of_agent1', type=int,
                        help='Size of first population.')
    parser.add_argument('number_of_agent2', type=int,
                        help='Size of second population.')
    parser.add_argument('food_amount', type=int,
                        help='Amount of food present between the two'
                             ' populations.')
    parser.add_argument('agent1_strategy', help=strategy_help)
    parser.add_argument('agent2_strategy', help='Same strategies available as'
                                                ' agent1_strategy')
    parser.add_argument('number_of_generations', type=int,
                        help='Number of generations to be simulated')
    args = parser.parse_args()
    # assigning variables to args
    number_of_agent1 = args.number_of_agent1
    number_of_agent2 = args.number_of_agent1
    food_amount = args.food_amount
    agent1_strategy = args.agent1_strategy
    agent2_strategy = args.agent2_strategy
    number_of_generations = args.number_of_generations
# get info from command line if nothing used argparse
else:
    [number_of_agent1, number_of_agent2, agent1_strategy, agent2_strategy,
     food_amount,
     number_of_generations] = get_commandline_input()

# create agentList
agentList = []

# populate agentList
for i in range(number_of_agent1 + number_of_agent2):
    if (i < number_of_agent1):
        agentList.append(Agent(agent1_strategy))
    else:
        agentList.append(Agent(agent2_strategy))

# create lists to store graphing information
strategy1_population = [0] * (number_of_generations + 1)
strategy2_population = [0] * (number_of_generations + 1)

# main loop
for generation in range(number_of_generations):
    # assign each agent to a random food
    agentList = assign_agents_to_food(agentList, food_amount)

    # agents compete for food
    agentList = compete_for_food(agentList)

    # agents reproduce and die
    agentList = advance_generation(agentList)

    # prepare stats for graphing purposes
    strategy1_population[0] = number_of_agent1
    strategy2_population[0] = number_of_agent2
    [strategy1_population[generation + 1],
     strategy2_population[generation + 1]] = save_statistics(agentList)

# print histogram graph
histogram_graph(strategy1_population, strategy2_population)
