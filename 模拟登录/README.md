模拟登录（豆瓣为例）  
思路：找到登录post数据的真实url。  
找到需要post的所有data。 
用一个session保持会话。  
向登录的url post登录需要的数据（用户名、密码等）。  
带cookies获取需要登录的页面。  
