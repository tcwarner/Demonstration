#Data for elements, compounds, and what is displayed in vpython

import copy
import fractions
import math
import time
from vpython import*

class Element:
    def __init__(self,symbol,name,position,en,mass,number,valence,oxidations,metal,size,color=vector(0.5,0.5,0.5)):
        self.symbol=symbol
        self.name=name
        self.position=position
        self.en=en
        self.mass=mass
        self.number=number
        self.valence=valence
        self.oxidations=oxidations
        self.metal=metal
        self.size=size
        self.charge=0
        self.color=color
    def __repr__(self):
        return self.name
    def ionize(self,new,forced=False):
        oldCharge=self.charge
        if new not in self.oxidations or forced:
            return "Invalid Ion"
        if self.valence-new==0 and new>0:
            self.size/=3
        elif self.valence==0 and new<=0:
            self.size*=3
            
        if new==0:
            #self.__class__=Element
            self.charge=0
            self.valence+=oldCharge-new
            return Element(self.symbol,self.name,self.position,self.en,self.mass,self.number,self.valence,self.oxidations,self.metal,self.size,self.color)
        else:
            self.charge=new
            self.valence-=self.charge
            #self.__class__=Ion
            return Ion(self.symbol,self.name,self.position,self.en,self.mass,self.number,self.valence,self.oxidations,self.metal,self.charge,self.size,self.color)
    def getHashables(self):
        return (self.symbol,self.name,self.position,self.en,self.mass,self.number,self.valence,self.oxidations,self.metal)
    def __hash__(self):
        return hash(self.getHashables())
    def __eq__(self,other):
        return str(self)==str(other)
 
class Ion(Element):
    def __init__(self,symbol,name,position,en,mass,number,valence,oxidations,metal,charge,size,color=vector(0.5,0.5,0.5)):
        super().__init__(symbol,name,position,en,mass,number,valence,oxidations,metal,size,color)
        self.charge=charge
        if self.charge==0:
            self=Element(self.symbol,self.name,self.position,self.en,self.mass,self.number,self.valence,self.oxidations,self.metal,self.size)
    def __repr__(self):
        if self.charge>0:
            sign='+'
        else:
            sign='-'
        return '%s: %d%s' %(self.name,abs(self.charge),sign)

