# import json
# import os

# # Read the JSON file
# with open('allData.json') as file:
#     data = json.load(file.read())
# # Prompt the user to enter a key
# key = input("Enter a key: ")
# # Check if the key exists in the JSON data
# if key in data:
#     # Run your code for the specified key
#     block = data[key]
#     # Execute your desired code using the block
#     print("Code executed for key:", key)
# else:
#     print("Key not found in the JSON data.")

# 

# import json

# # Read the JSON file
# with open('allData.json') as file:
#     data = json.load(file)
    
# # Prompt the user to enter a key
# key = input("Enter a key: ")

# # Check if the key exists in the JSON data
# if key in data[0]:
#     # Run your code for the specified key
#     block = data[0][key]
#     # Execute your desired code using the block
#     print("Code executed for key:", key)
# else:
#     print("Key not found in the JSON data.")


# import json

# # Read the JSON file
# with open('allData.json') as file:
#     data = json.load(file)

# # Prompt the user to enter a key
# key = input("Enter a key: ")

# # Check if the key exists in the JSON data
# if key in data[0]:
#     # Run your code for the specified key
#     block = data[0][key]
#     # Execute your desired code using the block
#     print("Code executed for key:", key)

#     # Print the data inside the thermostatPacket key
#     print(json.dumps(block, indent=4))
# else:
#     print("Key not found in the JSON data.")

# import json
# import matplotlib.pyplot as plt
# from datetime import datetime

# # Read the JSON file
# with open('allData.json') as file:
#     data = json.load(file)

# # Prompt the user to enter a key
# key = input("Enter a key: ")

# # Check if the key exists in the JSON data
# if key in data[0]:
#     # Run your code for the specified key
#     block = data[0][key]
#     # Execute your desired code using the block
#     print("Code executed for key:", key)

#     # Extract the timestamp and temperature data
#     timestamps = []
#     temperatures = []
#     for entry in block['data']:
#         timestamp_str = entry['timestamp']
#         temperature = entry['indoorTemperature10xF'] / 10  # Convert to degrees Fahrenheit
#         timestamp = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%SZ")
#         timestamps.append(timestamp)
#         temperatures.append(temperature)

#     # Plot the graph
#     plt.plot(timestamps, temperatures)
#     plt.xlabel('Timestamp')
#     plt.ylabel('Temperature (°F)')
#     plt.title('Temperature Variation')
#     plt.show()

# else:
#     print("Key not found in the JSON data.")

# 

# import json
# import matplotlib.pyplot as plt
# from datetime import datetime
# from flask import Flask, render_template, send_file

# # Read the JSON file
# with open('allData.json') as file:
#     data = json.load(file)

# # Create a Flask application
# app = Flask(__name__)

# # Route for displaying the graph
# @app.route('/')
# def display_graph():
#     # Prompt the user to enter a key
#     key = input("Enter a key: ")

#     # Check if the key exists in the JSON data
#     if key in data[0]:
#         # Run your code for the specified key
#         block = data[0][key]
#         # Execute your desired code using the block
#         print("Code executed for key:", key)

#         # Extract the timestamp and temperature data
#         timestamps = []
#         temperatures = []
#         timestamp_str = block['data']['timestamp']
#         temperature = block['data']['indoorTemperature10xF'] / 10  # Convert to degrees Fahrenheit
#         timestamp = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%SZ")
#         timestamps.append(timestamp)
#         temperatures.append(temperature)

#         # Plot the graph
#         plt.plot(timestamps, temperatures)
#         plt.xlabel('Timestamp')
#         plt.ylabel('Temperature (°F)')
#         plt.title('Temperature Variation')
#         plt.savefig('graph.png')  # Save the plot as an image file

#         return send_file('graph.png', mimetype='image/png')  # Display the image file in the browser

#     else:
#         return "Key not found in the JSON data."


# if __name__ == '__main__':
#     app.run()


import json
from flask import Flask, render_template

# Read the JSON file
with open('allData.json') as file:
    data = json.load(file)

# Create a Flask application
app = Flask(__name__)

# Route for displaying the data in tabular format
@app.route('/')
def display_data():
    # Prompt the user to enter a key
    key = input("Enter a key: ")

    # Check if the key exists in the JSON data
    if key in data[0]:
        # Run your code for the specified key
        block = data[0][key]
        # Execute your desired code using the block
        print("Code executed for key:", key)

        # Extract the data
        table_data = block['data']
        timestamp = table_data['timestamp']

        return render_template('data.html', timestamp=timestamp, table_data=table_data)

    else:
        return "Key not found in the JSON data."


if __name__ == '__main__':
    app.run()












