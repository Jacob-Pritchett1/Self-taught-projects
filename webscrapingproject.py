# Imports the Flask class and the render_template method
from flask import Flask, render_template
# Second line imports the Beautiful Soup class.
from bs4 import BeautifulSoup
# Third line imports requests module
import requests

source = requests.get('http://books.toscrape.com/').text
# source is the variable that will hold the HTML plain text.

soup = BeautifulSoup(source, 'html.parser')
# soup variable will store our value after source to Beautiful Soup
# lxml is the markup for our rendered code.

print(soup)
