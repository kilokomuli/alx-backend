import redis from 'redis';
import { createClient } from 'redis';

const client = createClient();

client.on('error', err => {
  console.log(`Redis client not connected to server: ${error.message}`);
  redisClient.quit();
});
client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    console.log(reply);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
