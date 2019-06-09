import numpy as np
import pandas as pd
import random as rnd
import society
import decision
import epidemics

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
    agents = society.generate_agents(num_agent, average_degree)
    result = pd.DataFrame({'Cr': [],
                           'Effectiveness': [],
                           'FES': [],
                           'VC': [],
                           'SAP': []
                          })

    rnd.seed()
    initial_vaccinators_id = decision.choose_initial_vaccinators(num_agent)

    for Cr in params_range:
        for effectiveness in params_range:
            decision.initialize_strategy(agents, initial_vaccinators_id)
            initial_fv = society.count_strategy_fraction(agents)
            fv_hist = [initial_fv]
            fes_hist = []
            sap_hist = []

            for season in range(1, max_season+1):
                print(f'Cr: {Cr:.1f}, Effectiveness: {effectiveness:.1f}, Season: {season} starts...')
                epidemics.initialize_state(agents, Cr, effectiveness)
                fs, fim, fi, fr = epidemics.disease_spreading(agents, beta, gamma)
                decision.PW_Fermi(agents)

                # Store FES, Fv, SAP to history
                fv = society.count_strategy_fraction(agents)
                num_nv = society.count_num_nv(agents)
                sap = society.count_sap(agents)

                fes_hist.append(fr)
                fv_hist.append(fv)
                sap_hist.append(sap)

                if num_nv <= num_initial_infected_agents:
                    fes_eq = fr
                    fv_eq = fv
                    sap_eq = sap

                    break

                elif (season >= 150 and np.mean(fv_hist[season-100:season-1]) - fv <= 0.001) or season == max_season:
                    fes_eq = np.mean(fes_hist[season-100:season-1])
                    fv_eq = np.mean(fv_hist[season-99:season])
                    sap_eq = np.mean(sap_hist[season-100:season-1])

                    break

            new_result = pd.DataFrame([[format(Cr, '.1f'), format(effectiveness, '.1f'), fes_eq, fv_eq, sap_eq]], columns = ['Cr', 'Effectiveness', 'FES', 'VC', 'SAP'])
            result = result.append(new_result)
            print(f'Cr: {Cr:.1f}, Effectiveness: {effectiveness:.1f}, Season finished with FES: {fes_eq:.2f}, VC: {fv_eq:.2f}, SAP: {sap_eq:.2f}')

    result.to_csv(f'episode{episode}.csv')

def main(num_episode):
    for episode in range(num_episode):
        one_episode(episode)

if __name__=='__main__':
    num_episode = 1
    main(num_episode)
