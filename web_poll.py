import pollavg as p
import os
import colorama
from colorama import Fore, Back, Style
import operator
import itertools
import datetime
from pathlib import Path

colorama.init()

def routine(str):
    style = Back.BLUE + Fore.WHITE
    print(style + 'ROUTINE: ' + str + Style.RESET_ALL)

if os.path.exists("index.html"):
    routine('DELETING OLD INDEX.HTML...')
    os.remove("index.html")
    
if os.path.exists("archive-"+str(datetime.datetime.today().strftime('%Y-%m-%d'))+".html"):
    routine('DELETING OLD ARCHIVE COPY FROM TODAY...')
    os.remove("./archive/archive-"+str(datetime.datetime.today().strftime('%Y-%m-%d'))+".html")

routine('CREATING NEW INDEX.HTML...')
routine('CREATING ARCHIVE COPY...')

f = open("index.html","w+")
f2 = open(Path("./archive/archive-"+str(datetime.datetime.today().strftime('%Y-%m-%d')+".html")),"w+")

routine('FILLING WITH POLLING DATA...')

#
# HTML PAGE BEGINS HERE
#

routine('GRABBING BOOTSTRAP RESOURCES...')
bootstrap = (
        '\n<meta charset="UTF-8">'
        '\n<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">'
        '\n<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">'
        '\n<script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0/dist/Chart.min.js"></script>'
        '\n<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>'
        '\n<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>'
        '\n<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>'
        '\n<script>'
        '\nfunction getRandomColor() {'
            '\nvar letters = "0123456789ABCDEF";'
            '\nvar color = "#";'
            '\nfor (var i = 0; i < 6; i++) {'
                '\ncolor += letters[Math.floor(Math.random() * 16)];'
            '\n}'
            '\nreturn color;'
        '\n}'
        '\n</script>'
        '\n<script src="./assets/darkmode.js"></script>'
)

top = ""
bot = ""
pollslist = ""

battles = ""

frontRunners = p.frontRunners
everyoneElse = p.everyoneElse
vsTrump = p.gen_polling
routine('DEBUG: FRONT RUNNERS IS ' + str(frontRunners))
routine('DEBUG: EVERYONE ELSE IS ' + str(everyoneElse))

for key, value in frontRunners:
    top += (
        "\n<div class='col-md-3 text-center'><img src='./portraits/"+str(key)+".png' style='width:70%'><h4 class='display-4'>"+str(key)+"<br/><span class='badge badge-success'>"+str(value)+"%</span></h4></div>"
    )
    
for key, value in everyoneElse:
    bot += (
        "\n<div class='col-md-2 text-center'><p class='h4'>"+str(key)+"<br/><span class='badge badge-primary'>"+str(value)+"%</span></p></div>"
    )
    
for person, polling in vsTrump.items():
    for px in polling:
        if(px > polling[px]):
            battles += "\n<table style='text-align:center'><tr><td style='width:45%'><img src='./portraits/"+person+".png' style='width:33%'></td><td><img src='./assets/vs.png' style='width:80%'></td><td style='width:45%'><img src='./portraits/Trump_sad.png' style='width:33%'></td></tr><tr><td><h4 class='display-4'><span class='badge badge-primary'>"+str(px)+"%</span></h4></td><td><p class='display-4' style='font-size:200%;'>"+person+" <span class='text-primary'>+"+str(px - polling[px])+"</span></p></td><td><h4 class='display-4'><span class='badge badge-danger'>"+str(polling[px])+"%</span></h4></td></tr>\n</table><br/>"
            
        if(px == polling[px]):
            battles += "\n<table style='text-align:center'><tr><td style='width:45%'><img src='./portraits/"+person+".png' style='width:33%'></td><td><img src='./assets/vs.png' style='width:80%'></td><td style='width:45%'><img src='./portraits/Trump_sad.png' style='width:33%'></td></tr><tr><td><h4 class='display-4'><span class='badge badge-primary'>"+str(px)+"%</span></h4></td><td><p class='display-4' style='font-size:200%;'>"+person+" "+str("EVEN.")+"</p></td><td><h4 class='display-4'><span class='badge badge-danger'>"+str(polling[px])+"%</span></h4></td></tr>\n</table><br/>"

        if(px < polling[px]):
            battles += "\n<table style='text-align:center'><tr><td style='width:45%'><img src='./portraits/"+person+".png' style='width:33%'></td><td><img src='./assets/vs.png' style='width:80%'></td><td style='width:45%'><img src='./portraits/Trump_happy.png' style='width:33%'></td></tr><tr><td><h4 class='display-4'><span class='badge badge-primary'>"+str(px)+"%</span></h4></td><td><p class='display-4' style='font-size:200%;'>Trump <span class='text-danger'>+"+str(polling[px] - px)+"</span></h4></td><td><h4 class='display-4'><span class='badge badge-danger'>"+str(polling[px])+"%</span></p></td></tr>\n</table><br/>"

for p2 in p.allpolling:
    pollslist += p2.replace(":","<th scope='col' class='lead'>").replace(r";","</th>")
    
title = "Pixel Politics"
labels = ""

for guy, data in p.pd_corr.items():
    for d in data:
        labels += (
            "\n{"
                "\nlabel: '"+guy.replace("'","")+"',"
                "\nborderColor: getRandomColor(),"
                "\nbackgroundColor: getRandomColor(),"
                "\ndata: [{x:"+str(data[d])+",y:"+str(d)+"}]"
            "\n},"
        )