def elementPicker(element): #avoids globals and aliasing   
    H=Element('H','Hydrogen',(1,1),2.20,1.008,1,1,(0,1),"Non Metal",53,color.white)
    He=Element('He','Helium',(1,18),0,4.0026,2,2,(0,), "Non Metal",31,color.cyan)
    Li=Element('Li','Lithium',(2,1),0.98,6.94,3,1,(0,1),"Metal",167,vector(0.8,0,0.8))
    Be=Element('Be','Berrylium',(2,2),1.57,9.012,4,2,(0,2),"Metal",112,vector(0.8,1,0.2))
    B=Element('B','Boron',(2,13),2.04,10.81,5,3,(0,3),"Metalloid",87,vector(0.5,0.5,0))
    C=Element('C','Carbon',(2,14),2.55,12.011,6,4,(0,-4,4),"Non Metal",67,color.black)
    N=Element('N','Nitrogen',(2,15),3.04,14.007,7,5,(0,-3,1,2),"Non Metal",56,color.blue)
    O=Element('O','Oxygen',(2,16),3.44,15.999,8,6,(0,-2),"Non Metal",48,color.red)
    F=Element('F','Fluorine',(2,17),3.98,18.998,9,7,(0,-1),"Non Metal",42,color.green)
    Ne=Element('Ne','Neon',(2,18),0,20.180,10,8,(0,),"Non Metal",38,color.cyan)
    Na=Element('Na','Sodium',(3,1),0.93,22.99,11,1,(0,1),'Metal',190,vector(0.8,0,0.8))
    Mg=Element('Mg','Magnesium',(3,2),1.31,24.305,12,2,(0,2),'Metal',145,vector(0.8,1,0.2))
    Al=Element('Al','Aluminium',(3,13),2.04,26.982,13,3,(0,3),'Metal',118)
    Si=Element('Si','Silicon',(3,14),2.55,28.085,14,4,(0,4,-4),'Metalloid',111)
    P=Element('P','Phosphorus',(3,15),3.04,30.974,15,5,(0,-3),'Non Metal',98,color.orange)
    S=Element('S','Sulfur',(3,16),3.44,32.06,16,6,(0,-2,6),'Non Metal',88,color.yellow)
    Cl=Element('Cl','Chlorine',(3,17),3.98,35.45,17,7,(0,-1),'Non Metal',79,vector(0,0.8,0))
    Ar=Element('Ar','Argon',(3,18),0,39.948,18,8,(0,),'Non Metal',71,color.cyan)
    K=Element('K','Potassium',(4,1),0.82,39.098,19,1,(0,1),'Metal',243,vector(0.8,0,0.8))
    Ca=Element('Ca','Calcium',(4,2),1.0,40.078,20,2,(0,2),'Metal',194,vector(0.8,1,0.2))
    Sc=Element('Sc','Scandium',(4,3),1.36,44.956,21,2,(0,1,2,3),'Metal',194)
    Ti=Element('Ti','Titanium',(4,4),1.54,47.867,22,2,(0,4),'Metal',176,vector(0.4,0.4,0.4))
    V=Element('V','Vanadium',(4,5),1.63,50.942,23,2,(0,5),'Metal',171)
    Cr=Element('Cr','Chromium',(4,6),1.66,51.996,24,1,(0,6),'Metal',166)
    Mn=Element('Mn','Manganese',(4,7),1.55,54.938,25,2,(0,2,4,7),'Metal',161)
    Fe=Element('Fe','Iron',(4,8),1.83,55.845,26,2,(0,2,3,6),'Metal',156,vector(1,0.6,0))
    Co=Element('Co','Cobalt',(4,9),1.88,58.933,27,2,(0,2,3),'Metal',152)
    Ni=Element('Ni','Nickel',(4,10),1.91,58.693,28,2,(0,2),'Metal',149)
    Cu=Element('Cu','Copper',(4,11),1.9,63.546,29,1,(0,1,2),'Metal',145)
    Zn=Element('Zn','Zinc',(4,12),1.65,65.38,30,2,(0,2),'Metal',142)
    Ga=Element('Ga','Gallium',(4,13),1.81,69.723,31,3,(0,3),'Metal',136)
    Ge=Element('Ge','Germanium',(4,14),2.01,72.63,32,4,(0,4,-4),'Metalloid',125)
    As=Element('As','Arsenic',(4,15),2.18,74.922,33,5,(0,-3,5),'Non Metal',114)
    Se=Element('Se','Selenium',(4,16),2.55,78.971,34,6,(0,-2,2,6),'Non Metal',103)
    Br=Element('Br','Bromine',(4,17),2.96,79.904,35,7,(0,-1,1),'Non Metal',94,color.magenta)
    Kr=Element('Kr','Krypton',(4,18),3.0,83.798,36,8,(0,2),'Non Metal',88,color.cyan)
    Rb=Element('Rb','Rubidium',(5,1),0.82,85.4,37,1,(0,1),'Metal',265,vector(0.8,0,0.8))
    Sr=Element('Sr','Strontium',(5,2),1,87.6,38,2,(0,2),'Metal',219,vector(0.8,1,0.2))
    Y=Element('Y','Yttrium',(5,3),1.22,88.9,39,2,(0,3),'Metal',212)
    Zr=Element('Zr','Zirconium',(5,4),1.33,91.224,40,2,(0,4),'Metal',206)
    Nb=Element('Nb','Niobium',(5,5),1.6,92.906,41,1,(0,5),'Metal',198)
    Mo=Element('Mo','Molybdenum',(5,6),2.16,95.95,42,1,(0,3,6),'Metal',190)
    Tc=Element('Tc','Technetium',(5,7),1.9,98,43,2,(0,4,7),'Metal',183)
    Ru=Element('Ru','Ruthenium',(5,8),2.2,101.07,44,1,(0,4),'Metal',178)
    Rh=Element('Rh','Rhodium',(5,9),2.28,102.91,45,1,(0,3),'Metal',173)
    Pd=Element('Pd','Palladium',(5,10),2.2,106.42,46,0,(0,2,4),'Metal',169)
    Ag=Element('Ag','Silver',(5,11),1.93,107.87,47,1,(0,1),'Metal',165)
    Cd=Element('Cd','Cadmium',(5,12),1.69,112.41,48,2,(0,2),'Metal',161)
    In=Element('In','Indium',(5,13),1.78,114.82,49,3,(0,3),'Metal',156)
    Sn=Element('Sn','Tin',(5,14),1.96,118.71,50,4,(0,4,-4,2),'Metal',145)
    Sb=Element('Sb','Antimony',(5,15),2.05,121.76,51,5,(0,-3,3,5),'Metalloid',133)
    Te=Element('Te','Tellurium',(5,16),2.1,127.6,52,6,(0,-2,2,4,6),'Metalloid',123)
    I=Element('I','Iodine',(5,17),2.66,126.904,53,7,(0,-1,1,3,5,7),'Non Metal',115,vector(0.6,0.2,1))
    Xe=Element('Xe','Xenon',(5,18),2.6,131.293,54,8,(0,2,4,6),'Non Metal',108,color.cyan)
    Cs=Element('Cs','Caesium',(6,1),0.79,132.9,55,1,(0,1),'Metal',298,vector(0.8,0,0.8))
    Ba=Element('Ba','Barium',(6,2),0.89,137.3,56,2,(0,2),'Metal',253,vector(0.8,1,0.2))
    La=Element('La','Lanthanum',(6,3),1.10,138.91,57,2,(0,1,2,3),'Metal',250)
    Ce=Element('Ce','Cerium',(6,1,False),1.12,140.12,58,2,(0,2,3,4),'Metal',250)
    Pr=Element('Pr','Praesodymium',(6,2,False),1.13,140.91,59,2,(0,2,3,4,5),'Metal',247)
    Nd=Element('Nd','Neodymium',(6,3,False),1.14,144.24,60,2,(0,2,3,4),'Metal',206)
    Pm=Element('Pm','Promethium',(6,4,False),0,145,61,2,(0,2,3),'Metal',205)
    Sm=Element('Sm','Samarium',(6,5,False),1.17,150.36,62,2,(0,2,3),'Metal',238)
    Eu=Element('Eu','Europium',(6,6,False),0,151.96,63,2,(0,2,3),'Metal',231)
    Gd=Element('Gd','Gadolinium',(6,7,False),1.2,157.25,64,2,(0,1,2,3),'Metal',233)
    Tb=Element('Tb','Terbium',(6,8,False),0,158.93,65,2,(0,1,2,3,4),'Metal',225)
    Dy=Element('Dy','Dysprosium',(6,9,False),1.22,162.5,66,2,(0,2,3,4),'Metal',228)
    Ho=Element('Ho','Holmium',(6,10,False),1.23,164.93,67,2,(0,2,3),'Metal',226)
    Er=Element('Er','Erbium',(6,11,False),1.24,167.26,68,2,(0,2,3),'Metal',226)
    Tm=Element('Tm','Thulium',(6,12,False),1.25,168.93,69,2,(0,2,3),'Metal',222)
    Yb=Element('Yb','Yitterbium',(6,13,False),0,173.05,70,2,(0,2,3),'Metal',222)
    Lu=Element('Lu','Lutetium',(6,14,False),1.27,174.97,71,2,(0,2,3),'Metal',217)
    Hf=Element('Hf','Halfnium',(6,4),1.3,178.49,72,2,(0,1,2,3,4),'Metal',208)
    Ta=Element('Ta','Tantalum',(6,5),1.5,180.95,73,2,(0,1,2,3,4,5),'Metal',200)
    W=Element('W','Tungsten',(6,6),2.36,183.84,74,2,(0,1,2,3,4,5,6,-4),'Metal',193)
    Re=Element('Re','Rhenium',(6,7),1.9,186.21,75,2,(0,1,2,3,4,5,6,7),'Metal',188)
    Os=Element('Os','Osmium',(6,8),2.2,190.23,76,2,(0,1,2,3,4,5,6,7,8,-4),'Metal',185)
    Ir=Element('Ir','Iridium',(6,9),2.2,192.22,77,2,(0,1,2,3,4,5,6,7,8,9,-3),'Metal',180)
    Pt=Element('Pt','Platinum',(6,10),2.28,195.08,78,2,(0,2,4),'Metal',177)
    Au=Element('Au','Gold',(6,11),2.54,196.97,79,1,(0,3,5),'Metal',174)
    Hg=Element('Hg','Mercury',(6,12),2,200.59,80,2,(0,1,2),'Metal',171)
    Tl=Element('Tl','Thallium',(6,13),1.62,204.38,81,3,(0,1,3,-5),'Metal',156)
    Pb=Element('Pb','Lead',(6,14),2.33,207.2,82,4,(0,1,2,4),'Metal',154)
    Bi=Element('Bi','Bismuth',(6,15),2.02,208.98,83,5,(0,-3,1,3),'Metal',143)
    Po=Element('Po','Polonium',(6,16),2,209,84,6,(0,-2,2,4),'Metal',135)
    At=Element('As','Astatine',(6,17),2.2,210,85,7,(0,-1,1,5,3),'Metalloid',127)
    Rn=Element('Rn','Radon',(6,18),0,222,86,8,(2,6),'Non Metal',120,color.cyan)
    Fr=Element('Fr','Francium',(7,1),0.7,223,87,1,(0,1),'Metal',265,vector(0.8,0,0.8))
    Ra=Element('Ra','Radium',(7,2),0.9,226,88,2,(0,1,2),'Metal',215,vector(0.8,1,0.2))
    Ac=Element('Ac','Actinium',(7,3),1.1,227,89,2,(0,3),'Metal',195)
    Th=Element('Th','Thorium',(7,1,True),1.3,232.04,90,2,(0,1,2,3,4),'Metal',180)
    Pa=Element('Pa','Protactinium',(7,2,True),1.5,231.04,91,2,2,(0,3,5),'Metal',180)
    U=Element('U','Uranium',(7,3,True),1.38,238.03,92,2,(0,1,6),'Metal',175)
    Np=Element('Np','Neptunium',(7,4,True),1.36,237,93,2,(0,2,5,7),'Metal',175)
    Pu=Element('Pu','Plutonium',(7,5,True),1.28,244,94,2,(0,3,4,6),'Metal',175)
    Am=Element('Am','Americium',(7,6,True),1.3,243,95,2,(0,3,7),'Metal',175)
    Cm=Element('Cm','Curium',(7,7,True),1.3,247,96,2,(0,3,6),'Metal',175)
    Bk=Element('Bk','Berkelium',(7,8,True),1.3,247,97,2,(0,3),'Metal',170)
    Cf=Element('Cf','Californium',(7,9,True),1.3,251,98,2,(0,2,3),'Metal',170)
    Es=Element('Es','Einsteinium',(7,10,True),1.3,252,99,2,(0,3,4),'Metal',170)
    Fm=Element('Fm','Fermium',(7,11,True),1.3,257,100,2,(0,2,3),'Metal',170)
    Md=Element('Md','Mendelevium',(7,12,True),1.3,258,101,2,(0,2,3),'Metal',170)
    No=Element('No','Nobelium',(7,13,True),1.3,259,102,2,(0,2),'Metal',170)
    Lr=Element('Lr','Lawrencium',(7,14,True),1.27,266,103,2,(0,3),'Metal',170)
    Rf=Element('Rf','Rutherfordium',(7,4),1.27,267,104,2,(0,4),'Metal',160)
    Db=Element('Db','Dubnium',(7,5),1.4,268,105,2,(0,5),'Metal',150)
    Sg=Element('Sg','Seaborgium',(7,6),2.56,269,106,2,(0,6),'Metal',140)
    Bh=Element('Bh','Bohrium',(7,7),1.9,270,107,2,(0,7),'Metal',140)
    Hs=Element('Hs','Hassium',(7,8),2.2,277,108,2,(0,8),'Metal',135)
    Mt=Element('Mt','Meitnerium',(7,9),2.12,278,109,2,(0,),'Metal',140)
    Ds=Element('Ds','Darmstadtium',(7,10),2.36,281,110,1,(0,),'Metal',135)
    Rg=Element('Rg','Roentgenium',(7,11),3,282,111,2,(0,),'Metal',140)
    Cn=Element('Cn','Copernicium',(7,12),2.21,285,112,2,(0,2),'Metal',160)
    Nh=Element('Nh','Nihonium',(7,13),1.5,286,113,3,(0,),'Metal',200)
    Fl=Element('Fl','Flerovium',(7,14),2.6,289,114,4,(0,),'Metal',190)
    Mc=Element('Mc','Moscovium',(7,15),2,290,115,5,(0,),'Metal',170)
    Lv=Element('Lv','Livermorium',(7,16),1.9,293,116,6,(0,),'Metal',190)
    Ts=Element('Ts','Tennessine',(7,17),2,294,117,7,(0,),'Metalloid',200)
    Og=Element('Og','Oganesson',(7,18),0,294,118,8,(0,),'Non Metal',130,color.cyan)
    
    table={'H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn','Fr','Ra','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr','Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn','Nh','Fl','Mc','Lv','Ts','Og'}
    #use eval for efficiency, but make sure it is safe
    if len(element)>2 or element not in table:
        return "Invalid element"
    return eval(element)


