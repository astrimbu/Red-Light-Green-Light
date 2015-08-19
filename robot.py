from rrb2 import*
import time
import picamera
import picamera.array

rr = RRB2()

def takePhoto():
  ''' Collect RGB data, return color hit '''

  with picamera.PiCamera() as camera:
    camera.led = False
    with picamera.array.PiRGBArray(camera) as output:
      camera.resolution = (50, 50)
      camera.capture(output, 'rgb')

      if (output.array[25,25,0] >= 220): return 'red'
      elif (output.array[25,25,1] >= 220): return 'green'
      elif (output.array[25,25,2] >= 220): return 'blue'

    return 'none'

def main():
  while True:
    color = takePhoto()
    if (color == 'green'):
      rr.forward()
    elif (color == 'red'):
      rr.set_motors(0, 0, 0, 0)
    elif (color == 'blue'):
      rr.set_motors(0.5, 1, 0.5, 1)

if __name__ == '__main__':
  main()
