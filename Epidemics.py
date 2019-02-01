import random as rnd

def initialize_state(agents, Cr, effectiveness, num_initial_infected_agents=5):
    """
    Randomely select initially infected agents from non-vaccinators and
    determine the agents who get perfect immunity from vaccinators
    """

    non_vaccinators_id = [agent_id for agent_id, agent in enumerate(agents) if agent.strategy == 'NV']
    initial_infected_agent_id  = rnd.sample(non_vaccinators_id, k = num_initial_infected_agents)
    for agent_id, agent in enumerate(agents):
        if agent_id in initial_infected_agent_id:
            agent.state = 'I'
            agent.point = -1            

        elif agent.strategy == 'V':
            agent.point = -Cr
            if rnd.random() <= effectiveness:
                agent.state = 'IM'
            else:
                agent.state = 'S'

        else:
            agent.state = 'S'
            agent.point = 0

def disease_spreading(agents, beta, gamma):
    """Calculate SIR dynamics until I agents disappear"""

    for day in range(1, 100000):
        # Only S or I state agents change their state, IM or R don't change their state!
        state_changeable_agents = [agent for agent in agents if agent.state in ['S', 'I']]

        for agent in state_changeable_agents:
            if agent.state == 'S':
                num_infected_neighbors = len([agents[agent_id] for agent_id in agent.neighbors_id if agents[agent_id].state == 'I'])
                if rnd.random() <= beta*num_infected_neighbors:
                    agent.next_state = 'I'
                    agent.point -= 1

                else:
                    agent.next_state = 'S'        

            elif agent.state == 'I':
                if rnd.random() <= gamma:
                    agent.next_state = 'R'

                else:
                    agent.next_state = 'I'

        # Update state
        for agent in state_changeable_agents:
            agent.state = agent.next_state
    
        fs, fim, fi, fr = count_state_fraction(agents)
        num_i = count_num_i(state_changeable_agents)
        print(f'Day: {day}, Fs: {fs:.2f}, Fim: {fim:.2f}, Fi: {fi:.2f}, Fr: {fr:.2f}')

        if num_i == 0:
            print('Disease spreading finished!')
            break
        
    return fs, fim, fi, fr

def count_state_fraction(agents):
    """Count the fraction of S/IM/I/R state agents"""

    fs  = len([agent for agent in agents if agent.state =='S'])/len(agents)
    fim = len([agent for agent in agents if agent.state =='IM'])/len(agents)
    fi  = len([agent for agent in agents if agent.state =='I'])/len(agents)
    fr  = 1 - fs - fim - fi 

    return fs, fim, fi, fr

def count_num_i(agents):
    """Count the number of infected agents"""

    num_i = len([agent for agent in agents if agent.state == 'I'])

    return num_i


