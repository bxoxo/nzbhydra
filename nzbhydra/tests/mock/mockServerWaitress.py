from waitress import serve

from nzbhydra.tests.mock.mockServer import app as application

serve(application, port=5001, host="0.0.0.0")
