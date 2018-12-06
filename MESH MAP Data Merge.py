
# coding: utf-8

# # ODA MAP MESH Data Merge
# * Code used to merge ODA MAP academic assessment data with MESH social emotional survey data.  
# * A total of thirteen CSV files were merged.  
# * The final CSV file developed from this code was used to create a data dashboard in excel.

# In[1]:


# Required dependencies

import pandas as pd
import numpy as np
import os
from pandas import Series, DataFrame
from collections import OrderedDict


# In[2]:


# Load CSV files

map_fall_2017_assessment_result = "01 Fall 2017 Assessment Results.csv"
map_winter_2017_assessment_result = "02 Winter 2017 Assessment Results.csv"
map_spring_2018_assessment_result = "03 Spring 2018 Assessment Results.csv"
map_fall_2018_assessment_result = "04 Fall 2018 Assessment Results.csv"
map_ay2017_2018_assessment_result = "05 Year.csv"
mesh_sel_fall_2017_survey = "06 Oxford Day SEL MESH Data Fall 2017 Data.csv"
mesh_cc_fall_2017_survey = "07 Oxford Day CC MESH Data Fall 2017 Data.csv"
mesh_sel_spring_2018_survey = "08 Oxford Day SEL MESH Data Spring 2018 Data.csv"
mesh_cc_spring_2018_survey = "09 Oxford Day CC MESH Data Spring 2018 Data.csv"
mesh_sel_fall_2018_survey = "10 Oxford Day SEL MESH Data Fall 2018 Data.csv"
mesh_cc_fall_2018_survey = "11 Oxford Day CC MESH Data Fall 2018 Data.csv"
student_names_id_list = "12 StudentNames.csv"


# In[3]:


# Read CSV files

map_fall_2017 = pd.read_csv(map_fall_2017_assessment_result)
map_winter_2017 = pd.read_csv(map_winter_2017_assessment_result)
map_spring_2018 = pd.read_csv(map_spring_2018_assessment_result)
map_fall_2018 = pd.read_csv(map_fall_2018_assessment_result)
map_ay_2017_2018 = pd.read_csv(map_ay2017_2018_assessment_result)
mesh_sel_fall_2017 = pd.read_csv(mesh_sel_fall_2017_survey)
mesh_cc_fall_2017 = pd.read_csv(mesh_cc_fall_2017_survey)
mesh_sel_spring_2018 = pd.read_csv(mesh_sel_spring_2018_survey)
mesh_cc_spring_2018 = pd.read_csv(mesh_cc_spring_2018_survey)
mesh_sel_fall_2018 = pd.read_csv(mesh_sel_fall_2018_survey)
mesh_cc_fall_2018 = pd.read_csv(mesh_cc_fall_2018_survey)
student_names_id = pd.read_csv(student_names_id_list)


# In[4]:


# Drop columns from MESH frames

