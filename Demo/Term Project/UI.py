#Run functions for tkinter
from elements import *

# Basic Animation Framework
#Animation framework recieved from: http://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    data.mode="Title"
    data.title=PhotoImage(file='title.gif') #https://studyib.net/physics
    data.ionic=PhotoImage(file='ionic.gif') #https://www.wikipedia.org/
    data.ionicBackground=PhotoImage(file='ionicBackground.gif') #https://www.wikipedia.org/
    data.covalent=PhotoImage(file='covalent.gif') #https://www.wikipedia.org/
    data.covalentBackground=PhotoImage(file='covalentBackground.gif') #https://www.bioanalysis-zone.com/category/articles/spotlights/lmspotlight/
    data.errorBackground=PhotoImage(file='error.gif') #https://www.wikipedia.org/
    data.demoBackground=PhotoImage(file='demo.gif') #https://www.wikipedia.org/
    data.bonusBackground=PhotoImage(file='bonus.gif') #https://www.cmu.edu
    data.text=['','','','','']
    data.boxes=[False,False,False,False,False]
    data.activeLower=False
    data.display=canvas(background=vector(0.25,0.25,0.25))
    data.error=False
    data.currentCompound=None
    data.isData=False
    data.bonus=False

def mousePressed(event, data):
    # use event.x and event.y
    if data.error:
        if not (event.x>100 and event.x<425 and event.y>390 and event.y<460):
            return
        data.error=False
        return
    if data.mode=='Title':
        titleMousePressed(event,data)
    elif data.mode=='Selection':
        selectionMousePressed(event,data)
    elif data.mode=='Instruction':
        instructionMousePressed(event,data)
    elif data.mode=='Ionic':
        ionicMousePressed(event,data)
    elif data.mode=='Covalent':
        covalentMousePressed(event,data)
    elif data.mode=='Data':
        dataMousePressed(event,data)
        
def titleMousePressed(event,data):
    if event.x>175 and event.x<325 and event.y>425 and event.y<475:
        data.mode='Selection'

def selectionMousePressed(event,data):
    if event.x>24 and event.x<240 and event.y>65 and event.y<350:
        data.mode='Ionic'
    elif event.x>260 and event.x<476 and event.y>65 and event.y<350:
        data.mode='Covalent'
    elif event.x>100 and event.x<425 and event.y>390 and event.y<460:
        data.mode='Instruction'

def instructionMousePressed(event,data):
    if event.x>100 and event.x<425 and event.y>390 and event.y<460:
        if data.isData:
            data.isData=False
            data.bonus=False
            return
        data.mode='Selection'
        data.currentCompound=None
        data.text[0]=''
    elif event.x>50 and event.x<230 and event.y>43 and event.y<137-32.5:
        data.text[0]='CH3%CH2%CH3'
        drawCovalentCompound(data)
    elif event.x>270 and event.x<450 and event.y>43 and event.y<137-32.5:
        data.text[0]='CH3%COH'
        drawCovalentCompound(data)
    elif event.x>50 and event.x<230 and event.y>137+32.5 and event.y<251-32.5:
        drawCubane(data)
        data.currentCompound=Compound('C8H8')
        data.isData=True
    elif event.x>270 and event.x<450 and event.y>137+32.5 and event.y<251-32.5:
        drawBiphenyl(data)
        data.currentCompound=Compound('C10H10')
        data.isData=True
    elif event.x>50 and event.x<230 and event.y>251+32.5 and event.y<345:
        drawFerrocene(data)
        data.currentCompound=Compound('FeC10H10')
        data.isData=True
    elif event.x>270 and event.x<450 and event.y>251+32.5 and event.y<345:
        data.currentCompound=CovalentCompound('B2H4')
        data.text[0]='BH2%BH2'
        data.isData=True
        drawCovalentCompound(data)

