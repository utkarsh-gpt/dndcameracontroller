from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://crashgamer0122:9DrTvjRaJvmrcIwo@cluster0.pymb0uj.mongodb.net/')  # Use your actual MongoDB connection string
db = client['arduino_input']
collection = db['input']