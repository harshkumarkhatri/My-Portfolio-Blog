import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/home/ubuntu/harshblog/harshblog/")

from app import app as application

application.secret_key = "Jo krna hai kr"