def drawCubane(data):
    data.display.delete()
    data.display=canvas(background=vector(0.25,0.25,0.25))
    cr=67/1.2
    hr=53
    for i in range(-1,2,2):
        for j in range(-1,2,2):
            for k in range(-1,2,2):
                sphere(pos=vector(i*cr,j*cr,k*cr),color=color.black,radius=cr*1.2)
                sphere(pos=vector(i*(cr+hr),j*(cr+hr),k*(cr+hr)),color=color.white,radius=hr)
            
def drawBenzene(data,center):
    cr=67
    hr=53
    activeMolecules=[]
    for i in range(6):
        activeMolecules.append(sphere(pos=vector(center[0]+1.2*cr*math.cos(i*2*math.pi/6),center[1]+1.2*cr*math.sin(i*2*math.pi/6),0),radius=cr,color=color.black))
        if (i==0 and center[0]<0) or (i==3 and center[0]>0):
            continue
        activeMolecules.append(sphere(pos=vector(center[0]+(1.2*cr+hr*1.5)*math.cos(i*2*math.pi/6),center[1]+(1.2*cr+hr*1.5)*math.sin(i*2*math.pi/6),0),radius=hr,color=color.white))
    if center[0]<0:
        for atom in activeMolecules:
            atom.rotate(origin=vector(center[0],center[1],center[2]),axis=vector(1,0,0),angle=math.pi/2)

def drawBiphenyl(data):
    data.display.delete()
    data.display=canvas(background=vector(0.25,0.25,0.25))
    for i in range(-1,2,2):
        drawBenzene(data,((67+(3**0.5)/2*67)*i,0,0))

def drawFerrocene(data):
    data.display.delete()
    data.display=canvas(background=vector(0.25,0.25,0.25))
    cr=67*1.2
    hr=53*1.5
    ironAtom=elementPicker('Fe')
    sphere(pos=vector(0,0,0),radius=ironAtom.size,color=ironAtom.color)
    for i in range(-1,2,2):
        for j in range(5):
            if i==1:
                j+=0.5
            sphere(pos=vector(cr*math.cos(j*2*math.pi/5),cr*math.sin(j*2*math.pi/5),1.2*ironAtom.size*i),radius=cr/1.2,color=color.black)
            sphere(pos=vector((hr+cr)*math.cos(j*2*math.pi/5),(hr+cr)*math.sin(j*2*math.pi/5),1.2*ironAtom.size*i),radius=hr/1.5,color=color.white)

def ionicMousePressed(event,data):
    if data.activeLower:
        if event.x>50 and event.x<110 and event.y>250 and event.y<300 :
            data.boxes=[False,True,False,False,False]
        elif event.x>125 and event.x<175 and event.y>225 and event.y<275:
            data.boxes=[False,False,True,False,False]
        elif event.x>250 and event.x<310 and event.y>250 and event.y<300:
            data.boxes=[False,False,False,True,False]
        elif event.x>325 and event.x<375 and event.y>225 and event.y<275:
            data.boxes=[False,False,False,False,True]
        else:
            data.boxes=[False,False,False,False,False]
    if event.x>100 and event.x<425 and event.y>390 and event.y<460:
        if data.isData:
            data.isData=False
            data.bonus=False
            return
        data.mode='Selection'
        data.currentCompound=None
        data.activeLower=False
        data.boxes=[False,False,False,False,False]
        data.text=['','','','','']
    elif event.x>50 and event.x<375 and event.y>250 and event.y<300:
        data.activeLower=True
        data.boxes[0]=False
    elif event.x>50 and event.x<375 and event.y>100 and event.y<150:
        data.activeLower=False
        data.boxes[0]=True
    elif event.x>400 and event.x<450 and event.y>100 and event.y<150:
        drawIonicCompound(data)
    elif event.x>400 and event.x<450 and event.y>250 and event.y<300:
        drawIonsToFormula(data)

