import numpy as np
import pandas as pd
import random as rnd
import Agent
import Decision
import Epidemics

def one_episode(episode):
    ### Calcualtion setting ###
    num_agent = 10000
    average_degree = 8
    beta = 0.14
    gamma = 0.33
    params_range = np.arange(0, 1.1, 0.1)
    max_season = 1000
    num_initial_infected_agents = 5

    # Prepare agents & DataFrame to store result
    agents = Agent.generate_agents(num_agent, average_degree)
    result = pd.DataFrame({'Cr': [],
                           'Effectiveness': [],
                           'FES': [],
                           'VC': [],
                           'SAP': []
                          })

    rnd.seed()
    initial_vaccinators_id = Decision.choose_initial_vaccinators(num_agent)

    for Cr in params_range: 
        for effectiveness in params_range:
            Decision.initialize_strategy(agents, initial_vaccinators_id)
            initial_fv = Decision.count_strategy_fraction(agents)
            fv_hist = [initial_fv]

            for season in range(1, max_season):
                print(f'Cr: {Cr:.1f}, Effectiveness: {effectiveness:.1f}, Season: {season} starts...')
                Epidemics.initialize_state(agents, Cr, effectiveness)
                fs, fim, fi, fr = Epidemics.disease_spreading(agents, beta, gamma)
                Decision.PW_Fermi(agents)

                fv = Decision.count_strategy_fraction(agents)
                num_nv = Decision.count_num_nv(agents)
                fv_hist.append(fv)
                
                if num_nv <= num_initial_infected_agents:
                    fv_eq = fv
                    break
                
                elif season >= 100 and np.mean(fv_hist[season-100:season-1]) - fv <= 0.001:
                    fv_eq = np.mean(fv_hist[season-99:season])
                    break
    
                elif fv in [0.0, 1.0]:
                    fv_eq = fv
                    break
            
            FES = fr
            VC = fv_eq
            SAP = np.mean([agent.point for agent in agents])
            new_result = pd.DataFrame([[format(Cr, '.1f'), format(effectiveness, '.1f'), FES, VC, SAP]], columns = ['Cr', 'Effectiveness', 'FES', 'VC', 'SAP'])
            result = result.append(new_result)
            print(f'Cr: {Cr:.1f}, Effectiveness: {effectiveness:.1f}, Season finished with FES: {FES:.2f}, VC: {VC:.2f}, SAP: {SAP:.2f}')

    result.to_csv(f'episode{episode}.csv')

def main(num_episode):
    for episode in range(num_episode):
        one_episode(episode)

if __name__=='__main__':
    num_episode = 1
    main(num_episode)

