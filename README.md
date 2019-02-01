# VaccinationGame
Multi-agent simulation code for modeling SIR dynamics and vaccination behavior

You can estimate the Final Epidemic Size (FES), Vaccination Coverage(VC), and Social Average Payoff (SAP) like following heatmap. To do such analysis, use the ipython notebook attached with the main program.   
![analysis](https://user-images.githubusercontent.com/39644776/44499214-e2dd8c00-a6bd-11e8-9e38-af0bb6aebfbe.png)

Model setting is:
1. Agents are connected with random regular network(default setting). You can change it with any other network provided by NetworkX or even you can use your own defined network.
2. Each season has a desease spreading term up to 365 days based on the (inperfect immunity) SIR model but this SIR epidemic days finish when there is no infectious people existing.
3. At the beginning of each desease spreading season, agents can choose whether they commit vaccination or not, based on game theoretical approach which is described with a payoff matrix. Game class is categolyzed into so called "Chicken game".
4. Basically vaccinators can avoid infection, but unfortunately some of them might be infected. This probability is expressed with vaccination effectiveness.
