
import cv2
import time
import math

p1 = 530
p2 = 300

xs = []
ys = []

video = cv2.VideoCapture("C:/Users/MARCO ANTONIO/Documents/Python/Projeto107/footvolleyball.mp4")
# Carregue o rastreador
tracker = cv2.TrackerCSRT_create()

# Leia o primeiro quadro do vídeo
success,img = video.read()

# Selecione a caixa delimitadora na imagem
bbox = cv2.selectROI("tracking",img,False)

# Inicialize o rastreador em img e na caixa delimitadora
tracker.init(img,bbox)

def goal_track(img, bbox):
    x, y,w, h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    c1 = x+int(w/2)
    c2 = y+int(h/2)
    cv2.circle(img,(c1,c2),2,(255,0,0),5)
    cv2.circle(img,(int(p1),int(p2)),2,(0,0,255),3)
    dist = math.sqrt(((c1-p1)**2)+((c2-p2)**2))
    print(dist)
    if dist <= 20:
        cv2.putText(img,"Cesta",(300,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
    xs.append(c1),
    ys.append(c2)
    for i in range(len(xs)-1):
        cv2.circle(img,(xs[i],ys[i]),2,(0,255,0),5)

def drawBox(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(0,255,0),3,1)
    cv2.putText(img,'rastreando',(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,255),2)
    
  


while True:
    check, img = video.read()   

    # Atualize o rastreador em img e na caixa delimitadora
    success, bbox = tracker.update(img)

    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img,"Errou",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

    goal_track(img,bbox)
    
    cv2.imshow("resultado", img)
            
    key = cv2.waitKey(25)
    if key == 32:
        print("Interrompido")
        break

video.release()
cv2.destroyALLwindows()