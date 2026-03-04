AI Assignment 2

Anish Bandaru
SE24UCSE007

Overview 
This assignment consists of three Python programs that
demonstrate important concepts in Artificial Intelligence. The programs
implement CAPTCHA generation, a reflex agent for calculating the Air
Quality Index (AQI), and search algorithms for solving a classic
problem.

1.  CAPTCHA Generator

This program generates a CAPTCHA image and verifies whether the user
enters the correct characters shown in the image.

First, a random string containing letters and numbers is generated. An
image is then created using the Python Imaging Library (PIL), and the
generated text is drawn onto the image. To make it difficult for
automated programs (bots) to read the CAPTCHA, random lines and dots are
added as noise.

The generated CAPTCHA image is displayed to the user, who must enter the
characters shown in the image. If the entered text matches the generated
CAPTCHA text, the program displays a success message. Otherwise, it
informs the user that the CAPTCHA entered is incorrect.

Implementation File: captcha.py

2.  AQI Simple Reflex Agent

This program implements a simple reflex agent that calculates the Air
Quality Index (AQI) using environmental pollution data.

The program reads pollutant values such as PM2.5, PM10, NO2, SO2, CO,
NH3, and O3 from a dataset. Using predefined AQI breakpoint ranges, the
program calculates the sub-index for each pollutant.

The pollutant with the highest sub-index is identified as the dominant
pollutant, and its value determines the final AQI.

Based on the calculated AQI value, the air quality is categorized into
levels such as: Good Satisfactory Moderate Poor Very Poor Severe

The dataset visakhapatnam_aqi.csv should be downloaded and placed in the
same folder as the program so that the program can read the pollution
data.

Implementation File: aqi_agent.py

Dataset Used: visakhapatnam_aqi.csv

3.  Missionaries and Cannibals Problem

This program solves the classic Missionaries and Cannibals problem using
different search algorithms.

In this problem, three missionaries and three cannibals are on one side
of a river and must cross to the other side using a boat that can carry
only two people at a time. The rule is that the number of cannibals
should never exceed the number of missionaries on either side of the
river.

Each situation in the problem is represented as a state showing the
number of missionaries and cannibals on the left side of the river along
with the position of the boat.

Algorithms implemented: Breadth First Search (BFS) Uniform Cost Search
(UCS) Depth First Search (DFS) Depth Limited Search (DLS) Iterative
Deepening Depth First Search (IDDFS)

Implementation File: missionaries_cannibals.py


Conclusion Through this assignment, different Artificial Intelligence
concepts were implemented using Python programs. The CAPTCHA generator
demonstrates a simple human verification system used to prevent
automated access. The AQI reflex agent shows how an intelligent agent
can analyze environmental data and make decisions based on predefined
rules. The Missionaries and Cannibals program demonstrates the use of
search algorithms to explore possible states and find a valid solution
to a problem.
