# system-dashboard

![](docs/system-dashboard-gif.gif)

Minimalist Win/OSX/Linux System Dashboard for Python 2/3 using Flask and [Freeboard](https://github.com/Freeboard/freeboard). This tool was created extremely quickly (less than a couple hours) as a "Hello World" test for both technologies, with impressive and practical results for the amount of time invested.

The cross-platform system information is derived from the `psutil` Python package.

## Setup

To install the Python dependencies, run:

```
pip install psutil flask flask_cors
```

Then run the Flask server by `cd` into the folder containing the files, then run:

```
python flask_system.py
```

After the server starts running, open up a Freeboard window by opening `system_dashboard.html` in any browser, choose Load Freeboard, and select the `system_daskboard_flask.json` config file. Done!

## Credits

[Flask JSONDash](https://github.com/christabor/flask_jsondash) by Chris Tabor which gave me the silly idea to work on a local dashboard, and noted the CORS requirement for Flask.

## License

MIT

The included Freeboard code is redistributed per its MIT License.