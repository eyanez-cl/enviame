def palabras_iguales(texto):
    largo_texto= len(texto)
    if largo_texto % 2 == 0:
        izq = texto[: largo_texto // 2]
        der = texto [largo_texto // 2:]
        
        
    else:
        izq = texto[: largo_texto // 2]
        der = texto [largo_texto // 2 + 1]
        
    print(izq)
    print('--------------------------------')
    print(der)
        
    return  izq == der [:: -1]

print(palabras_iguales('afoolishconsistencyisthehobgoblinoflittlemindsadoredbylittlestatesmenandphilosophersanddivineswithconsistencyagreatsoulhassimplynothingtodohemayaswellconcernhimselfwithhisshadowonthewallspeakwhatyouthinknowinhardwordsandtomorrowspeakwhattomorrowthinksinhardwordsagainthoughitcontradicteverythingyousaidtodayahsoyoushallbesuretobemisunderstoodisitsobadthentobemisunderstoodpythagoraswasmisunderstoodandsocratesandjesusandlutherandcopernicusandgalileoandnewtonandeverypureandwisespiritthatevertookfleshtobegreatistobemisunderstood'))

        





