from flask import Flask
from flask_cors import CORS
from flask_cors import cross_origin
import json
import os
import psutil
import time

app = Flask(__name__)
CORS(app)   # Necessary since API is running locally

period = 1

# Disable Flask console messages: http://stackoverflow.com/a/18379764
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@cross_origin()
@app.route('/')
def index():

    disk_write_data_start = psutil.disk_io_counters(perdisk=False)
    io_data_start = psutil.net_io_counters()
    
    time.sleep(period)

    cpu_data = psutil.cpu_percent(interval=None)
    ram_data = psutil.virtual_memory()
    disk_data = psutil.disk_usage('/')
    disk_write_data = psutil.disk_io_counters(perdisk=False)
    io_data = psutil.net_io_counters()

    data = {
        'cpu': {
            'percent': cpu_data
            },
        'ram': {
            'percent': ram_data[2],
            'total': ram_data[0],
            'used': ram_data[3]
            },
        'disk': {
            'total': disk_data[0],
            'used': disk_data[1],
            'percent': disk_data[3],
            'read_bytes_sec': (disk_write_data[2] - disk_write_data_start[2]) \
                                / period,
            'write_bytes_sec': (disk_write_data[3] - disk_write_data_start[3]) \
                                / period
            },
        'io': {
            'sent_bytes_sec': (io_data[0] - io_data_start[0]) / period,
            'received_bytes_sec': (io_data[1] - io_data_start[1]) / period
            }
    }

    return json.dumps(data)

if __name__ == "__main__":
    print "System API up at http://localhost:5002"
    PORT = int(os.getenv('PORT', 5002))
    app.run(port=PORT, threaded=True)