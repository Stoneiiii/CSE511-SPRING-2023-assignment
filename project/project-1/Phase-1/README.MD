# Introduction & Background

A major peer-to-peer taxi cab firm has hired your team to develop and run multiple spatial queries on their large database that contains geographic data and real-time location data of their customers. A spatial query is a special query supported by geodatabases and spatial databases. The queries differ from traditional SQL queries because they allow for using points, lines, and polygons. The spatial queries also consider the relationship between these geometries. Since the database is large and mostly unstructured, your client wants you to use a popular Big Data software application, SparkSQL. The goal of the project is to extract data from this database that will be used by your client for operational (day-to-day) and strategic-level (long-term) decisions.

# Problem Statement

In this project, a rectangle, R, represents a geographical boundary in a town or city, and a set of points, P, represents customers who request taxi cab service using the client firm’s app.

- Range query:
	- Given a query rectangle R and a set of points P, find all the points within R. You need to use the ‘ST_Contains’ function in this query.
- Range join query:
	- Given a set of rectangles R and a set of points P, find all (point, rectangle) pairs such that the point is within the rectangle.
- Distance query:
	- Given a fixed point location P and distance D (in kilometres), find all points within distance D from P. You need to use the ‘ST_Within’ function in this query.
- Distance join query:
	- Given two sets of points P1 and P2, and a distance D (in kilometres), find all(p1, p2) pairs such that p1 is within a distance D from p2(i.e., p1 belongs to P1 and p2 belongs to P2). You need to use the ‘ST_Within’ function in this query.