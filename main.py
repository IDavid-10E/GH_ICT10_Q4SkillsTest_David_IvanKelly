from pyscript import document, display
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt
days_list = []
absent_list = []

def add_data(event):
    day = document.getElementById("day").value
    absent = document.getElementById("absent").value
    msg = document.getElementById("msg")

    if day == "" or absent == "":
        msg.innerHTML = "<p style='color:#fff82e;'>Complete inputs pls.</p>"
        return

    if day in days_list:
        msg.innerHTML = "<p style='color:#7729ff;'>Day already added.</p>"
        return

    days_list.append(day)
    absent_list.append(int(absent))

    msg.innerHTML = f"<p style='color:#14ff47;'>Added! {day} - {absent}</p>"


def plot_graph(event):
    if len(days_list) == 0:
        document.getElementById("msg").innerHTML = "<p style='color:#ff1f1f;'>No data</p>"
        return

    x = np.array(days_list)
    y = np.array(absent_list)

    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o')

    ax.set_title("Attendance (Absences)")
    ax.set_xlabel("Day")
    ax.set_ylabel("Number of Absences")
    ax.grid()

    display(fig, target="graph", append=False)


def reset_all(event):
    global days_list, absent_list

    days_list.clear()
    absent_list.clear()

    document.getElementById("graph").innerHTML = ""
    document.getElementById("msg").innerHTML = "<p style='color:#FFFFFF;'>Refreshed.</p>"