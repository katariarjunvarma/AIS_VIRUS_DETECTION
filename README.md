# AIS_VIRUS_DETECTION
1. Introduction to AIS
   
•	What is AIS? 

o	Artificial Immune Systems (AIS) are inspired by the human immune system. They detect "viruses" (anomalies) by distinguishing between "self" (normal) and "non-self" (abnormal) patterns.

o	This code uses the Negative Selection Algorithm, where detectors are trained to recognize non-self patterns.

•	Why is it Useful? 

o	It’s great for virus detection in computers because it adapts to normal behavior and flags anything unusual.

2. How the Code Works
   
•	Self Points (Blue): 

o	100 random 2D points represent normal behavior (e.g., typical network traffic).

•	Detectors (Red): 

o	50 points are generated that don’t overlap with self points. These detect anomalies.

•	Test Points: 

o	40 new points simulate incoming data. Some are normal (green), some are anomalous (orange).

•	Classification: 

o	If a test point is near a detector, it’s flagged as anomalous (1). Otherwise, it’s normal (0).

•	Evaluation: 

o	Accuracy shows how well it works. False positives and negatives show mistakes.

3. Show the Output

•	Console: 

o	"Accuracy: 0.85 means 85% of test points were correctly classified."

o	"False Positives: 3 means 3 normal points were wrongly flagged as viruses."

o	"False Negatives: 2 means 2 viruses were missed."

•	Plot: 

o	Point to the blue points: "These are normal system data."

o	Red points: "These detectors catch anomalies."

o	Green and orange points: "Green are normal test data, orange are anomalies. See how detectors catch the orange ones!"

4. Why It Matters?

•	This AIS can be used for real-time virus detection in networks or systems.

•	It’s simple but shows the core idea: train on normal data, detect anything unusual.

Understanding the Output

Console Output

When you run the code, the terminal will display something like this (values will vary due to randomness):

Accuracy: 0.85

False Positives: 3

False Negatives: 2

•	Accuracy: A number between 0 and 1 (e.g., 0.85 means 85% correct). It shows how often the AIS correctly classified test points.

•	False Positives: Number of normal points wrongly classified as anomalous (e.g., 3).

•	False Negatives: Number of anomalous points wrongly classified as normal (e.g., 2).

Plot Output

A window will open with a scatter plot:

•	Blue Points: Self points (normal system behavior).

•	Red Points: Detectors (covering anomalous regions).

•	Green Points: Test points that are truly normal.

•	Orange Points: Test points that are truly anomalous.

The plot visually shows how detectors are placed in areas away from normal (self) points and how test points are distributed.