def findLeastEn(elements):
    least=None
    leastEn=5
    for element in elements:
        if element.name=='Hydrogen':
            continue #only 1 bond
        if least==None or element.en<leastEn:
            leastEn=element.en
            least=element
    if least==None:
        return elements
    elements.remove(least)
    return [least]+elements

def ionicBondChecker(atom1,atom2):
    if atom1.charge==0 or atom2.charge==0:
        return False
    elif atom1.charge*atom2.charge>0:
        return False
    return True
    
def ionicBondRatio(ion1,ion2):
    if ion1=='Invalid Ion' or ion2=='Invalid Ion' or not ionicBondChecker(ion1,ion2):
        return "Not possible"
    ions=ionSorter(ion1,ion2)
    cation=ions[0]
    anion=ions[1]
    ratio=-fractions.Fraction(anion.charge/cation.charge).limit_denominator()
    return([ratio,cation,anion])

def ionSorter(ion1,ion2):
    if ion1.charge>0:
        return [ion1,ion2]
    else:
        return [ion2,ion1]

class Compound:
    def __init__(self,formula):
        self.formula=formula
        self.atoms=reducedToAtoms(self.formula)
    def __repr__(self):
        return self.formula
    def atomList(self):
        return self.atoms
    def getStats(self):
        return calculateStats(self.atoms)

