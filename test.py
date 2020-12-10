import streamlit as st
import pandas as pd
import pickle

st.write("""
# Project Web Application
**data science** project!
""")

st.sidebar.header('User Input')
st.sidebar.subheader('Please enter your data:')

def get_input():
    # Display widgets and store their values in variables
    v_AcademicYear = st.sidebar.radio('AcademicYear', ['2562','2563'])
    v_Sex = st.sidebar.radio('Sex', ['Male','Female'])
    v_FacultyID = st.sidebar.selectbox('Faculty', ['School of Liberal Arts',
                                                'School of Science',
                                                'School of Management',
                                                'School of Information Technology',
                                                'School of Agro-industry',
                                                'School of Law',
                                                'School of Cosmetic Science',
                                                'School of Health Science',
                                                'School of Nursing',
                                                'School of Medicine',
                                                'School of Dentistry',
                                                'School of Social Innovation',
                                                'School of Sinology',
                                                'School of Integrative Medicine'])
    v_DepartmentCode = st.sidebar.selectbox('Department', ['Thai Language and Culture for Foreigners',
                                                'English',
                                                'Applied Chemistry',
                                                'Biotechnology',
                                                'Materials Engineering',
                                                'Accounting',
                                                'Economics',
                                                'Business Administration',
                                                'Tourism Management',
                                                'Hospitality Industry Management',
                                                'Logistics and Supply Chain Management',
                                                'Aviation Business Management',
                                                'Digital Technology for Business Innovation',
                                                'Information Technology'
                                                'Computer Science and Innovation',
                                                'Software Engineering',
                                                'Multimedia Technology and Animation',
                                                'Food Science and Technology',
                                                'Posthavest Technology and Logistics',
                                                'Computer Engineering',
                                                'Laws',
                                                'Cosmetic Science',
                                                'Beauty Technology',
                                                'Public Health',
                                                'Sports and Health Science',
                                                'Environmental Health',
                                                'Occupational Health and Safety'
                                                'Nursing Science',
                                                'Medicine',
                                                'Dentistry',
                                                'International Development',
                                                'Chinese Study',
                                                'Business Chinese',
                                                'Teaching Chinese Language (4 Year)',
                                                'Teaching Chinese Language (5 Year)',
                                                'Chinese Language and Culture',
                                                'Applied Thai Traditional Medicine',
                                                'Physical Therapy',
                                                'Traditional Chinese Medicine'])
    v_MajorName = st.sidebar.selectbox('Major Name', ['None',
                                                'English',
                                                'Aviation Services',
                                                'Aviation Operations',
                                                'International Aviation Logistics Business'])
    v_EntryTypeID = st.sidebar.selectbox('Entry Type', ['QUOTA 17 NORTHERN PROVINCES',
                                                'QUOTA BY SCHOOL',
                                                'QUOTA BY COMMUNITY HOSPITAL',
                                                'DIRECT ADMISSION',
                                                'INTERNATIONAL SCHOOL',
                                                'DIRECT ADMISSION BY SCHOOL',
                                                'ADMISSIONS',
                                                'FOREIGNER',
                                                'GOOD BEHAVE STUDENTS',
                                                'SCHOLARSHIP FROM SOUTHERN BORDER',
                                                'SPECIAL TALENT',
                                                'SPECIAL FOR GOOD STUDENT',
                                                'DIRECT ADMISSION UNDER CONDITION GPAX 2.00 FIRST SEMESTER',
                                                'DIRECT ADMISSION UNDER CONDITION GPAX 2.00 FIRST SEMESTER (FOREIGN)',
                                                'DISABLE STUDENT',
                                                'CHIANG RAI DEVELOPMENT SCHOLARSHIP',
                                                'RE-ID FIRST SEMESTER GPAX 2.00',
                                                'EP-MEP PROGRAM',
                                                'QUOTA FOR SOUTHERN BORDER'])
    v_HomeRegion = st.sidebar.selectbox('Home Region', ['International',
                                                'North',
                                                'North East',
                                                'South',
                                                'Central',
                                                'East',
                                                'West',
                                                'No'])
    v_SchoolRegionNameEng = st.sidebar.selectbox('School Region Name', ['Foreign',
                                                'No',
                                                'Northern',
                                                'Northeast',
                                                'Southern',
                                                'Central',
                                                'Eastern',
                                                'Western'])
    v_TCAS = st.sidebar.radio('TCAS', ['1','2','3','4','5'])
    v_EntryGPA = st.sidebar.slider('Entry GPA', 0.00, 4.00)
    v_GPAX = st.sidebar.slider('GPAX', 0.00, 4.00)
    v_GPA_Eng = st.sidebar.slider('GPA of English', 0.00, 4.00)
    v_GPA_Math = st.sidebar.slider('GPA of Mathemetic', 0.00, 4.00)
    v_GPA_Sci = st.sidebar.slider('GPA of Science', 0.00, 4.00)
    v_GPA_Sco = st.sidebar.slider('GPA of Social', 0.00, 4.00)

    if v_FacultyID == 'School of Liberal Arts': 
        v_FacultyID = '10'
    elif v_FacultyID == 'School of Science':
        v_FacultyID = '11'
    elif v_FacultyID == 'School of Management':
        v_FacultyID = '12'
    elif v_FacultyID == 'School of Information Technology':
        v_FacultyID = '13'
    elif v_FacultyID == 'School of Agro-industry':
        v_FacultyID = '14'
    elif v_FacultyID == 'School of Law':
        v_FacultyID = '16'
    elif v_FacultyID == 'School of Cosmetic Science':
        v_FacultyID = '17'
    elif v_FacultyID == 'School of Health Science':
        v_FacultyID = '18'
    elif v_FacultyID == 'School of Nursing':
        v_FacultyID = '19'
    elif v_FacultyID == 'School of Medicine':
        v_FacultyID = '21'
    elif v_FacultyID == 'School of Dentistry':
        v_FacultyID = '22'
    elif v_FacultyID == 'School of Social Innovation':
        v_FacultyID = '23'
    elif v_FacultyID == 'School of Sinology':
        v_FacultyID = '24'
    elif v_FacultyID == 'School of Integrative Medicine':
        v_FacultyID = '25'

    if v_DepartmentCode == 'Thai Language and Culture for Foreigners': 
        v_DepartmentCode = '1005'
    elif v_DepartmentCode == 'English':
        v_DepartmentCode = '1006'
    elif v_DepartmentCode == 'Applied Chemistry':
        v_DepartmentCode = '1102'
    elif v_DepartmentCode == 'Biotechnology':
        v_DepartmentCode = '1105'
    elif v_DepartmentCode == 'Materials Engineering':
        v_DepartmentCode = '1112'
    elif v_DepartmentCode == 'Accounting':
        v_DepartmentCode = '1201'
    elif v_DepartmentCode == 'Economics':
        v_DepartmentCode = '1202'
    elif v_DepartmentCode == 'Business Administration':
        v_DepartmentCode = '1203'
    elif v_DepartmentCode == 'Tourism Management':
        v_DepartmentCode = '1205'
    elif v_DepartmentCode == 'Hospitality Industry Management':
        v_DepartmentCode = '1207'
    elif v_DepartmentCode == 'Logistics and Supply Chain Management':
        v_DepartmentCode = '1209'
    elif v_DepartmentCode == 'Aviation Business Management':
        v_DepartmentCode = '1210'
    elif v_DepartmentCode == 'Digital Technology for Business Innovation':
        v_DepartmentCode = '1301'
    elif v_DepartmentCode == 'Information Technology':
        v_DepartmentCode = '1301'
    elif v_DepartmentCode == 'Computer Science and Innovation':
        v_DepartmentCode = '1302'
    elif v_DepartmentCode == 'Software Engineering':
        v_DepartmentCode = '1305'
    elif v_DepartmentCode == 'Multimedia Technology and Animation':
        v_DepartmentCode = '1306'
    elif v_DepartmentCode == 'Food Science and Technology':
        v_DepartmentCode = '1401'
    elif v_DepartmentCode == 'Posthavest Technology and Logistics':
        v_DepartmentCode = '1407'
    elif v_DepartmentCode == 'Computer Engineering':
        v_DepartmentCode = '1501'
    elif v_DepartmentCode == 'Laws':
        v_DepartmentCode = '1601'
    elif v_DepartmentCode == 'Cosmetic Science':
        v_DepartmentCode = '1701'
    elif v_DepartmentCode == 'Beauty Technology':
        v_DepartmentCode = '1703'
    elif v_DepartmentCode == 'Public Health':
        v_DepartmentCode = '1804'
    elif v_DepartmentCode == 'Sports and Health Science':
        v_DepartmentCode = '1806'
    elif v_DepartmentCode == 'Environmental Health':
        v_DepartmentCode = '1807'
    elif v_DepartmentCode == 'Occupational Health and Safety':
        v_DepartmentCode = '1808'
    elif v_DepartmentCode == 'Nursing Science':
        v_DepartmentCode = '1901'
    elif v_DepartmentCode == 'Medicine':
        v_DepartmentCode = '2101'
    elif v_DepartmentCode == 'Dentistry':
        v_DepartmentCode = '2201'
    elif v_DepartmentCode == 'International Development':
        v_DepartmentCode = '2301'
    elif v_DepartmentCode == 'Chinese Study':
        v_DepartmentCode = '2401'
    elif v_DepartmentCode == 'Teaching Chinese Language (4 Year)':
        v_DepartmentCode = '2403'
    elif v_DepartmentCode == 'Teaching Chinese Language (5 Year)':
        v_DepartmentCode = '2403'
    elif v_DepartmentCode == 'Chinese Language and Culture':
        v_DepartmentCode = '2404'
    elif v_DepartmentCode == 'Applied Thai Traditional Medicine':
        v_DepartmentCode = '2501'
    elif v_DepartmentCode == 'Physical Therapy':
        v_DepartmentCode = '2502'
    elif v_DepartmentCode == 'Traditional Chinese Medicine':
        v_DepartmentCode = '2503'

    if v_EntryTypeID == 'QUOTA 17 NORTHERN PROVINCES': 
        v_EntryTypeID = '10'
    elif v_EntryTypeID == 'QUOTA BY SCHOOL':
        v_EntryTypeID = '11'
    elif v_EntryTypeID == 'QUOTA BY COMMUNITY HOSPITAL':
        v_EntryTypeID = '15'
    elif v_EntryTypeID == 'DIRECT ADMISSION':
        v_EntryTypeID = '20'
    elif v_EntryTypeID == 'INTERNATIONAL SCHOOL':
        v_EntryTypeID = '24'
    elif v_EntryTypeID == 'DIRECT ADMISSION BY SCHOOL':
        v_EntryTypeID = '29'
    elif v_EntryTypeID == 'ADMISSIONS':
        v_EntryTypeID = '30	'
    elif v_EntryTypeID == 'FOREIGNER':
        v_EntryTypeID = '40'
    elif v_EntryTypeID == 'GOOD BEHAVE STUDENTS':
        v_EntryTypeID = '41'
    elif v_EntryTypeID == 'SCHOLARSHIP FROM SOUTHERN BORDER	':
        v_EntryTypeID = '50'
    elif v_EntryTypeID == 'SPECIAL TALENT':
        v_EntryTypeID = '51'
    elif v_EntryTypeID == 'SPECIAL FOR GOOD STUDENT	':
        v_EntryTypeID = '52'
    elif v_EntryTypeID == 'DIRECT ADMISSION UNDER CONDITION GPAX 2.00 FIRST SEMESTER':
        v_EntryTypeID = '58'
    elif v_EntryTypeID == 'DIRECT ADMISSION UNDER CONDITION GPAX 2.00 FIRST SEMESTER (FOREIGN)':
        v_EntryTypeID = '59'
    elif v_EntryTypeID == 'DISABLE STUDENT':
        v_EntryTypeID = '64'
    elif v_EntryTypeID == 'CHIANG RAI DEVELOPMENT SCHOLARSHIP':
        v_EntryTypeID = '66'
    elif v_EntryTypeID == 'RE-ID FIRST SEMESTER GPAX 2.00':
        v_EntryTypeID = '67'
    elif v_EntryTypeID == 'EP-MEP PROGRAM':
        v_EntryTypeID = '68'
    elif v_EntryTypeID == 'QUOTA FOR SOUTHERN BORDER':
        v_EntryTypeID = '69'

    if v_MajorName == 'None': 
        v_MajorName = '0'
    elif v_MajorName == 'English':
        v_MajorName = '1'
    elif v_MajorName == 'Aviation Services':
        v_MajorName = '2'
    elif v_MajorName == 'Aviation Operations':
        v_MajorName = '3'
    elif v_MajorName == 'International Aviation Logistics Business':
        v_MajorName = '4'

    if v_HomeRegion == 'International': 
        v_HomeRegion = '0'
    elif v_HomeRegion == 'North':
        v_HomeRegion = '1'
    elif v_HomeRegion == 'North East':
        v_HomeRegion = '2'
    elif v_HomeRegion == 'South':
        v_HomeRegion = '3'
    elif v_HomeRegion == 'Central':
        v_HomeRegion = '4'
    elif v_HomeRegion == 'East':
        v_HomeRegion = '5'
    elif v_HomeRegion == 'No':
        v_HomeRegion = '6'
    elif v_HomeRegion == 'West':
        v_HomeRegion = '7'

    if v_SchoolRegionNameEng == 'Foreign': 
        v_SchoolRegionNameEng = '0'
    elif v_SchoolRegionNameEng == 'No':
        v_SchoolRegionNameEng = '1'
    elif v_SchoolRegionNameEng == 'Northern':
        v_SchoolRegionNameEng = '2'
    elif v_SchoolRegionNameEng == 'Northeast':
        v_SchoolRegionNameEng = '3'
    elif v_SchoolRegionNameEng == 'Southern':
        v_SchoolRegionNameEng = '4'
    elif v_SchoolRegionNameEng == 'Central':
        v_SchoolRegionNameEng = '5'
    elif v_SchoolRegionNameEng == 'Eastern':
        v_SchoolRegionNameEng = '6'
    elif v_SchoolRegionNameEng == 'Western':
        v_SchoolRegionNameEng = '7'

    # Store user input data in a dictionary
    data = {'Sex': v_Sex,
            'AcademicYear': v_AcademicYear,
            'FacultyID': v_FacultyID,
            'DepartmentCode': v_DepartmentCode,
            'EntryTypeID': v_EntryTypeID,
            'MajorName': v_MajorName,
            'HomeRegion': v_HomeRegion,
            'SchoolRegionNameEng':  v_SchoolRegionNameEng,
            'TCAS': v_TCAS,
            'EntryGPA': v_EntryGPA,
            'GPAX': v_GPAX,
            'GPA_Eng': v_GPA_Eng,
            'GPA_Math': v_GPA_Math,
            'GPA_Sci': v_GPA_Sci,
            'GPA_Sco': v_GPA_Sco,}

    # Create a data frame from the above dictionary
    data_df = pd.DataFrame(data, index=[0])
    return data_df
    # -- Call function to display widgets and get data from user
df = get_input()

st.header('Application of Status MFU Student Prediction:')
st.subheader('User Input:')
st.write(df)

st.subheader('Pre-Processed Input:')
data_sample = pd.read_excel('tcas_new_simple.xlsx')
df = pd.concat([df, data_sample],axis=0)
cat_data = pd.get_dummies(df[['Sex']])
X_new = pd.concat([cat_data, df], axis=1)
X_new = X_new[:1] 
X_new = X_new.drop(columns=['Sex'])
st.write(X_new)

load_sc = pickle.load(open('normal.pkl', 'rb'))
X_new = load_sc.transform(X_new)
st.subheader('Normalized Input:')
st.write(X_new)

load_knn = pickle.load(open('best_knn.pkl', 'rb'))
prediction = load_knn.predict(X_new)
st.subheader('Prediction:')
st.write(prediction)