#chart = (
#    "\n<script>\n"
#    "var scatterChartData = {\n"
#        "datasets: ["+labels+"]\n"
#    "};\n"
#    "window.onload = function() {\n"
#        "var ctx = document.getElementById('mcanvas');\n"
#        "window.myScatter = Chart.Scatter(ctx, {\n"
#            "data: scatterChartData,\n"
#            "options: { title: { display: false }, scales: {xAxes:[{display:true,scaleLabel:{display:true,labelString:'Days'}}],yAxes:[{display:true,scaleLabel:{display:true,labelString:'Percent (%)'}}]}}\n"
#        "});\n"
#    "};\n"
#    "</script>\n"
#)

n_p = p.n_polls
html = (
        "<html>"
        "\n<head><title>"+title+"</title>" + bootstrap + "</head>"
        "\n<body>"
        "\n<div id='top' class='position-relative overflow-hidden mb-5 pb-3 justify-center text-center bg-light'>"
        "\n<div class='col-md-8 p-lg-8 mx-auto my-5'>"
        "\n<h1 class='display-4 font-italic'><img src='./assets/logo.png' style='width:45%;'><br/>2020 Democratic Primary Datasheet</h1>"
        "\n<p class='lead my-3'>Below is the polling data pulled from FiveThirtyEight and <i>averaged</i> over the last <b>"+str(n_p)+"</b> polls from approved pollsters (see below).</p>"
        "\n<p class='lead my-3'>The top four are the current front runners, always sorted dynamically, and thus given the most attention in the design.</p>"
	    "\n<p class='lead my-3'>To regenerate this data, re-run: <code>python web_poll.py</code>"
        "\n<p><span class='badge badge-success'>This data snapshot was created on: "+str(datetime.datetime.now())+"</span></p>"
        "\n<p><a class='btn btn-outline-dark btn-large' href='https://github.com/fivethirtyeight/data/tree/master/polls'>See FiveThirtyEight's data</a> "
        "<button class='btn btn-outline-dark btn-large' onClick='lightsOut()' id='lights'>Lights Out!</button></p>"
        "\n</div>"
        "\n</div>"
    
        "\n<div class='container'><main role='main'>"
    
        "<div class='jumbotron'>"
        "\n<h1 class='display-4 font-italic'>The Front Runners</h1>"
        "\n<p class='lead'>This is how the current "+str(len(frontRunners))+" front runners are polling. They're given the most attention in the datasheet.</p>"
        "\n<hr class='my-4'/>"
        "<p>"
        "\n<div class='row justify-content-md-center'>" + top + "</div><br/>"
        "</p>"
    
        "\n<h1 class='display-4 font-italic'>...and everyone else.</h1>"
        "\n<p class='lead'>Every other current candidate that hasn't been disqualified debates gets some love, too. Here are their numbers. This is sorted dynamically and any one of these candidates can jump up to frontrunner status.</p>"
        "\n<hr class='my-4'/>"
        "\n<div class='row justify-content-md-center'>" + bot + "</div>"
        "</p>"
        "</div>"
        
        #"<div class='jumbotron'>"
        #"\n<h1 class='display-4 font-italic'>Polling vs. Time in Polls</h1><br/>"
        #"\n<p class='lead'>The data plots a candidate's time in the polls vs their polling, and suggests that candidates poll better when they've been in the polls for a longer amount of time (i.e. they're known better).</p>"
        #"\n<hr class='my-4'/>"
        #"<p>"
        #"\n" + chart + ""
        #"\n<div class='chart-container' style='position: relative; height:50vh; width:50vw'><canvas id='mcanvas'></canvas></div>"
        #"</p>"
        #"</div>"
    
        "<div class='jumbotron'>"
        "\n<h1 class='display-4 font-italic'>The <span class='text-primary'>Front Runners</span> Vs. <span class='text-danger'>Donald J. Trump</span></h1><br/>"
        "\n<p class='lead'>Here's how the current "+str(len(frontRunners))+" frontrunners poll against their likely opponent in the general election, President Donald J. Trump.</p>"
        "\n<hr class='my-4'/>"
        "\n<p>"
        "\n" + battles + ""
        "\n</p>"
        "</div>"
    
        "<div class='jumbotron'>"
        "\n<h1 class='display-4 font-italic'>Individual Polls</h1><br/>"
        "\n<p class='lead'>Lastly, individual Democratic Primary polls for the 2020 cycle, sorted by the last "+str(p.n_polls)+" polls from approved pollsters.<br/><b>Approved polls are:</b> " + str((', ').join(p.approved)) + "</p>"
        "\n<hr class='my-4'/>"
        "<p>"
        "\n<table class='table'>"
        "\n<thead><tr><th>Pollster</th><th>Date Conducted</th><th>Answer</th><th>Percent (%)</th><th>Result</th></tr></thead>"
        "\n<tbody>"
        "\n" + pollslist + ""
        "\n</tbody>"
        "\n</table>"
        "</p>"
        "\n</main></div>"
        "</div>"
    
        "\n<br/>"
        "\n</body>"
        "\n</html>"
)

# 
# HTML PAGE ENDS HERE
#

f.write(html)
f2.write(html)

f.close
f2.close
routine('SUCCESS.')
