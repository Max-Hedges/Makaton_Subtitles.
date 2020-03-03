def main():
    import csv
    import pyglet
    import time
    WordFile = open("example_test_B99.txt","r")


    def outputGif(inputgif):
        animation = pyglet.resource.animation(inputgif)
        sprite = pyglet.sprite.Sprite(animation)
        window = pyglet.window.Window(width=sprite.width, height=sprite.height)
        back = 0, 0, 0, 0.5
        pyglet.gl.glClearColor(*back)
        @window.event
        def on_draw():
            window.clear()
            sprite.draw()
        def close(event):
            window.close()
        pyglet.clock.schedule_once(close, 1.0)
        pyglet.app.run()









    punctuation = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
    wordsList = []
    wordsline = []
    for line in WordFile:
        line = line.split()
        for word in line:
            outLine = ''
            for char in word:
                if char not in punctuation:
                    outLine = outLine+char.upper()

            wordsline.append(outLine)
        wordsList.append(wordsline)
        wordsline=[]

    GifList = []
    with open("TextToGif.csv") as csv_file:
        csvRead = csv.reader(csv_file, delimiter=",")
        lineCount = 0
        for line in csvRead:
            readline = [line[0],line[1]]
            GifList.append(readline)


    for wordline in wordsList:
        for worditem in wordline:
            for line in GifList:
                if worditem == line[0]:
                    outputGif(line[1])