mesh_sel_fall_2017 = mesh_sel_fall_2017.drop(columns=['School School ID','For VALUES columns, the numbers represent the answer values. These are used in calculating means for reports. For example, in a 5 point scale for a positively coded question, Strongly Agree, Agree, Neither Agree Nor Disagree, Disagree, Strongly Agree have values 5, 4, 3, 2, 1 respectively. For a negatively coded question, the values are reversed.','Client Name','Network Name','School Name','Student Panorama ID','Student Student ID'])
mesh_cc_fall_2017 = mesh_cc_fall_2017.drop(columns=['School School ID','For VALUES columns, the numbers represent the answer values. These are used in calculating means for reports. For example, in a 5 point scale for a positively coded question, Strongly Agree, Agree, Neither Agree Nor Disagree, Disagree, Strongly Agree have values 5, 4, 3, 2, 1 respectively. For a negatively coded question, the values are reversed.','Client Name','Network Name','School Name','Student Panorama ID','Student Student ID'])
mesh_sel_spring_2018 = mesh_sel_spring_2018.drop(columns=['School School ID','For VALUES columns, the numbers represent the answer values. These are used in calculating means for reports. For example, in a 5 point scale for a positively coded question, Strongly Agree, Agree, Neither Agree Nor Disagree, Disagree, Strongly Agree have values 5, 4, 3, 2, 1 respectively. For a negatively coded question, the values are reversed.','Client Name','Network Name','School Name','Student Panorama ID','Student Student ID'])
mesh_cc_spring_2018 = mesh_cc_spring_2018.drop(columns=['School School ID','For VALUES columns, the numbers represent the answer values. These are used in calculating means for reports. For example, in a 5 point scale for a positively coded question, Strongly Agree, Agree, Neither Agree Nor Disagree, Disagree, Strongly Agree have values 5, 4, 3, 2, 1 respectively. For a negatively coded question, the values are reversed.','Client Name','Network Name','School Name','Student Panorama ID','Student Student ID'])
mesh_sel_fall_2018 = mesh_sel_fall_2018.drop(columns=['For VALUES columns, the numbers represent the answer values. These are used in calculating means for reports. For example, in a 5 point scale for a positively coded question, Strongly Agree, Agree, Neither Agree Nor Disagree, Disagree, Strongly Agree have values 5, 4, 3, 2, 1 respectively. For a negatively coded question, the values are reversed.','Client Name','Network Name','School Name','Student Panorama ID','Student Student ID'])
mesh_cc_fall_2018 = mesh_cc_fall_2018.drop(columns=['For VALUES columns, the numbers represent the answer values. These are used in calculating means for reports. For example, in a 5 point scale for a positively coded question, Strongly Agree, Agree, Neither Agree Nor Disagree, Disagree, Strongly Agree have values 5, 4, 3, 2, 1 respectively. For a negatively coded question, the values are reversed.','Client Name','Network Name','School Name','Student Panorama ID','Student Student ID'])


# In[5]:


# Add Student Name column to MESH frames
# Combine 'Student First Name' and 'Student Last Name'

mesh_sel_fall_2017['Student Name'] = mesh_sel_fall_2017['Student First Name'] + ' ' + mesh_sel_fall_2017['Student Last Name']
mesh_cc_fall_2017['Student Name'] = mesh_cc_fall_2017['Student First Name'] + ' ' + mesh_cc_fall_2017['Student Last Name']
mesh_sel_spring_2018['Student Name'] = mesh_sel_spring_2018['Student First Name'] + ' ' + mesh_sel_spring_2018['Student Last Name']
mesh_cc_spring_2018['Student Name'] = mesh_cc_spring_2018['Student First Name'] + ' ' + mesh_cc_spring_2018['Student Last Name']
mesh_sel_fall_2018['Student Name'] = mesh_sel_fall_2018['Student First Name'] + ' ' + mesh_sel_fall_2018['Student Last Name']
mesh_cc_fall_2018['Student Name'] = mesh_cc_fall_2018['Student First Name'] + ' ' + mesh_cc_fall_2018['Student Last Name']


# In[6]:


# Index students by StudentID

StudentID = student_names_id.set_index('StudentID')


# In[7]:


# Index students by Student Name

Student_Name = student_names_id.set_index('Student Name')


# In[8]:


# Add student names to Map df
# Merge all Map df with StudentID df

map_fall_2017 = pd.merge(map_fall_2017,StudentID, how="left", on=['StudentID'])
map_winter_2017 = pd.merge(map_winter_2017,StudentID, how="left", on=['StudentID'])
map_spring_2018 = pd.merge(map_spring_2018,StudentID, how="left", on=['StudentID'])
map_fall_2018 = pd.merge(map_fall_2018,StudentID, how="left", on=['StudentID'])


# In[9]:


# Add StudentID to MESH df
# Merge all Mesh df with Student_Name df

mesh_sel_fall_2017 = pd.merge(mesh_sel_fall_2017,Student_Name, how="left", on=['Student Name'])
mesh_cc_fall_2017 = pd.merge(mesh_cc_fall_2017,Student_Name, how="left", on=['Student Name'])
mesh_sel_spring_2018 = pd.merge(mesh_sel_spring_2018,Student_Name, how="left", on=['Student Name'])
mesh_cc_spring_2018 = pd.merge(mesh_cc_spring_2018,Student_Name, how="left", on=['Student Name'])
mesh_sel_fall_2018 = pd.merge(mesh_sel_fall_2018,Student_Name, how="left", on=['Student Name'])
mesh_cc_fall_2018 = pd.merge(mesh_cc_fall_2018,Student_Name, how="left", on=['Student Name'])


