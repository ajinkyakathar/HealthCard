{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "3e2b858d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import webbrowser\n",
    "# initalize the cam\n",
    "cap = cv2.VideoCapture(0)\n",
    "# initialize the cv2 QRCode detector\n",
    "detector = cv2.QRCodeDetector()\n",
    "while True:\n",
    "    _, img = cap.read()\n",
    "    # detect and decode\n",
    "    data, bbox, _ = detector.detectAndDecode(img)\n",
    "    # check if there is a QRCode in the image\n",
    "    if data:\n",
    "        a=data\n",
    "        break\n",
    "    # display the result\n",
    "    cv2.imshow(\"QRCODEscanner\", img)    \n",
    "    if cv2.waitKey(1) == ord(\"q\"):\n",
    "        break\n",
    "\n",
    "b=webbrowser.open(str(a))\n",
    "cap.release()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d31d1c64",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3e7a764f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
