from django.test import TestCase
import jwt
from website import settings

# Create your tests here.
str2 = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODEyOTg1NTAsImlhdCI6MTY4MTIxMjE1MCwiZGF0YSI6eyJuYW1lIjoicm9vdCJ9fQ.2dO7k4WTMqBpZwh6mKUXq6MNJZwZujHqmsn4oz8meW4'
str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODEyOTczODcsImlhdCI6MTY4MTIxMDk4NywiZGF0YSI6eyJuYW1lIjoicm9vdCJ9fQ.Yy-fj8QDWlwzEWil1J7h0i6a3QUlGy9OVgDBI5rUXEg'
print(jwt.decode(str2, settings.SECRET_KEY, algorithms=['HS256']))
