import requests
import time

local_url = 'http://localhost:5000/result'

num_runs = 100
total_response_time = 0

for _ in range(num_runs):
    payload = {'option': '############'}
    start_time = time.time()
    response = requests.post(local_url, data=payload)
    end_time = time.time()
    response_time = end_time - start_time
    
    total_response_time += response_time
    print(response_time)

average_response_time = total_response_time / num_runs

print(f'Average Response Time: {average_response_time:.2f} seconds')
