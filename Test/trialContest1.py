UnVaccinated = [0,0,0]
Vaccinated = [0,0,0]
VaccinatedNum = 0
UnVaccinatedNum = 0
NumParticipants = input()
for i in range(0,int(NumParticipants)):
    Participant = str(input())
    if (Participant[0] == 'N'):
        UnVaccinatedNum += 1
        if(Participant[1] == 'Y'):
            UnVaccinated[0] +=1
        if(Participant[2] == 'Y'):
            UnVaccinated[1] +=1
        if(Participant[3] == 'Y'):
            UnVaccinated[2] +=1
    else:
        VaccinatedNum += 1
        if(Participant[1] == 'Y'):
            Vaccinated[0] +=1
        if(Participant[2] == 'Y'):
            Vaccinated[1] +=1
        if(Participant[3] == 'Y'):
            Vaccinated[2] +=1
    
if(UnVaccinated[0] == 0):
    Aeff = 0
else:
    AEff = round((1-((Vaccinated[0]/VaccinatedNum)/(UnVaccinated[0]/UnVaccinatedNum)))*100,6)

if(UnVaccinated[0] == 0):
    Beff = 0
else:
    BEff = round((1-((Vaccinated[1]/VaccinatedNum)/(UnVaccinated[1]/UnVaccinatedNum)))*100,6)

if(UnVaccinated[0] == 0):
    Ceff = 0
else:
    CEff = round((1-((Vaccinated[2]/VaccinatedNum)/(UnVaccinated[2]/UnVaccinatedNum)))*100,6)
    
if(AEff <=0 ):
    print("Not Effective")
else:
    print (f"{AEff:.6f}")

if(BEff <=0 ):
    print("Not Effective")
else:
    print (f"{BEff:.6f}")

if(CEff <=0 ):
    print("Not Effective")
else:
    print (f"{CEff:.6f}")