def findIonicFormula(atoms):
    if ionicBondRatio(atoms[0],atoms[1])=='Not possible':
        return None
    ratio=ionicBondRatio(atoms[0],atoms[1])[0]
    ions=ionSorter(atoms[0],atoms[1])
    cation=ions[0]
    anion=ions[1]

    if ratio==1:
        cationNumber=''
        anionNumber=''
    elif int(ratio)==ratio:
        cationNumber=str(ratio)
        anionNumber=''
    elif ratio<1:
        cationNumber=str(ratio.numerator)
        anionNumber=str(ratio.denominator)
    else:    
        cationNumber=str(ratio.denominator)
        anionNumber=str(ratio.numerator)
        
    if cationNumber=='1':
        cationNumber=''
    if anionNumber=='1':
        anionNumber=''
    return cation.symbol+cationNumber+anion.symbol+anionNumber
    

class CovalentCompound(Compound):
    def __init__(self,formula):
        self.groups=[]
        self.formula=''
        self.atoms=[]
        self.groupAtoms=[]
        counter=0
        maxCount=len(formula.split('%'))-1
        previous=0
        for group in formula.split('%'):
            if counter==0:
                bool1=False
            else:
                bool1=True
            if counter==maxCount:
                bool2=False
            else:
                bool2=True
            currentGroup=findCovalentGroup([reducedToAtoms(group),(bool1,bool2)],previous)
            self.groups.append([currentGroup[0],(bool1,bool2),currentGroup[1][0]])
            atomGroup=[reducedToAtoms(group),(bool1,bool2),currentGroup[1][0]]
            self.formula+=group
            self.atoms+=reducedToAtoms(group)
            counter+=1
            previous=currentGroup[1][1]
    def draw(self):
        groups=self.groups
        drawCovalentWrapper(groups)