# In[10]:


# Create MAP Reading df by year

map_fall_2017_reading = map_fall_2017.drop(map_fall_2017[map_fall_2017.Discipline.isin(["Language","Mathematics","Science"])].index)
map_winter_2017_reading = map_winter_2017.drop(map_winter_2017[map_winter_2017.Discipline.isin(["Language","Mathematics","Science"])].index)
map_spring_2018_reading = map_spring_2018.drop(map_spring_2018[map_spring_2018.Discipline.isin(["Language","Mathematics","Science"])].index)
map_fall_2018_reading = map_fall_2018.drop(map_fall_2018[map_fall_2018.Discipline.isin(["Language","Mathematics","Science"])].index)
map_ay_2017_2018_reading = map_ay_2017_2018.drop(map_ay_2017_2018[map_ay_2017_2018.Discipline.isin(["Language","Mathematics","Science"])].index)


# Create CSV files for df

map_fall_2017_reading.to_csv('13_map fall 2017 reading.csv')
map_winter_2017_reading.to_csv('14 map winter 2018 reading.csv')
map_spring_2018_reading.to_csv('15_map spring 2018 reading.csv')
map_fall_2018_reading.to_csv('16 map fall 2018 reading.csv')
map_ay_2017_2018_reading.to_csv('17 map ay 2017 2018 reading.csv')


# In[11]:


# Create MAP Language df by year

map_fall_2017_language = map_fall_2017.drop(map_fall_2017[map_fall_2017.Discipline.isin(["Reading","Mathematics","Science"])].index)
#map_winter_2017_language = map_winter_2017.drop(map_winter_2017[map_winter_2017.Discipline.isin(["Reading","Mathematics","Science"])].index)
map_spring_2018_language = map_spring_2018.drop(map_spring_2018[map_spring_2018.Discipline.isin(["Reading","Mathematics","Science"])].index)
map_fall_2018_language = map_fall_2018.drop(map_fall_2018[map_fall_2018.Discipline.isin(["Reading","Mathematics","Science"])].index)
map_ay_2017_2018_language = map_ay_2017_2018.drop(map_ay_2017_2018[map_ay_2017_2018.Discipline.isin(["Reading","Mathematics","Science"])].index)


# Create CSV files for df

map_fall_2017_language.to_csv('18 map fall 2017 language.csv')
# No language discipline for map_winter_2017
map_spring_2018_language.to_csv('19 map spring 2018 language.csv')
map_fall_2018_language.to_csv('20 map fall 2018 language.csv')
map_ay_2017_2018_language.to_csv('21 map ay 2017 2018 language.csv')


# In[12]:


# Create MAP Mathematics df by year

map_fall_2017_mathematics = map_fall_2017.drop(map_fall_2017[map_fall_2017.Discipline.isin(["Reading","Language","Science"])].index)                                                            
map_winter_2017_mathematics = map_winter_2017.drop(map_winter_2017[map_winter_2017.Discipline.isin(["Reading","Language","Science"])].index)
map_spring_2018_mathematics = map_spring_2018.drop(map_spring_2018[map_spring_2018.Discipline.isin(["Reading","Language","Science"])].index)
map_fall_2018_mathematics = map_fall_2018.drop(map_fall_2018[map_fall_2018.Discipline.isin(["Reading","Language","Science"])].index)
map_ay_2017_2018_mathematics = map_ay_2017_2018.drop(map_ay_2017_2018[map_ay_2017_2018.Discipline.isin(["Reading","Language","Science"])].index)

#Research how to drop items listed as false
    #map_fall_2017_Mathematics = map_fall_2017_Mathematics.drop(map_fall_2017_Mathematics[map_fall_2017_Mathematics.GrowthMeasureYN.isin(["False"])].index)
    #map_winter_2017_Mathematics = map_winter_2017_Mathematics.drop(map_winter_2017_Mathematics[map_winter_2017_Mathematics.GrowthMeasureYN.isin(["False"])].index)
    #map_spring_2018_Mathematics = map_spring_2018_Mathematics.drop(map_spring_2018_Mathematics[map_spring_2018_Mathematics.GrowthMeasureYN.isin(["False"])].index)
    #map_fall_2018_Mathematics = map_fall_2018_Mathematics.drop(map_fall_2018_Mathematics[map_fall_2018_Mathematics.Discipline.GrowthMeasureYN.isin(["False"])].index)


