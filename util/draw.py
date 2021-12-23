from entity.Map import Map
from PIL import Image, ImageDraw
from random import randint


def Draw(gridMap: Map, paths: list, obstacles: list, filename='animated_trajectories'):
    """
    Auxiliary function that visualizes the enviromnet, the path and OPEN and CLOSED.
    """
    k = 20
    quality = 5
    hIm = gridMap._height * k
    wIm = gridMap._width * k
    maxlength = 0
    for path in paths:
        maxlength = max(maxlength, len(path))
    step = 0
    images = []
    colors = [(randint(0, 255), randint(0, 255), randint(0, 255)) for _ in range(len(paths))]
    while step < maxlength:
        for n in range(0, quality):
            im = Image.new('RGB', (wIm, hIm), color='white')
            draw = ImageDraw.Draw(im)
            for i in range(gridMap._height):
                for j in range(gridMap._width):
                    if len(gridMap._safe_intervals[i][j]) == 0:
                        draw.rectangle((j * k, i * k, (j + 1) * k - 1, (i + 1) * k - 1), fill=(70, 80, 80))
            for i in range(len(paths)):
                if len(paths[i]) <= step:
                    continue
                curNode = paths[i][min(len(paths[i]) - 1, step)]
                nextNode = paths[i][min(len(paths[i]) - 1, step + min(n, 1))]
                draw.ellipse((float(curNode.j + n * (nextNode.j - curNode.j) / quality + 0.2) * k,
                              float(curNode.i + n * (nextNode.i - curNode.i) / quality + 0.2) * k,
                              float(curNode.j + n * (nextNode.j - curNode.j) / quality + 0.8) * k - 1,
                              float(curNode.i + n * (nextNode.i - curNode.i) / quality + 0.8) * k - 1),
                             fill=colors[i], width=0)
            for i in range(len(obstacles)):
                curNode = obstacles[i][min(len(obstacles[i]) - 1, step)]
                nextNode = obstacles[i][min(len(obstacles[i]) - 1, step + min(n, 1))]
                draw.ellipse((float(curNode[1] + n * (nextNode[1] - curNode[1]) / quality + 0.2) * k,
                              float(curNode[0] + n * (nextNode[0] - curNode[0]) / quality + 0.2) * k,
                              float(curNode[1] + n * (nextNode[1] - curNode[1]) / quality + 0.8) * k - 1,
                              float(curNode[0] + n * (nextNode[0] - curNode[0]) / quality + 0.8) * k - 1),
                             fill=(50, 50, 50), width=0)
            images.append(im)
        step += 1
    images[0].save('./' + filename + '.gif', save_all=True, append_images=images[1:], optimize=False,
                   duration=750 / quality, loop=0)