def drawCovalentWrapper(groups,center=(0,0,0),rotation=(0,0),depth=0):
    newCenter=(0,0,0)
    again=False
    if len(groups)>=1:
        geometry=getStericGeometry(groups[0][2])
        current=[]
        for i in range(len(geometry)):
            if i>len(groups[0][0])-1:
                if depth%2==0:
                    mult=1
                else:
                    mult=-1
                if len(groups)==1:
                    r=groups[0][0][0].size*1.5
                else:
                    r=(groups[0][0][0].size+groups[1][0][0].size)/2*1.5
                newCenter=(center[0]+geometry[-1][0]*r,center[1]+mult*geometry[-1][1]*r,center[2]+geometry[-1][2]*r)
                again=True
                break
            atom=groups[0][0][i]
            if i==0:
                sizeConstant=1.8
            else:
                sizeConstant=getBondLength(groups[0][0][0],groups[0][0][i])
            r=atom.size*sizeConstant
            atom=sphere(pos=vector(center[0]+geometry[i][0]*r,center[1]+geometry[i][1]*r,center[2]+geometry[i][2]*r),radius=r/sizeConstant,color=atom.color)
            current.append(atom)
        current=rotateX(current,center,rotation[0],groups[0][2])
        current=rotateY(current,center,rotation[1],groups[0][2])
        if again and len(groups)>1:
            if depth%2==1:
                yMult=2
                xMult=-1
            else:
                yMult=1
                xMult=1
            temp=getRotation(groups[0][2])
            newRotation=(xMult*rotation[0]+temp[0],yMult*rotation[1]+temp[1])
            drawCovalentWrapper(groups[1::],newCenter,newRotation,depth+1)

def getBondLength(center,other):
    #return 1.8
    return 0.9*(center.size+other.size)/other.size
        
def rotateX(atoms,center,rotation,steric):
    center=vector(center[0],center[1],center[2])
    if steric==4:
        for atom in atoms:
            atom.rotate(origin=center,axis=vector(0,0,1),angle=rotation)
    else:
        for atom in atoms:
            atom.rotate(origin=center,axis=vector(1,0,0),angle=rotation)
    return atoms
    
def rotateY(atoms,center,rotation,steric):
    center=vector(center[0],center[1],center[2])
    for atom in atoms:
        atom.rotate(origin=center,axis=vector(0,1,0),angle=rotation)
    return atoms
        
