from pyscript import document

def szamit(event):
    szam=float (document.querySelector("#szam").value)
    
    szam2=float (document.querySelector("#szam2").value)
    
    muvelet=float (document.querySelector("#muvelet").value)
    document.querySelector("#eredmeny").innerText=""


def torol(event):
    document.querySelector("#szam").value=""
    document.querySelector("#szam2").value=""
    document.querySelector("#eredmeny").innerText=""
    document.querySelector("#muveletet").selectedIndex=0