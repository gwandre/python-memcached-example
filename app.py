import pylibmc, time
#client = memcache.Client([('localhost', 11211)])
client = pylibmc.Client(['localhost:11211'])

objectToStore = {"name" : "Person Name", "age": "38"}

client.set("user1", objectToStore, 5)
print("Object stored to memcached, expires in 15s")
print(client.get("user1"))

print("Waiting 4s...")
time.sleep(4)
print(client.get("user1"))

print("Waiting more 4s...")
time.sleep(4)
print(client.get("user1"))