def getRotation(geometry):
    if geometry==0:
        return(0,0)
    elif geometry==1:
        pass
    elif geometry==2:
        return(0,math.pi)
    elif geometry==3:
        return(0,math.pi)
    elif geometry==4:
        return(70.5*math.pi/180,math.pi)
    elif geometry==5:
        return(2*math.pi/6,math.pi)
    elif geometry==6:
        return(2*math.pi/8,math.pi)
    elif geometry==7:
        return(2*math.pi/10,math.pi)
    elif geometry==8:
        pass
    return((0,0,0))
        
def findCovalentGroup(atoms,n):
    sortedAtoms=findLeastEn(atoms[0])
    steric=findSteric(sortedAtoms,atoms[1],n)
    return [sortedAtoms,steric]
    
def findSteric(atoms,bools,previous):
    test1=elementPicker('C')
    test2=elementPicker('H')
    if atoms==[test1,test2]:#special case for ethyne
        return [2,2]
    maximum=atoms[0].valence
    extraBonds=0
    bonds=[]
    if bools[0]:
        extraBonds+=1
    if bools[1]:
        extraBonds+=1
    counter=0
    for atom in atoms[1:]:
        counter+=1
        if atom.name=='Hydrogen':
            bonds.append((atoms[0],atom,counter))
            continue
        while atom.valence+bonds.count((atoms[0],atom,counter))<8:
            bonds.append((atoms[0],atom,counter))
    #make a distinction between double bonds and lone pairs
    lonePairs=abs((maximum-(len(bonds)+extraBonds))/2)
    steric=len(set(bonds))+extraBonds+lonePairs
    if steric==int(steric):
        return [int(steric),0]
    else:
        return [int(steric),1]        
        