# Create CSV files for df

map_fall_2017_mathematics.to_csv('22 map fall 2017 mathematics.csv')
map_winter_2017_mathematics.to_csv('23 map winter 2018 mathematics.csv')
map_spring_2018_mathematics.to_csv('24 map spring 2018 mathematics.csv')
map_fall_2018_mathematics.to_csv('25 map fall 2018 mathematics.csv')
map_ay_2017_2018_mathematics.to_csv('26 map ay 2017 2018 mathematics.csv')


# In[13]:


# Index Map (Reading, Language, Mathematics) and MESH (SEL and CC) frames by StudentID

map_fall_2017_reading = map_fall_2017_reading.set_index('StudentID')
map_winter_2017_reading = map_winter_2017_reading.set_index('StudentID')
map_spring_2018_reading = map_spring_2018_reading.set_index('StudentID')
map_fall_2018_reading = map_fall_2018_reading.set_index('StudentID')
map_ay_2017_2018_reading = map_ay_2017_2018_reading.set_index('StudentID')
map_fall_2017_language = map_fall_2017_language.set_index('StudentID')
map_spring_2018_language = map_spring_2018_language.set_index('StudentID')
map_fall_2018_language = map_fall_2018_language.set_index('StudentID')
map_ay_2017_2018_language = map_ay_2017_2018_language.set_index('StudentID')
map_fall_2017_mathematics = map_fall_2017_mathematics.set_index('StudentID')
map_winter_2017_mathematics = map_winter_2017_mathematics.set_index('StudentID')
map_spring_2018_mathematics = map_spring_2018_mathematics.set_index('StudentID')
map_fall_2018_mathematics = map_fall_2018_mathematics.set_index('StudentID')
map_ay_2017_2018_mathematics = map_ay_2017_2018_mathematics.set_index('StudentID')
mesh_sel_fall_2017 = mesh_sel_fall_2017.set_index('StudentID')
mesh_cc_fall_2017 = mesh_cc_fall_2017.set_index('StudentID')
mesh_sel_spring_2018 = mesh_sel_spring_2018.set_index('StudentID')
mesh_cc_spring_2018 = mesh_cc_spring_2018.set_index('StudentID')
mesh_sel_fall_2018 = mesh_sel_fall_2018.set_index('StudentID')
mesh_cc_fall_2018 = mesh_cc_fall_2018.set_index('StudentID')


# In[14]:


# Merge Mesh SEL and CC tables

mesh_fall_2017_total = pd.merge(mesh_sel_fall_2017, mesh_cc_fall_2017, on='StudentID')
mesh_spring_2018_total = pd.merge(mesh_sel_spring_2018, mesh_cc_spring_2018, on='StudentID')
mesh_fall_2018_total = pd.merge(mesh_sel_fall_2018, mesh_cc_fall_2018, on='StudentID')

# Merge MAP fall, winter, spring with AY2017-2018

