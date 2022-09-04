#Currently only works for inround screenshots of the stat board
#post game ss's are in a slightely different spot.
#Possible algorithmic way to find box?
#
import cv2
import pytesseract
import sys
mag = 2.1
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
pytesseract.charBlacklist=' '
filepath = sys.argv[1]
#filepath ="test.jpg"
img = cv2.imread(filepath,0)


img = cv2.rectangle(img, (250,900),(1650,210),(0,0,255),5)
crop_img = img[210:900, 250:1650].copy()


statf=open(filepath+"stats.txt","w")
players=[]
x=95
offset=45
for i in range(5):
    temp = crop_img[x:x+offset,215:400].copy()
    big = cv2.resize(temp, (0,0), fx=8, fy=4)
    #ret,msk = cv2.threshold(big,133,255,cv2.THRESH_BINARY)
    #ret,msk = cv2.threshold(big,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # Otsu's thresholding after Gaussian filtering
    blur = cv2.GaussianBlur(big,(5,5),0)
    ret,msk = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    msk=cv2.bitwise_not(msk)

        
    text=pytesseract.image_to_string(msk,config='--psm 10')
    text=''.join(text.split())
    for k in range(15-len(text)):
        text+=" "
    #print(text)
    players.append(text)
    #cv2.imshow("cropped", msk)
    #cv2.waitKey(1000)
    #cv2.destroyAllWindows()
    x+=55



x=100
offset=40

pkinfo=[]
#painfo=[]
pdinfo=[]
for i in range(5):
        
    kills = crop_img[x:x+offset,1040:1067].copy()
    bigk = cv2.resize(kills, (0,0), fx=mag, fy=mag)
    blurk = cv2.GaussianBlur(bigk,(5,5),0)
    ret,msk2 = cv2.threshold(blurk,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    msk2=cv2.bitwise_not(msk2)
    text=(pytesseract.image_to_string(msk2, lang='eng',config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'))
    #print(text,end =" ")
    #cv2.imshow("cropped", msk2)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    pkinfo.append(text)

    '''
        assists = crop_img[x:x+offset,1100:1180].copy()
        biga = cv2.resize(assists, (0,0), fx=1.5, fy=1.5)
        blura = cv2.GaussianBlur(biga,(5,5),0)
        ret,msk3 = cv2.threshold(blura,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        msk3=cv2.bitwise_not(msk3)
        text=(pytesseract.image_to_string(msk3, lang='eng',config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'))
        cv2.imshow("cropped", msk3)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
        print(text)
        painfo.append(text)
    '''

    deaths = crop_img[x:x+offset,1230:1300].copy()
    bigd = cv2.resize(deaths, (0,0), fx=mag, fy=mag)
    blurd = cv2.GaussianBlur(bigd,(5,5),0)
    ret,msk4 = cv2.threshold(blurd,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    msk4=cv2.bitwise_not(msk4)
    text=(pytesseract.image_to_string(msk4, lang='eng',config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'))
    #print(text+"\n")
    pdinfo.append(text)

        
    x+=55

for i in range(5):
    inf="?"
    if(pdinfo[i]!="0" and (pdinfo[i] != '' and pkinfo[i] != '')):
        inf=str(round(int(pkinfo[i])/int(pdinfo[i]),2))
    kd="n/a"
    if((pdinfo[i] != '' and pkinfo[i] != '')):
        kd=str(int(pkinfo[i])-int(pdinfo[i]))
    
    text=(players[i]+" "+ pkinfo[i]+" "+ pdinfo[i]+" K/D:"+inf+" +/-:"+kd+"\n")
    statf.write(text)
    print(text)
    #removed assists

statf.close()
print("done")
'''
print(pytesseract.image_to_string(temp))

temp = crop_img[145:200,215:900].copy()




'''


