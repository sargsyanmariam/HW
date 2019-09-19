
# coding: utf-8

# In[1]:


import json


# In[2]:


f = open("C:/Users/user/Desktop//cities.json")


# In[3]:


data = json.load(f)


# In[7]:


#Problem 2
company_city = {}
for city in data:
    for company in city['company']:
        city_name = city['city']
        comp_name = company['name']
        if company_city.get(comp_name) != None:
            company_city[comp_name].append(city_name)
        else:
            company_city[comp_name] = [city['city']]
print(company_city)


# In[5]:


#Problem 1
#Find all cities where there is no "Chemicals"
cities_with_no_chemicals =[]
for city in data:
    for company in city['company']:
        if company['industry'] != 'Chemicals':
            cities_with_no_chemicals.append(city['city'])
            break    
cities_with_no_chemicals  