class IonicCompound(Compound):
    def __init__(self,atoms,formula):
        if formula==None:
            self.formula=findIonicFormula(atoms)
            self.atoms=ratioToIons(self.formula)[0]
            self.ratio=ratioToIons(self.formula)[1]
            self.catNumber=self.ratio.numerator
            self.anNumber=self.ratio.denominator
        else:
            self.formula=formula
            self.atoms=ratioToIons(formula)[0]
            self.ratio=ratioToIons(formula)[1]
            self.catNumber=self.ratio.numerator
            self.anNumber=self.ratio.denominator
    def draw(self):
        catSize=self.atoms[0].size
        anSize=self.atoms[-1].size
        compare=max([catSize/anSize,anSize/catSize])
        mult=1
        if compare>4:
            mult*=1.2
        for j in range(2):
            if j==1:
                mult*=-1
            for i in range(len(self.atoms)):
                fill=self.atoms[i].color
                if i<self.catNumber:
                    if self.catNumber%2!=0:
                        current=sphere(pos=vector(-catSize/1.5*mult,(i-self.catNumber//2)*2*catSize,j*(anSize+catSize)/1.1),radius=catSize,color=fill)
                    else:
                        current=sphere(pos=vector(-catSize/1.5*mult,((i+0.5)-self.catNumber//2)*2*catSize,j*(anSize+catSize)/1.1),radius=catSize,color=fill)
                else:
                    if self.anNumber%2!=0:
                        current=sphere(pos=vector(anSize/1.5*mult,(i-self.catNumber-self.anNumber//2)*2*anSize,j*(anSize+catSize)/1.1),radius=anSize,color=fill)
                    else:
                        current=sphere(pos=vector(anSize/1.5*mult,((i+0.5)-self.catNumber-self.anNumber//2)*2*anSize,j*(anSize+catSize)/1.1),radius=anSize,color=fill)
        
def reducedFormula(formula):
    reducedFormula=[]
    currentNumbers=''
    number=False
    for i in range(len(formula)):
        if formula[i].isupper():
            if currentNumbers!='':
                reducedFormula.append(currentNumbers)
                currentNumbers=''
            number=False
            if i<len(formula)-1 and formula[i+1].islower():
                reducedFormula.append(formula[i:i+2])
            else:
                reducedFormula.append(formula[i])
        if formula[i].isnumeric():
            number=True
            currentNumbers+=formula[i]
            if i==len(formula)-1:
                reducedFormula.append(currentNumbers)
    return reducedFormula
    
def reducedToAtoms(formula):
    reduced=reducedFormula(formula)
    atoms=[]
    for i in range(len(reduced)):
        if reduced[i].isalpha():
            if i<len(reduced)-1 and reduced[i+1].isnumeric():
                for j in range(int(reduced[i+1])):
                    atoms.append(elementPicker(reduced[i]))
            else:
                atoms.append(elementPicker(reduced[i]))
    return atoms

def ratioToIons(formula):
    same=False
    atomsUsed=[]
    allAtoms=reducedToAtoms(formula)
    for atom in allAtoms:
        if atom not in atomsUsed:
            atomsUsed.append(atom)
        if len(atomsUsed)>1:
            break
    if len(atomsUsed)==1:
        atomsUsed*=2
        same=True
    ratio=fractions.Fraction(allAtoms.count(atomsUsed[0])/allAtoms.count(atomsUsed[1])).limit_denominator()
    if same:
        allAtoms[0]=allAtoms[0].ionize(allAtoms[i].oxidations[1])
        allAtoms[0]=allAtoms[0].ionize(allAtoms[i].oxidations[-1])
        totalCharge=0
        for atom in allAtoms:
            totalCharge+=atom.charge
        if totalCharge!=0:
            return False
        else:
            return [allAtoms,ratio]
    for i in range(len(allAtoms)):
        if ratio!=1:
            if allAtoms[0].name==allAtoms[i].name:
                allAtoms[i]=allAtoms[i].ionize(ratio.denominator)
            else:
                allAtoms[i]=atom.ionize(-ratio.numerator)
        else:
            if allAtoms[0].name==allAtoms[i].name:
                allAtoms[i]=allAtoms[i].ionize(allAtoms[i].oxidations[1])
                if allAtoms[i].charge<0:
                    return False
            else:
                allAtoms[i]=atom.ionize(allAtoms[i].oxidations[1])
                if allAtoms[i].charge>0:
                    return False
        if allAtoms[i]=='Invalid Ion':
            return False
    totalCharge=0
    for atom in allAtoms:
        totalCharge+=atom.charge
    if totalCharge!=0:
        return False
    return (allAtoms,ratio)

def getStericGeometry(n): #hard code in all geometries
    #form: center, first bond, previous bond, all others
    #all bond lengths are 1
    if n==0:
        return [[0,0,0]]
    elif n==1:
        return [[0,0,0],
            [1,0,0]]
    elif n==2:
        return [[0,0,0],
            [-1,0,0],
            [1,0,0]]
    elif n==3:
        return [[0,0,0],
            [-0.5,(3**0.5)/2,0],
            [-0.5,-(3**0.5)/2,0],
            [1,0,0]]
    elif n==4:
        return [[0,0,0],
            [-0.94/2,-0.33,-0.94*(3**0.5)/2],
            [-0.94/2,-0.33,0.94*(3**0.5)/2],
            [0,1,0],
            [0.94,-0.33,0]]
    elif n==5:
        return [[0,0,0],
            [0,1,0],
            [0,-0.5,(3**0.5)/2],
            [0,-0.5,-(3**0.5)/2],
            [-1,0,0],
            [1,0,0]]
    elif n==6:
        return [[0,0,0],
            [0,0,-1],
            [0,1,0],
            [0,-1,0],
            [0,0,1],
            [-1,0,0],
            [1,0,0]]
    elif n==7:
        return [[0,0,0],
            [0,1,0],
            [0,math.cos(2*math.pi/5),math.sin(2*math.pi/5)],
            [0,math.cos(2*2*math.pi/5),math.sin(2*2*math.pi/5)],
            [0,math.cos(3*2*math.pi/5),math.sin(3*2*math.pi/5)],
            [0,math.cos(4*2*math.pi/5),math.sin(4*2*math.pi/5)],
            [-1,0,0],
            [1,0,0]]
    elif n==8:
        return [[0,0,0],
            [1/(3**0.5),1/(3**0.5),-1/(3**0.5)],
            [-1/(3**0.5),1/(3**0.5),1/(3**0.5)],
            [-1/(3**0.5),1/(3**0.5),-1/(3**0.5)],
            [0,-1/(3**0.5),(2**0.5)/(3**0.5)],
            [0,-1/(3**0.5),-(2**0.5)/(3**0.5)],
            [(2**0.5)/(3**0.5),-1/(3**0.5),0],
            [-(2**0.5)/(3**0.5),-1/(3**0.5),0],
            [1/(3**0.5),1/(3**0.5),1/(3**0.5)]]

def calculateStats(compound):
    atoms=compound.atoms
    molarMass=findMolarMass(atoms)
    totalValence=findTotalValence(atoms)
    if isinstance(atoms[0],Ion): #ionic
        ionicAttraction=findIonicAttraction(atoms)[0]
        hBondStatus='No'
        hybridizations=None
        bondLength=findIonicAttraction(atoms)[1]
        ionicName=getIonicName(compound)
        sol=isWaterSoluble(compound)
    else: #covalent
        if compound.formula=='FeC10H10': #special case: organotransition complex
            ionicAttraction=(2.31*(10**-19)*-2/(156)*6.022*(10**23))
            bondLength=156
            ionicName='Iron (II) cyclopentadienyl'
            sol='No'
        else:
            ionicAttraction=0
            bondLength=None
            ionicName=None
            sol=None
        hBondStatus=formsHydrogenBonds(compound)
        hybridizations= getHybridizations(compound)
    return [molarMass,totalValence,ionicAttraction,hBondStatus,hybridizations,bondLength,ionicName,sol]

def isWaterSoluble(compound):
    cation=compound.atoms[0]
    anion=compound.atoms[-1]
    if cation.position[1]==1:
        return 'Yes'
    if cation.name=='Silver':
        return 'No'
    if anion.name=='Fluorine':
        return 'No'
    if anion.name=='Sulfur' and cation.position[1] in range(3,13):
        return 'No'
    if anion.name=='Chlorine' or anion.name=='Iodine' or anion.name=='Bromine':
        if cation.name=='Lead' or cation.name=='Mercury':
            return 'No'
        else:
            return 'Yes'
    return 'No'

def getIonicName(compound):
    firstHalf=compound.atoms[0].name+' '
    if compound.atoms[0].position[1] in range(3,13) or (len(compound.atoms[0].position)>2 and (compound.atoms[0].position[2]==True or compound.atoms[0].position[2]==False)):
        n=getOxidationNumber(compound.atoms[0].charge)
        firstHalf=firstHalf+n+' '
    anionName=compound.atoms[-1].name
    if anionName.endswith('ium'):
        anionName=anionName.replace('ium','ide')
    elif anionName.endswith('ine'):
        anionName=anionName.replace('ine','ide')
    elif anionName=='Oxygen':
        anionName='Oxide'
    elif anionName=='Carbon':
        anionName='Carbide'
    elif anionName=='Nitrogen':
        anionName='Nitride'
    elif anionName=='Phosphorus':
        anionName='Phosphide'
    elif anionName=='Silicon':
        anionName='Silicide'
    elif anionName=='Arsenic':
        anionName='Arsenide'
    elif anionName=='Tin':
        anionName='Stannide'
    elif anionName=='Antimony':
        anionName='Antimonide'
    elif anionName=='Tungsten':
        anionName='Tungstide'
    elif anionName=='Osmium':
        anionName='Osmide'
    elif anionName=='Iridium':
        anionName='Iridide'
    elif anionName=='Bismuth':
        anionName='Bismide'
    return firstHalf+anionName

def getOxidationNumber(n):
    if n==1:
        return '(I)'
    elif n==2:
        return '(II)'
    elif n==3:
        return '(III)'
    elif n==4:
        return '(IV)'
    elif n==5:
        return '(V)'
    elif n==6:
        return '(VI)'
    elif n==7:
        return '(VII)'
    elif n==8:
        return '(VIII)'
    elif n==9:
        return '(IX)'
    
def findMolarMass(atoms):
    mass=0
    for atom in atoms:
        mass+=atom.mass
    return mass
    
def findTotalValence(atoms):
    valence=0
    for atom in atoms:
        valence+=atom.valence
    return valence

def findIonicAttraction(atoms):
    k=2.31*(10**-19)
    q1=atoms[0].charge
    q2=atoms[-1].charge
    r=(atoms[0].size+atoms[-1].size)*2
    attraction=k*(q1*q2)/(r)*6.022*(10**23)
    return [attraction,r/2]
    
def formsHydrogenBonds(compound):
    if compound.formula=='FeC10H10' or compound.formula=='C8H8' or compound.formula=='C10H10':
        return 'No'
    for group in compound.groups:
        if (elementPicker('N')==group[0][0] or elementPicker('O')==group[0][0] or elementPicker('F')==group[0][0]) and elementPicker('H') in group[0]:
            return 'Yes'
    return 'No'

def getHybridizations(compound):
    if compound.formula=='C8H8':
        return ['sp3']*8
    elif compound.formula=='C10H10':
        return ['sp2']*10
    elif compound.formula=='FeC10H10':
        return [None]+['sp2']*10
    hybridizations=[]
    for group in compound.groups:
        steric=group[2]
        if steric==0:
            hybridizations.append('s')
        elif steric==2 or steric==1:
            hybridizations.append('sp')
        elif steric==3:
            hybridizations.append('sp2')
        elif steric==4:
            hybridizations.append('sp3')
        elif steric==5:
            hybridizations.append('dsp3')
        elif steric==6:
            hybridizations.append('d2sp3')
        elif steric==7:
            hybridizations.append('d3sp3')
        elif steric==8:
            hybridizations.append('d4sp4')
    return hybridizations