def drawIonicCompound(data):
    data.display.delete()
    data.display=canvas(background=vector(0.25,0.25,0.25))
    try:
        currentCompound=IonicCompound(None,data.text[0])
        currentCompound.draw()
        data.currentCompound=currentCompound
        data.isData=True
        if 'Cn' in currentCompound.formula:
            data.bonus=True
    except:
        data.error=True

def drawIonsToFormula(data):
    data.display.delete()
    data.display=canvas(background=vector(0.25,0.25,0.25))
    try:
        cation=elementPicker(data.text[1]).ionize(int(data.text[2]))
        anion=elementPicker(data.text[3]).ionize(-int(data.text[4]))
        currentCompound=IonicCompound([cation,anion],None)
        currentCompound.draw()
        data.currentCompound=currentCompound
        if 'Cn' in currentCompound.formula:
            data.bonus=True
        data.isData=True
    except:
        data.error=True
        
def drawCovalentCompound(data):
    data.display.delete()
    data.display=canvas(background=vector(0.25,0.25,0.25))
    try:
        currentAtoms=[]
        compound=CovalentCompound(data.text[0])
        compound.draw()
        data.currentCompound=compound
        if 'Cn' in compound.formula:
            data.bonus=True
        data.isData=True
    except:
        data.error=True
        
def covalentMousePressed(event,data):
    if event.x>100 and event.x<425 and event.y>390 and event.y<460:
        if data.isData:
            data.isData=False
            data.bonus=False
            return
        data.mode='Selection'
        data.currentCompound=None
        data.text[0]=''
        data.boxes[0]=False
    elif event.x>50 and event.x<375 and event.y>75 and event.y<125:
        data.boxes[0]=True
    elif event.x>400 and event.x<450 and event.y>75 and event.y<125:
        drawCovalentCompound(data)

def keyPressed(event, data):
    # use event.char and event.keysym
    if data.isData:
        return
    if data.error:
        return
    for i in range(5):
        if data.boxes[i]:
            if event.char!='' and event.keysym!='BackSpace' and event.keysym!='Return' and event.keysym!='Tab':
                if i==0:
                    if len(data.text[0])>22 or (data.text[0].count('%')>=2 and event.char=='%'):
                        return
                elif i%2==1:
                    if len(data.text[i])>1:
                        return
                else:
                    if len(data.text[i])>0:
                        return
                data.text[i]+=event.char
            elif event.keysym=='BackSpace':
                data.text[i]=data.text[i][0:len(data.text[i])-1]
    if data.mode=='Ionic':
        ionicKeyPressed(event,data)
    elif data.mode=='Covalent':
        covalentKeyPressed(event,data)

def ionicKeyPressed(event,data):
    if data.boxes[0] and event.keysym=='Return':
        drawIonicCompound(data)
    elif True in data.boxes and event.keysym=='Return':
        drawIonsToFormula(data)
    elif True in data.boxes and event.keysym=='Tab':
        currentBox=data.boxes.index(True)
        data.boxes[currentBox]=False
        data.boxes[(currentBox+1)%5]=True
        if data.boxes[0]:
            data.activeLower=False
        else:
            data.activeLower=True

def covalentKeyPressed(event,data):
    if data.boxes[0] and event.keysym=='Return':
        drawCovalentCompound(data)

def redrawAll(canvas, data):
    # draw in canvas
    if data.error:
        canvas.create_image(250,250,image=data.errorBackground)
        canvas.create_rectangle(50,175,450,260,fill='white')
        canvas.create_text(250,200,text='Input is invalid.',font='Georgia 20')
        canvas.create_text(250,235,text='Please enter a valid compound.',font='Georgia 20')
        canvas.create_rectangle(100,390,400,460,fill='white')
        canvas.create_text(250,425,text='Back',font='Georgia 20')
        return
    if data.isData:
        dataRedrawAll(canvas,data)
        return
    if data.mode=='Title':
        titleRedrawAll(canvas,data)
    elif data.mode=='Selection':
        selectionRedrawAll(canvas,data)
    elif data.mode=='Instruction':
        instructionRedrawAll(canvas,data)
    elif data.mode=='Ionic':
        ionicRedrawAll(canvas,data)
    elif data.mode=='Covalent':
        covalentRedrawAll(canvas,data)
    elif data.mode=='Data':
        dataRedrawAll(canvas,data)
        
