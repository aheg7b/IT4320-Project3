import os
import io
from flask import Flask, render_template, request, send_from_directory, jsonify, url_for
import requests
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime