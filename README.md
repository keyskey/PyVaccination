# PyVaccination
Multi-agent simulation code for modeling SIR dynamics and vaccination dilemma

Model setting:
1. Agents are connected with network. You can change it with any other network provided by NetworkX or even you can use your own defined network.
2. Each season has a desease spreading term based on the (inperfect immunity) SIR model but this SIR epidemic days finish when there is no infectious people existing.
3. At the beginning of each desease spreading season, agents can choose whether they commit vaccination or not, based on game theory.
4. Basically vaccinators can avoid infection, but some of them might be infected. This probability is expressed with vaccination effectiveness.

How to run: 
In your terminal, just type
```
$ python main.py
```
after the calculation, you'll get output csv file named "episodex.csv".
Then, visualize the result with the attached jupyter notebook.
You can estimate the Final Epidemic Size (FES), Vaccination Coverage(VC), and Social Average Payoff (SAP) like following;
![episode0](https://user-images.githubusercontent.com/39644776/52142882-576d1b80-269d-11e9-9ffb-184737d37999.png)
