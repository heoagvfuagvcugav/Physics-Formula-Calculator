from tkinter import *

window = Tk()
window.title("Physics")

results = []


def click():

	del results[:]


	if len(str(voltage.get())) != 0:
		v = float(voltage.get())
		results.append("Voltage = " + str(v))
	else:
		v = None

	if len(str(ampage.get())) != 0:
		i = float(ampage.get())
		results.append("Ampage = " + str(i))
	else:
		i = None

	if len(str(resistance.get())) != 0:
		r = float(resistance.get())
		results.append("Resistance = " + str(r))
	else:
		r = None

	if len(str(time.get())) != 0:
		t = float(time.get())
		results.append("Time = " + str(t))
	else:
		t = None

	if len(str(power.get())) != 0:
		p = float(power.get())
		results.append("Power = " + str(p))
	else:
		p = None

	if len(str(speed.get())) != 0:
		s = float(speed.get())
		results.append("Speed = " + str(s))
	else:
		s = None

	if len(str(distance.get())) != 0:
		d = float(distance.get())
		results.append("Distance = " + str(d))
	else:
		d = None

	if len(str(acceleration.get())) != 0:
		a = float(acceleration.get())
		results.append("Acceleration = " + str(a))
	else:
		a = None

	if len(str(force.get())) != 0:
		f = float(force.get())
		results.append("Force = " + str(f))
	else:
		f = None

	if len(str(mass.get())) != 0:
		m = float(mass.get())
		results.append("Mass = " + str(m))
	else:
		m = None

	if len(str(weight.get())) != 0:
		w = float(weight.get())
		results.append("Weight = " + str(w))
	else:
		w = None

	if len(str(gravity.get())) != 0:
		g = float(gravity.get())
		results.append("Gravity = " + str(g))
	else:
		g = None


	if m and g:
		w = round(m * g, 2)
		results.append("Weight = " + str(w))

	if w and g:
		m = round(w / g, 2)
		results.append("Mass = " + str(m))

	if w and m:
		g = round(w / m, 2)
		results.append("Gravity = " + str(g))

	if m and a:
		f = round(m * a, 2)
		results.append("Force = " + str(f))

	if f and a:
		m = round(f / a, 2)
		results.append("Mass = " + str(m))

	if f and m:
		a = round(f / m, 2)
		results.append("Acceleration = " + str(a))

	if d and t:
		s = round(d / t, 2)
		results.append("Speed = " + str(s))

	if d and s:
		t = round(d / s, 2)
		results.append("Time = " + str(t))

	if s and t:
		d = round(s * t, 2)
		results.append("Distance = " + str(d))

	if i and r:
		v = round(i * r, 2)
		results.append("Voltage = " + str(v))

	if i and v:
		r = round(v / i, 2)
		results.append("Resistance = " + str(r))
	
	if v and r:
		i = round(v / r, 2)
		results.append("Ampage = " + str(i))		

	result = str(set(results))
	result1 = result[5:(len(result) - 2)]


	output.configure(text=(result1))

Label(window, text="Voltage").grid(row=1, column=1)
Label(window, text="Ampage").grid(row=3, column=1)
Label(window, text="Resistance").grid(row=5, column=1)
Label(window, text="Time").grid(row=7, column=1)

Label(window, text="Power").grid(row=1, column=2)
Label(window, text="Speed").grid(row=3, column=2)
Label(window, text="Distance").grid(row=5, column=2)
Label(window, text="Acceleration").grid(row=7, column=2)

Label(window, text="Force").grid(row=1, column=3)
Label(window, text="Mass").grid(row=3, column=3)
Label(window, text="Weight").grid(row=5, column=3)
Label(window, text="Gravity").grid(row=7, column=3)

voltage = Entry(window)
ampage = Entry(window)
resistance = Entry(window)
time = Entry(window)
power = Entry(window)
speed = Entry(window)
distance = Entry(window)
acceleration = Entry(window)
force = Entry(window)
mass = Entry(window)
weight = Entry(window)
gravity = Entry(window)

voltage.grid(row=2, column=1)
ampage.grid(row=4, column=1)
resistance.grid(row=6, column=1)
time.grid(row=8, column=1)

power.grid(row=2, column=2)
speed.grid(row=4, column=2)
distance.grid(row=6, column=2)
acceleration.grid(row=8, column=2)

force.grid(row=2, column=3)
mass.grid(row=4, column=3)
weight.grid(row=6, column=3)
gravity.grid(row=8, column=3)

button = Button(window, text="Get Answers", command=click)
button.grid(row=9, column=2)

output = Label(window, text="")

output.grid(row=10, column=2)


window.mainloop()