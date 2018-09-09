import subprocess
from flask import Flask, request, render_template

app = Flask(__name__)

tele = subprocess.check_output("python3 /Users/MarcoPizarro/Desktop/Environments/instagramIngenuity/tkinterTest.py", shell=True)

print(str(tele))

#ipq
origin = subprocess.check_output("cd /Users/MarcoPizarro/Desktop/Environments/instagramIngenuity/bin; source activate; cd -; python -m scripts.label_image --graph=tf_files/retrained_graph.pb --image={link}".format(link=tele), shell=True)
hello = origin.decode("utf-8")
newdata = hello[:0] + hello[60:]
ipq = newdata[:1] + newdata[2:]
ipq = int(ipq)

#contrast
origin = subprocess.check_output("cd /Users/MarcoPizarro/Desktop/Environments/instagramIngenuity/bin; source activate; cd -; cd contrast ;python -m scripts.label_image --graph=tf_files/retrained_graph.pb --image={link}".format(link=tele), shell=True)
hello = origin.decode("utf-8")
newdata = hello[:0] + hello[60:]
contrast = newdata[:len(newdata)-10] + newdata[len(newdata):]
contrastP = 1 if contrast=="high" else 0

#colorStatus
origin = subprocess.check_output("cd /Users/MarcoPizarro/Desktop/Environments/instagramIngenuity/bin; source activate; cd -; cd colorStatus ;python -m scripts.label_image --graph=tf_files/retrained_graph.pb --image={link}".format(link=tele), shell=True)
hello = origin.decode("utf-8")
newdata = hello[:0] + hello[60:]
colorStatus = newdata[:len(newdata)-1] + newdata[len(newdata):]
colorStatus = str(colorStatus)
colorStatusP = 1 if colorStatus=="color" else 0

#type
origin = subprocess.check_output("cd /Users/MarcoPizarro/Desktop/Environments/instagramIngenuity/bin; source activate; cd -; cd type ;python -m scripts.label_image --graph=tf_files/retrained_graph.pb --image={link}".format(link=tele), shell=True)
hello = origin.decode("utf-8")
newdata = hello[:0] + hello[60:]
type = newdata[:len(newdata)-1] + newdata[len(newdata):]
if type=="portrait":
    type = 0
if type=="landscape":
    type = 1
if type=="selfie":
    type = 2
if type=="other":
    type = 3

tele = tele[:len(tele)-1] + tele[len(tele):]

print(type, ipq, colorStatusP, contrastP, tele)
@app.route('/')
def output():
	return render_template("results.html", ipq=ipq, contrast=contrastP, colorStatus=colorStatusP, type=type, tele=str(tele))

app.run()
