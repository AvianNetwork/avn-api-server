from server import config
from server import app

app.url_map.strict_slashes = False

if __name__ == '__main__':
	app.run()
