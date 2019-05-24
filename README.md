# Heuristieken - Smart Grid
---
**Project**

Green energy is nowadays the energy of the future. Many houses receive their energy through solar panels, wind turbines or other installations. The problem here is that these installations often produce more than is necessary for their own consumption. It would be an economic advantage when the surplus could be sold back to the supplier. However, the infrastructure in this case (what we call the grid), is usually not designed for this particullar topic. To manage the overconsumptions and production, it is necessary to place batteries between the houses. Each of these batteries have a maximum capacity, whereby the houes have a maximum output.

The importance of this project is to see how the batteries can best be placed and how the costs can be reduced the most (based no the distances).

---

**Getting Started**
---
### Prerequisites

This code is written in [Python 3.7.3](https://www.python.org/downloads/). Requirements.txt contains all the necessary packages to successfully run the code. These are easy to install via pip with the following instruction:

````
pip install -r requirements.txt
````
### Structure

---

The code is divided into different directories, which we describe here one by one.

*Classes:*


This folder contains the following objects:
- Battery
- Cable
- Grid
- House

For more information about these objects, you can have a look into the [properties and methods](https://github.com/Gwyd10n/Smart_grid/blob/master/classes/README.md).

*Data:*

This folder contains all data sets that have been used for this smart grid.

In addition, there is also a second folder, called results. If you choose to save the results of a chosen algorithm, these can be found here.

*Helpers:*

All algorithms are listed in this folder.

In addition to the algorithms, there are also four other files, called helpers, visualizer, clui and clui_test. Helpers is a file that contains functions that are helpful for the algorithms. Visualizer will plot a grid for each algorithm that you will run. Clui is the command line user interface, which contains all the instructions for the user. Clui_test is also a command line interface, which is only useful for analysis of the data.

For a brief introduction to each algorithm, you can click [here](https://github.com/Gwyd10n/Smart_grid/blob/master/helpers/README.md).

### Testing

---

To start the users interface, you have to run the following in your terminal:

```
$ python application.py
```
The terminal will show you the way to apply different algorithms and save the results.


### Authors

---

- Gwydion Oostvogel
- Sophie Schubert

### Acknowledgments

---

- Stackoverflow
- Wouter Vrielink, Arne Meijs and Daan van den Berg
