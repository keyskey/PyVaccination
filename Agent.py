import networkx as nx

class Agent:

    def __init__(self):
        """
        state = ['S', 'IM', 'I', 'R'] (S: Susceptible, IM: Immuned, I: Infectious, R: Recovered)
        strategy = ['V', 'NV']        (V: Vaccinator, NV: Non-vaccinator)
        """
        self.state = 'S'
        self.next_state = 'S'
        self.strategy = 'V'
        self.next_strategy = 'NV'
        self.point = 0
        self.neighbors_id = None

def generate_agents(num_agent, average_degree):
    network = nx.barabasi_albert_graph(num_agent, average_degree//2)
    agents = [Agent() for agent_id in range(num_agent)]
    
    for agent_id, agent in enumerate(agents):
        agent.neighbors_id = list(network[agent_id])

    return agents