def dataRedrawAll(canvas,data):
    if data.bonus:
        canvas.create_image(250,250,image=data.bonusBackground)
    canvas.create_rectangle(100,390,400,460,fill='white')
    canvas.create_text(250,425,text='Back',font='Georgia 20')
    stats=calculateStats(data.currentCompound)
    font='Georgia 15'
    canvas.create_text(50,50,text='Formula: %s'%(data.currentCompound.formula),font=font, anchor=W)
    canvas.create_text(50,100,text='Molar mass: %0.3f g/mol'%(stats[0]),font=font,anchor=W)
    canvas.create_text(50,150,text='Number of valence electrons: %d'%(stats[1]),font=font,anchor=W)
    if isinstance(data.currentCompound,IonicCompound) or data.currentCompound.formula=='FeC10H10':
        canvas.create_text(50,200,text='Binding energy: %0.2f kJ/mol'%(stats[2]),font=font,anchor=W)
        canvas.create_text(50,250,text='Average bond length: %d pm'%(stats[5]),font=font,anchor=W)
        canvas.create_text(50,300,text='Name: %s'%stats[6],font=font,anchor=W)
        canvas.create_text(50,350,text="Water soluble: %s" %stats[7],font=font,anchor=W)
    else:
        canvas.create_text(50,200,text='Can form hydrogen bonds: %s' %(stats[3]), font=font,anchor=W)
        canvas.create_text(50,250,text='Hybridization of central atoms:', font=font, anchor=W)
        canvas.create_text(250,300,text=str(stats[4]),font=font)
    
def titleRedrawAll(canvas,data):
    canvas.create_image(data.width/2,data.height/2,image=data.title)
    canvas.create_rectangle(1,25,499,75,fill='white')
    canvas.create_text(250,50,text='15-112 3D Molecule Viewer',font='Georgia 30')
    canvas.create_rectangle(175,425,325,475,fill='white')
    canvas.create_text(250,450,text='Start',font='Georgia 25')
    
def selectionRedrawAll(canvas,data):
    canvas.create_text(250,25,text='Select a type of molecule',font='Georgia 30')
    canvas.create_rectangle(24,65,240,350)
    canvas.create_rectangle(500-24,65,500-240,350)
    canvas.create_image(data.width/4,180,image=data.ionic)
    canvas.create_text(125,315,text='Ionic',font='Georgia 20')
    canvas.create_image(data.width/4*3,180,image=data.covalent)
    canvas.create_text(375,315,text='Covalent',font='Georgia 20')
    canvas.create_rectangle(100,390,400,460)
    canvas.create_text(250,425,text='Sample Molecules',font='Georgia 20')
    
def instructionRedrawAll(canvas,data):
    canvas.create_image(250,250,image=data.demoBackground)
    canvas.create_rectangle(100,390,400,460,fill='white')
    canvas.create_text(250,425,text='Back',font='Georgia 20')
    canvas.create_rectangle(50,43,230,137-32.5,fill='white')
    canvas.create_text((50+230)/2,(23+137-12.5)/2,text='Propane',font='Georgia 20')
    canvas.create_rectangle(270,43,450,137-32.5,fill='white')
    canvas.create_text((270+450)/2,(23+137-12.5)/2,text='Acetaldehyde',font='Georgia 20')
    canvas.create_rectangle(50,137+32.5,230,251-32.5,fill='white')
    canvas.create_text((50+230)/2,(137+12.5+251-12.5)/2,text='Cubane',font='Georgia 20')
    canvas.create_rectangle(270,137+32.5,450,251-32.5,fill='white')
    canvas.create_text((270+450)/2,(137+12.5+251-12.5)/2,text='Biphenyl',font='Georgia 20')
    canvas.create_rectangle(50,251+32.5,230,345,fill='white')
    canvas.create_text((50+230)/2,(251+12.5+365)/2,text='Ferrocene',font='Georgia 20')
    canvas.create_rectangle(270,251+32.5,450,345,fill='white')
    canvas.create_text((270+450)/2,(251+12.5+365)/2,text='Boranylborane',font='Georgia 18')
    
