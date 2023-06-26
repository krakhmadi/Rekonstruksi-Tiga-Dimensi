import cv2
import numpy as np
import plotly.graph_objects as go

def process(heightmap_path, texture_path):
    print(texture_path)
    heightmap = cv2.imread(heightmap_path)
    texture = cv2.imread(texture_path)

    size_heightmap = heightmap.shape
    x = size_heightmap[1]/2 - size_heightmap[1] / 4
    y = size_heightmap[0]/2 - size_heightmap[0] / 2
    crop_heightmap = heightmap[int(y):int(y + size_heightmap[0]), int(x):int(x + (size_heightmap[1] / 2))]

    size_texture = texture.shape
    x2 = size_texture[1] / 2 - size_texture[1] / 4
    y2 = size_texture[0] / 2 - size_texture[0] / 2
    crop_texture = texture[int(y2):int(y2 + size_texture[0]), int(x2):int(x2 + (size_texture[1] / 2))]

    grayscale_heightmap = cv2.cvtColor(crop_heightmap, cv2.COLOR_BGR2GRAY)
    grayscale_texture = cv2.cvtColor(crop_texture, cv2.COLOR_BGR2GRAY)

    flip_heightmap = np.flipud(grayscale_heightmap)
    flip_texture = np.flipud(grayscale_texture)

    size_crop_heightmap = crop_heightmap.shape
    sizeX = size_crop_heightmap[1]
    sizeY = size_crop_heightmap[0]
    arrayX = list(range(1, sizeX))
    arrayY = list(range(1, sizeY))
    arrayZ = flip_heightmap
    overlay_texture = flip_texture

    fig = go.Figure(
        go.Surface(
            x=arrayX,
            y=arrayY,
            z=arrayZ,
            hidesurface=False,
            surfacecolor=overlay_texture,
            colorscale=[[0, 'rgb(0,0,0)'], [1, 'rgb(255,255,255)']],
            showscale=False
        )
    )

    fig.update_layout(

        scene={
            "xaxis": {"nticks": 10},
            "yaxis": {"nticks": 10},
            "zaxis": {"nticks": 10},
            # 'camera_eye': {"x": 0, "y": -1, "z": 0.5},


            # # Selatan
            # 'camera_eye': {"x": 0, "y": -0.5, "z": 0.02},
            # Utara
            # 'camera_eye': {"x": 0, "y": 0.5, "z": 0.02},
            # Timur
            # 'camera_eye': {"x": 0.5, "y": 0, "z": 0.02},
            # # Barat
            'camera_eye': {"x": -0.5, "y": 0, "z": 0.028},
            "aspectratio": {"x": 1, "y": 1, "z": 0.2}
        })

    html = fig.to_html()
    return html


