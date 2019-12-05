#!/usr/bin/env python
# coding: utf-8

# API 資料串接 - 以 Dcard API 實作範例
# 利用 urllib 套件的 urlretrieve 方法下載檔案
# 了解 Python File I/O 讀檔、寫檔的用法
# 能用運用資源管理器 With Statement 優化寫法
# 作業目標
# 請利用 API: https://www.dcard.tw/_api/forums/pet/posts?popular=true 回答下列問題：
# 
# 這個 API 一次會回傳幾筆資料？每一筆資料包含哪些欄位？
# 
# 取出每一筆資料的「標題」、「貼文時間」、「留言人數」、「按讚人數」
# 計算熱門/非熱門文章的「平均留言人數」與「平均按讚人數」

# In[1]:


import requests
import json


# In[2]:


import pandas as pd


# In[13]:


r_pop = requests.get('https://www.dcard.tw/_api/forums/pet/posts?popular=true')
r_npop = requests.get('https://www.dcard.tw/_api/forums/pet/posts?popular=false')

resp_pop = r_pop.text
resp_npop = r_npop.text

#data_pop = json.loads(resp_pop)
#data_npop = json.loads(resp_npop)
df_pop = pd.read_json(resp_pop)
df_npop = pd.read_json(resp_npop)


# In[14]:


print('熱門文章有%s筆資料\n' % len(df_pop))
print('非熱門文章有%s筆資料\n' % len(df_npop))


# In[15]:


cols_name = ['標題', '貼文時間', '留言人數', '按讚人數']


# In[16]:


df_pop_r = df_pop[['title', 'createdAt', 'commentCount', 'likeCount']]
df_pop_r.columns = cols_name
print('熱門文章:\n')
df_pop_r


# In[17]:


# 非熱門文章
df_npop_r = df_npop[['title', 'createdAt', 'commentCount', 'likeCount']]
df_npop_r.columns = cols_name
print('非熱門文章:\n')
df_npop_r


# In[18]:


# 3. 計算熱門/非熱門文章的「平均留言人數」與「平均按讚人數」
print('熱門文章-平均留言人數:', df_pop_r['留言人數'].mean())
print('熱門文章-平均按讚人數:', df_pop_r['按讚人數'].mean())
print('非熱門文章-平均留言人數:', df_npop_r['留言人數'].mean())
print('非熱門文章-平均按讚人數:', df_npop_r['按讚人數'].mean())


# In[ ]:




