import pandas as pd
import numpy as np

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    male = df['sex'] == 'Male'# this give us with the index's of the all males entries and then we can use that index's to derive a sub-dataframe
    df1 = df[male]
    
    average_age_men = round(df1['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    #bach_count = df.education.value_counts()['Bachelors']
    bach_df = df.loc[df['education'] =='Bachelors']
    bach_count= bach_df.size
    allcount =df.size
    
    #percentage_bachelors 
    percentage_bachelors = round((bach_count/allcount)*100,1) #percentage

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    
    #rich_high_edu = df[(df.salary == '>50K') & (df.education.isin(['Bachelors', 'Masters', 'Doctorate']))].count()

    #rich_50 = (df['salary'] == '>50K')
    #rich_df = df[rich_50]
    higher_education = df[(df['education'] =='Bachelors') |(df['education'] =='Masters') | (df['education'] =='Doctorate')]
    
    rich_50_ind = (higher_education['salary'] == '>50K')
    rich_50 = higher_education[rich_50_ind]
    
    lower_education = df.loc[~((df['education'] == 'Bachelors') | (df['education'] == 'Masters')|(df['education'] == 'Doctorate')),:]

    rich_50_ind = (lower_education['salary'] == '>50K')
    low_edu_rich= lower_education[rich_50_ind]



    # percentage with salary >50K
    higher_education_rich = round(((rich_50.size)/(higher_education.size))*100, 1)
    
    lower_education_rich = round(((low_edu_rich.size)/(lower_education.size))*100,1) #None

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min() #None

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    #min_work_hr_index = df['hours-per-week'] = '1'
    min_work_hr_index = (df['hours-per-week'] == 1)
    num_min_workers = df[min_work_hr_index]
    #num_min_workers = None
    num_min_workers_rich_ind = (num_min_workers['salary'] == '>50K')
    num_min_workers_rich = num_min_workers[num_min_workers_rich_ind]

    rich_percentage = ((num_min_workers_rich.size)/(num_min_workers.size))*100

    # What country has the highest percentage of people that earn >50K?
    us = df['native-country'] =='United-States'
    us_count = us.sum()
    us_count # usa country count

    usa=df[us]
    usaRich = usa['salary'] == '>50K'
    usaRich_count =usaRich.sum()
    usaRich_count

    USpercent = ((usaRich_count)/(us_count))*100
    USpercent # usa percentage


    Philippines = df['native-country'] =='Philippines'
    Philippines_count = Philippines.sum()
    Philippines_count # Philippines country count

    phil=df[Philippines]
    philRich = phil['salary'] == '>50K'
    philRich_count =philRich.sum()
    philRich_count

    philpercent = ((philRich_count)/(Philippines_count))*100
    philpercent # philippines percentage


    Germany = df['native-country'] =='Germany'
    Germany_count = Germany.sum()
    Germany_count # Germany country count

    ger=df[Germany]
    gerRich = ger['salary'] == '>50K'
    gerRich_count =gerRich.sum()
    gerRich_count

    gerpercent = ((gerRich_count)/(Germany_count))*100
    gerpercent # Germany percentage


    Canada = df['native-country'] =='Canada'
    Canada_count = Canada.sum()
    Canada_count # Canada country count

    can=df[Canada]
    canRich = can['salary'] == '>50K'
    canRich_count =canRich.sum()
    canRich_count

    canpercent = ((canRich_count)/(Canada_count))*100
    canpercent # Canada percentage


    PRico = df['native-country'] =='Puerto-Rico'
    PRico_count = PRico.sum()
    PRico_count # Puerto-Rico country count

    pric=df[PRico]
    pricRich = pric['salary'] == '>50K'
    pricRich_count =pricRich.sum()
    pricRich_count

    pricpercent = ((pricRich_count)/(PRico_count))*100
    pricpercent # Puerto-Rico percentage



    ElSalvador = df['native-country'] =='El-Salvador'
    ElSalvador_count = ElSalvador.sum()
    ElSalvador_count # El-Salvador country count

    elsa=df[ElSalvador]
    elsaRich = elsa['salary'] == '>50K'
    elsaRich_count =elsaRich.sum()
    elsaRich_count

    elsapercent = ((elsaRich_count)/(ElSalvador_count))*100
    elsapercent # El-Salvador percentage



    India = df['native-country'] =='India'
    India_count = India.sum()
    India_count # India country count

    ind=df[India]
    indRich = ind['salary'] == '>50K'
    indRich_count =indRich.sum()
    indRich_count

    indpercent = ((indRich_count)/(India_count))*100
    indpercent # India percentage



    England = df['native-country'] =='England'
    England_count = England.sum()
    England_count # England country count

    eng=df[England]
    engRich = eng['salary'] == '>50K'
    engRich_count =engRich.sum()
    engRich_count

    engpercent = ((engRich_count)/(England_count))*100
    engpercent # England percentage


    Jamaica = df['native-country'] =='Jamaica'
    Jamaica_count = Jamaica.sum()
    Jamaica_count # Jamaica country count

    jam=df[Jamaica]
    jamRich = jam['salary'] == '>50K'
    jamRich_count =jamRich.sum()
    jamRich_count

    jampercent = ((jamRich_count)/(Jamaica_count))*100
    jampercent # Jamaica percentage


    South = df['native-country'] =='South'
    South_count = South.sum()
    South_count # South country count

    sou=df[South]
    souRich = sou['salary'] == '>50K'
    souRich_count =souRich.sum()
    souRich_count

    soupercent = ((souRich_count)/(South_count))*100
    soupercent # South percentage


    China = df['native-country'] =='China'
    China_count = China.sum()
    China_count # China country count

    chin=df[China]
    chinRich = chin['salary'] == '>50K'
    chinRich_count =chinRich.sum()
    chinRich_count

    chinpercent = ((chinRich_count)/(China_count))*100
    chinpercent # China percentage


    Italy = df['native-country'] =='Italy'
    Italy_count = Italy.sum()
    Italy_count # Italy country count

    ita=df[Italy]
    itaRich = ita['salary'] == '>50K'
    itaRich_count =itaRich.sum()
    itaRich_count

    itapercent = ((itaRich_count)/(Italy_count))*100
    itapercent # Italy percentage


    DominicanRepublic = df['native-country'] =='Dominican-Republic'
    DominicanRepublic_count = DominicanRepublic.sum()
    DominicanRepublic_count # Dominican-Republic country count

    dorep=df[DominicanRepublic]
    dorepRich = dorep['salary'] == '>50K'
    dorepRich_count =dorepRich.sum()
    dorepRich_count

    doreppercent = ((dorepRich_count)/(DominicanRepublic_count))*100
    doreppercent # DominicanRepublic percentage


    Vietnam = df['native-country'] =='Vietnam'
    Vietnam_count = Vietnam.sum()
    Vietnam_count # Vietnam country count

    viet=df[Vietnam]
    vietRich = viet['salary'] == '>50K'
    vietRich_count =vietRich.sum()
    vietRich_count

    vietpercent = ((vietRich_count)/(Vietnam_count))*100
    vietpercent # Vietnam percentage


    Guatemala = df['native-country'] =='Guatemala'
    Guatemala_count = Guatemala.sum()
    Guatemala_count # Guatemala country count

    guat=df[Guatemala]
    guatRich = guat['salary'] == '>50K'
    guatRich_count =guatRich.sum()
    guatRich_count

    guatpercent = ((guatRich_count)/(Guatemala_count))*100
    guatpercent # Guatemala percentage


    Japan = df['native-country'] =='Japan'
    Japan_count = Japan.sum()
    Japan_count # Japan country count

    jap=df[Japan]
    japRich = jap['salary'] == '>50K'
    japRich_count =japRich.sum()
    japRich_count

    jappercent = ((japRich_count)/(Japan_count))*100
    jappercent # Japan percentage


    Poland = df['native-country'] =='Poland'
    Poland_count = Poland.sum()
    Poland_count # Poland country count

    pol=df[Poland]
    polRich = pol['salary'] == '>50K'
    polRich_count =polRich.sum()
    polRich_count

    polpercent = ((polRich_count)/(Poland_count))*100
    polpercent # Poland percentage

    Columbia = df['native-country'] =='Columbia'
    Columbia_count = Columbia.sum()
    Columbia_count # Columbia country count

    col=df[Columbia]
    colRich = col['salary'] == '>50K'
    colRich_count =colRich.sum()
    colRich_count

    colpercent = ((colRich_count)/(Columbia_count))*100
    colpercent # Columbia percentage



    Taiwan = df['native-country'] =='Taiwan'
    Taiwan_count = Taiwan.sum()
    Taiwan_count # Taiwan country count

    tai=df[Taiwan]
    taiRich = tai['salary'] == '>50K'
    taiRich_count =taiRich.sum()
    taiRich_count

    taipercent = ((taiRich_count)/(Taiwan_count))*100
    taipercent # Taiwan percentage


    Haiti = df['native-country'] =='Haiti'
    Haiti_count = Haiti.sum()
    Haiti_count # Haiti country count

    hai=df[Haiti]
    haiRich = hai['salary'] == '>50K'
    haiRich_count =haiRich.sum()
    haiRich_count

    haipercent = ((haiRich_count)/(Haiti_count))*100
    haipercent # Poland percentage  


    Laos = df['native-country'] =='Laos'
    Laos_count = Laos.sum()
    Laos_count # Laos country count

    lao=df[Laos]
    laoRich = lao['salary'] == '>50K'
    laoRich_count =laoRich.sum()
    laoRich_count

    laopercent = ((laoRich_count)/(Laos_count))*100
    laopercent # Laos percentage


    France = df['native-country'] =='France'
    France_count = France.sum()
    France_count # France country count

    fra=df[France]
    fraRich = fra['salary'] == '>50K'
    fraRich_count =fraRich.sum()
    fraRich_count

    frapercent = ((fraRich_count)/(France_count))*100
    frapercent # France percentage


    Ecuador = df['native-country'] =='Ecuador'
    Ecuador_count = Ecuador.sum()
    Ecuador_count # Ecuador country count

    ecu=df[Ecuador]
    ecuRich = ecu['salary'] == '>50K'
    ecuRich_count =ecuRich.sum()
    ecuRich_count

    ecupercent = ((ecuRich_count)/(Ecuador_count))*100
    ecupercent # Ecuador percentage


    Ireland = df['native-country'] =='Ireland'
    Ireland_count = Ireland.sum()
    Ireland_count # Ireland country count

    ire=df[Ireland]
    ireRich = ire['salary'] == '>50K'
    ireRich_count =ireRich.sum()
    ireRich_count

    irepercent = ((ireRich_count)/(Ireland_count))*100
    irepercent # Ireland percentage


    Hong = df['native-country'] =='Hong'
    Hong_count = Hong.sum()
    Hong_count # Hong country count

    hon=df[Hong]
    honRich = hon['salary'] == '>50K'
    honRich_count =honRich.sum()
    honRich_count

    honpercent = ((honRich_count)/(Hong_count))*100
    honpercent # Hong percentage

    TTobago = df['native-country'] =='Trinadad&Tobago'
    TTobago_count = TTobago.sum()
    TTobago_count # Trinadad&Tobago country count

    tto=df[TTobago]
    ttoRich = tto['salary'] == '>50K'
    ttoRich_count =ttoRich.sum()
    ttoRich_count

    ttopercent = ((ttoRich_count)/(TTobago_count))*100
    ttopercent # Trinadad&Tobago percentage


    Cambodia = df['native-country'] =='Cambodia'
    Cambodia_count = Cambodia.sum()
    Cambodia_count # Cambodia country count

    cam=df[Cambodia]
    camRich = cam['salary'] == '>50K'
    camRich_count =camRich.sum()
    camRich_count

    campercent = ((camRich_count)/(Cambodia_count))*100
    campercent # Cambodia percentage

    Greece = df['native-country'] =='Greece'
    Greece_count = Greece.sum()
    Greece_count # Greece country count

    gre=df[Greece]
    greRich = gre['salary'] == '>50K'
    greRich_count =greRich.sum()
    greRich_count

    grepercent = ((greRich_count)/(Greece_count))*100
    grepercent # Greece percentage


    Iran = df['native-country'] =='Iran'
    Iran_count = Iran.sum()
    Iran_count # Iran country count

    ira=df[Iran]
    iraRich = ira['salary'] == '>50K'
    iraRich_count =iraRich.sum()
    iraRich_count

    irapercent = ((iraRich_count)/(Iran_count))*100
    irapercent # Iran percentage


    Portugal = df['native-country'] =='Portugal'
    Portugal_count = Portugal.sum()
    Portugal_count # Portugal country count

    por=df[Portugal]
    porRich = por['salary'] == '>50K'
    porRich_count =porRich.sum()
    porRich_count

    porpercent = ((porRich_count)/(Portugal_count))*100
    porpercent # Portugal percentage


    Nicaragua = df['native-country'] =='Nicaragua'
    Nicaragua_count = Nicaragua.sum()
    Nicaragua_count # Nicaragua country count

    nic=df[Nicaragua]
    nicRich = nic['salary'] == '>50K'
    nicRich_count =nicRich.sum()
    nicRich_count

    nicpercent = ((nicRich_count)/(Nicaragua_count))*100
    nicpercent # Nicaragua percentage


    Peru = df['native-country'] =='Peru'
    Peru_count = Peru.sum()
    Peru_count # Peru country count

    per=df[Peru]
    perRich = per['salary'] == '>50K'
    perRich_count =perRich.sum()
    perRich_count

    perpercent = ((perRich_count)/(Peru_count))*100
    perpercent # Peru percentage


    Thailand = df['native-country'] =='Thailand'
    Thailand_count = Thailand.sum()
    Thailand_count # Thailand country count

    tha=df[Thailand]
    thaRich = tha['salary'] == '>50K'
    thaRich_count =thaRich.sum()
    thaRich_count

    thapercent = ((thaRich_count)/(Thailand_count))*100
    thapercent # Thailand percentage


    Yugoslavia = df['native-country'] =='Yugoslavia'
    Yugoslavia_count = Yugoslavia.sum()
    Yugoslavia_count # Yugoslavia country count

    yug=df[Yugoslavia]
    yugRich = yug['salary'] == '>50K'
    yugRich_count =yugRich.sum()
    yugRich_count

    yugpercent = ((yugRich_count)/(Yugoslavia_count))*100
    yugpercent # Yugoslavia percentage


    outus = df['native-country'] =='Outlying-US(Guam-USVI-etc)'
    outus_count = outus.sum()
    outus_count # Outlying-US(Guam-USVI-etc) country count

    out=df[outus]
    outRich = out['salary'] == '>50K'
    outRich_count =outRich.sum()
    outRich_count

    outpercent = ((outRich_count)/(outus_count))*100
    outpercent # outus percentage


    Honduras = df['native-country'] =='Honduras'
    Honduras_count = Honduras.sum()
    Honduras_count # Honduras country count

    hon=df[Honduras]
    honRich = hon['salary'] == '>50K'
    honRich_count =honRich.sum()
    honRich_count

    honpercent = ((honRich_count)/(Honduras_count))*100
    honpercent # Honduras percentage


    Hungary = df['native-country'] =='Hungary'
    Hungary_count = Hungary.sum()
    Hungary_count # Hungary country count

    hun=df[Hungary]
    hunRich = hun['salary'] == '>50K'
    hunRich_count =hunRich.sum()
    hunRich_count

    hunpercent = ((hunRich_count)/(Hungary_count))*100
    hunpercent # Hungary percentage


    Scotland = df['native-country'] =='Scotland'
    Scotland_count = Scotland.sum()
    Scotland_count # Scotland country count

    sco=df[Scotland]
    scoRich = sco['salary'] == '>50K'
    scoRich_count =scoRich.sum()
    scoRich_count

    scopercent = ((scoRich_count)/(Scotland_count))*100
    scopercent # Scotland percentage


    Holand = df['native-country'] =='Holand-Netherlands'
    Holand_count = Holand.sum()
    Holand_count # Holand-Netherlands country count

    hol=df[Holand]
    holRich = hol['salary'] == '>50K'
    holRich_count =holRich.sum()
    holRich_count

    holpercent = ((holRich_count)/(Holand_count))*100
    holpercent # Holand percentage


    cuba = df['native-country'] =='Cuba'
    cuba_count = cuba.sum()
    cuba_count # cuba country count

    cub=df[cuba]
    cubRich = cub['salary'] == '>50K'
    cubRich_count =cubRich.sum()
    cubRich_count

    cubpercent = ((cubRich_count)/(cuba_count))*100
    cubpercent # cuba percentage


    Mexico = df['native-country'] =='Mexico'
    Mexico_count = Mexico.sum()
    Mexico_count # Mexico country count

    mex=df[Mexico]
    mexRich = mex['salary'] == '>50K'
    mexRich_count =mexRich.sum()
    mexRich_count

    mexpercent = ((mexRich_count)/(Mexico_count))*100
    mexpercent # Mexico percentage


    percenlist = pd.Series([cubpercent,holpercent,scopercent,hunpercent,honpercent,outpercent,yugpercent,thapercent,perpercent,nicpercent,porpercent,irapercent,grepercent,campercent,ttopercent,honpercent,irepercent,ecupercent,frapercent,laopercent,haipercent,taipercent,colpercent,polpercent,jappercent,guatpercent,vietpercent,doreppercent,itapercent,chinpercent,soupercent,jampercent,engpercent,indpercent,elsapercent,pricpercent,canpercent,gerpercent,philpercent,mexpercent,USpercent])

    #index
    index_ = ['cuba','Holand-Netherlands','Scotland','Hungary','Honduras','Outlying-US(Guam-USVI-etc)','Yugoslavia','Thailand','Peru','Nicaragua','Portugal','Iran','Greece','Cambodia','Trinadad&Tobago','Hong','Ireland','Ecuador','France','Laos','Haiti','Taiwan','Columbia','Poland','Japan','Guatemala','Vietnam','Dominican-Republic','Italy','China','South','Jamaica','England','India','El-Salvador','Puerto-Rico','Canada','Germany','Philippines','Mexico','United-States']
    percenlist.index = index_
    #percenlist.idxmax()
    
    #--------------------------------------------------------------
    
    highest_earning_country = percenlist.idxmax()# None
    highest_earning_country_percentage = round(percenlist.max(), 1) #None

    # Identify the most popular occupation for those who earn >50K in India.
    indian = df['native-country'] == 'India'
    india_df=df[indian]
    india_rich_indx = india_df['salary'] == '>50K'
    india_rich=india_df[india_rich_indx]
    india_rich['occupation'].value_counts()

    prof_count = india_rich.occupation.value_counts()['Prof-specialty']
    exec_count = india_rich.occupation.value_counts()['Exec-managerial']
    tech_count = india_rich.occupation.value_counts()['Tech-support']
    other_count = india_rich.occupation.value_counts()['Other-service']
    Sales_count = india_rich.occupation.value_counts()['Sales']
    adm_count = india_rich.occupation.value_counts()['Adm-clerical']
    tran_count = india_rich.occupation.value_counts()['Transport-moving']

    ocup_count = pd.Series([prof_count,exec_count,tech_count,other_count,Sales_count,adm_count,tran_count])
    index_ =['Prof-specialty','Exec-managerial','Tech-support','Other-service','Sales','Adm-clerical','Transport-moving']
    ocup_count.index = index_
    ocup_count.idxmax()

    top_IN_occupation = ocup_count.idxmax()#None

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
