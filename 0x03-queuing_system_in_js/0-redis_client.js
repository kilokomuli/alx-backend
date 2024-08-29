import { createClient } from 'redis';

const client = createClient();

client.on('error', err => {
  console.log(`Redis client not connected to server: ${error.message}`);
  redisClient.quit();
});
client.on('connect', () => console.log('Redis client connected to the server'));
