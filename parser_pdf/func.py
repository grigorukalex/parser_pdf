import cv2


# Вырезаем bbox из изображения
def cut_bbox_from_img(path_img, bbox):
    """
    :param path_img: путь к изображению
    :param bbox: bbox {'left':0.1, 'right':0.8, 'top':0.2, 'bottom':0.5) для изображения
        в относительных значениях (от 0 до 1)
    :return: вырезанное изображение
    """
    # Открываем изображение текущей страницы PDF
    img = cv2.imread(path_img)
    # Определяем размеры изображения
    width, height = img.shape[1], img.shape[0]

    # Переводим относительные (0-1) в абсолютные координаты
    left = int(bbox['left'] * width)
    top = int(bbox['top'] * height)
    right = int(bbox['right'] * width)
    bottom = int(bbox['bottom'] * height)

    # Вырезаем bbox из изображения
    img_bbox = img[top:bottom, left:right]

    return img_bbox
