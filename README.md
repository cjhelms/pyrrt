# WORK IN PROGRESS

This project is in very early development and the API is constantly changing.

# About

This project provides an implementation of Steve LaVelle's Rapidly-Exploring
Random Trees (RRT) data structure and derivatives.

RRT is a data structure designed for efficiently searching non-convex 
high-dimensional spaces.

RRT is primarly intended for use as a path-planning algorithm, and particurarly
excels at handling nonholonomic systems navigating obstacles, but can be used
for any search problem which can be cast as searching for a path in a
dimensional space.

# Package Objective

A nonholonomic system is a system which has fewer degrees of control than
degrees of control. For example, under normal operation, a bicycle can freely
roll forward (and backwards, with some skill), but will just fall over if you
try to move from side-to-side. The only way to go, for example, left is to turn
the handlebars and move forward -- The rider does not have direct control in the
side-to-side dimension.

It turns out, in general, nonholonomic systems are really hard to make motion
plans for. It also turns out, some of the most important control problems facing
humanity at the moment are about controlling a nonholonomic system, like
self-driving cars. It ALSO turns out, the mathematics behind nonholonomic
systems and motion planning in general can be very intimidating.

The primary objective of this package is to provide an easy-to-use, pragmatic
motion planner capable of natively handling nonholonomic systems written in
Python with the target audience being robotics enthusiasts tinkering on projects
on a Raspberry PI or laptop/desktop. The vision is to provide many derivatives
of RRT so the user can select the most applicable solution to their problem, but
maintain a simple, common interface between them all.

The secondary objective of the package is to be performant. A motion planner
which cannot run real-time is not particularly useful, after all.

# Roadmap

- [ ] Implement the original RRT
- [ ] Implement RRT*
- [ ] Implement Closed-Loop RRT (CL-RRT)
- [ ] Implement CL-RRT*