def ionicRedrawAll(canvas,data):
    canvas.create_image(250,250,image=data.ionicBackground)
    canvas.create_rectangle(100,390,400,460,fill='white')
    canvas.create_text(250,425,text='Back',font='Georgia 20')
    if data.boxes[0]:
        canvas.create_rectangle(50,100,375,150,fill='lightslategray')
        canvas.create_text((50+375)/2,125,text=data.text[0],font='Georgia 15')
    else:
        canvas.create_rectangle(50,100,375,150,fill='white')
    if data.activeLower:
        if data.boxes[1]:
            canvas.create_rectangle(50,250,110,300,fill='lightslategray')
        else:
            canvas.create_rectangle(50,250,110,300,fill='white')
        if data.boxes[2]:
            canvas.create_rectangle(125,225,175,275,fill='lightslategray')
        else:    
            canvas.create_rectangle(125,225,175,275,fill='white')
        canvas.create_text(163,243,text='+',font='Georgia 18')
        canvas.create_text((175+250)/2,275,text='+',font='Georgia 20')
        if data.boxes[3]:
            canvas.create_rectangle(250,250,310,300,fill='lightslategray')
        else:
            canvas.create_rectangle(250,250,310,300,fill='white')
        if data.boxes[4]:
            canvas.create_rectangle(325,225,375,275,fill='lightslategray')
        else:
            canvas.create_rectangle(325,225,375,275,fill='white')
        canvas.create_text(363,240,text='_')
        canvas.create_text(80,275,text=data.text[1],font='Georgia 15')
        canvas.create_text(150-6,250,text=data.text[2],font='Georgia 15')
        canvas.create_text(280,275,text=data.text[3],font='Georgia 15')
        canvas.create_text(350-6,250,text=data.text[4],font='Georgia 15')
    canvas.create_rectangle(400,100,450,150,fill='seagreen')
    canvas.create_rectangle(400,250,450,300,fill='seagreen')
    canvas.create_text(425,125,text='Draw',font='Georgia 15')
    canvas.create_text(425,275,text='Draw',font='Georgia 15')
    
    if data.boxes[0]==False:   
        canvas.create_text(200,125,text='Enter Formula',font='Georgia 20')
    if not data.activeLower:
        canvas.create_rectangle(50,250,375,300,fill='white')
        canvas.create_text(200,275,text='Enter Ions       ',font='Georgia 20')
    
def covalentRedrawAll(canvas,data):
    canvas.create_image(250,250,image=data.covalentBackground)
    canvas.create_rectangle(100,390,400,460,fill='white')
    canvas.create_text(250,425,text='Back',font='Georgia 20')
    if data.boxes[0]:
        canvas.create_rectangle(50,75,375,125,fill='lightslategray')
        canvas.create_text((50+375)/2,100,text=data.text[0],font='Georgia 15')
    else:
        canvas.create_rectangle(50,75,375,125,fill='white')
        canvas.create_text(200,100,text='Enter Formula',font='Georgia 20')
    canvas.create_rectangle(400,75,450,125,fill='seagreen')
    canvas.create_text(425,100,text='Draw',font='Georgia 15')
    canvas.create_rectangle(50,250-75/2,450,250+75/2,fill='white')
    canvas.create_text(250,250,text="Note: Seperate chemical groups with a '%'.\n For example, enter ethane as CH3%CH3",font='Georgia 15')

####################################
# use the run function as-is
####################################
#15112 run function from http://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")