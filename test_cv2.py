import cv2


# Отображение изображения
def cv2_show(name, img):
    cv2.imshow(name, img)  # Для компа
    # cv2_imshow(img)  # Для колаба
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image = cv2.imread("examples/parser_pdf/db/i1.jpg")
# cv2.rectangle(image, (10, 10), (596, 842), (0, 255, 0), 2)  # Рисуем найденный контур
width, height = image.shape[1], image.shape[0]

print(width, height )
cv2_show("Image", image)