map_fall_2017_reading_total = pd.merge(map_fall_2017_reading, map_ay_2017_2018_reading, how="left", on=['StudentID','TermName'])
map_winter_2017_reading_total = pd.merge(map_winter_2017_reading, map_ay_2017_2018_reading, how="left", on=['StudentID','TermName'])
map_spring_2018_reading_total = pd.merge(map_spring_2018_reading, map_ay_2017_2018_reading, how="left", on=['StudentID','TermName'])
map_fall_2018_reading_total = pd.merge(map_fall_2018_reading, map_ay_2017_2018_reading, how="left", on=['StudentID','TermName'])
map_fall_2017_language_total = pd.merge(map_fall_2017_language, map_ay_2017_2018_language, how="left", on=['StudentID','TermName'])
map_spring_2018_language_total = pd.merge(map_spring_2018_language, map_ay_2017_2018_language, how="left", on=['StudentID','TermName'])
map_fall_2018_language_total = pd.merge(map_fall_2018_language, map_ay_2017_2018_language, how="left", on=['StudentID','TermName'])
map_fall_2017_mathematics_total = pd.merge(map_fall_2017_mathematics, map_ay_2017_2018_mathematics, how="left", on=['StudentID','TermName'])
map_winter_2017_mathematics_total = pd.merge(map_winter_2017_mathematics, map_ay_2017_2018_mathematics, how="left", on=['StudentID','TermName'])
map_spring_2018_mathematics_total = pd.merge(map_spring_2018_mathematics, map_ay_2017_2018_mathematics, how="left", on=['StudentID','TermName'])
map_fall_2018_mathematics_total = pd.merge(map_fall_2018_mathematics, map_ay_2017_2018_mathematics, how="left", on=['StudentID','TermName'])


# In[15]:


# Join MAP and MESH data

#Reading
map_fall_2017_reading_total = pd.merge(map_fall_2017_reading_total, mesh_fall_2017_total, how="left", on=['StudentID'])
map_spring_2018_reading_total = pd.merge(map_spring_2018_reading_total, mesh_spring_2018_total, how="left", on=['StudentID'])
map_fall_2018_reading_total = pd.merge(map_fall_2018_reading_total, mesh_fall_2018_total, how="left", on=['StudentID'])

#Language
map_fall_2017_language_total = pd.merge(map_fall_2017_language_total, mesh_fall_2017_total, how="left", on=['StudentID'])
map_spring_2018_language_total = pd.merge(map_spring_2018_language_total, mesh_spring_2018_total, how="left", on=['StudentID'])
map_fall_2018_language_total = pd.merge(map_fall_2018_language_total, mesh_fall_2018_total, how="left", on=['StudentID'])

#Mathematics
map_fall_2017_mathematics_total = pd.merge(map_fall_2017_mathematics_total, mesh_fall_2017_total, how="left", on=['StudentID'])
map_spring_2018_mathematics_total = pd.merge(map_spring_2018_mathematics_total, mesh_spring_2018_total, how="left", on=['StudentID'])
map_fall_2018_mathematics_total = pd.merge(map_fall_2018_mathematics_total, mesh_fall_2018_total, how="left", on=['StudentID'])


# In[16]:


#Concatenate Map and MESH Total Frames by Year

#map_mesh_fall_2017
map_mesh_fall_2017 = map_fall_2017_reading_total.append([map_fall_2017_language_total, map_fall_2017_mathematics_total])
map_mesh_fall_2017.to_csv('27 map mesh fall 2017.csv')

#map_mesh_sring_2017
map_mesh_spring_2018 = map_spring_2018_reading_total.append([map_spring_2018_language_total, map_spring_2018_mathematics_total])
map_mesh_spring_2018.to_csv('28 map mesh spring 2018.csv')

#map_mesh_fall_2018
map_mesh_fall_2018 = map_fall_2018_reading_total.append([map_fall_2018_language_total, map_fall_2018_mathematics_total])
map_mesh_fall_2018.to_csv('29 map mesh fall 2018.csv')

#map_winter_2018
map_winter_2017 = map_winter_2017_reading_total.append([map_winter_2017_mathematics_total])
map_winter_2017.to_csv('30 map winter 2017.csv')


# In[17]:

# List data columns

map_fall_2017_list = list(map_fall_2017)
map_winter_2017_list = list(map_winter_2017)
map_spring_2018_list = list(map_spring_2018)
map_fall_2018_list = list(map_fall_2018)
map_ay_2018_2018_list = list(map_ay_2017_2018)
mesh_sel_fall_2017_list = list(mesh_sel_fall_2017)
mesh_cc_fall_2017_list = list(mesh_cc_fall_2017)
mesh_sel_spring_2018_list = list(mesh_sel_spring_2018)
mesh_cc_spring_2018_list = list(mesh_cc_spring_2018)
mesh_sel_fall_2018_list = list(mesh_sel_fall_2018)
mesh_cc_fall_2018_list = list(mesh_cc_fall_2018)
student_names_id_list = list(student_names_id)

