import streamlit as st

st.set_page_config(
    page_title="First App",
    page_icon="🤓",
)

st.write("# Команда YOLO 🤓")

st.write(
    """
    ### Разработка multipage-приложения с использованием streamlit

    В данной работе представлены:

    - Классификация произвольного изображения с помощью модели Xception (обученной на датасете ImageNet, использовали готовую модель из torchvision.models)
    - Классификация изображений котов и собак дообученной моделью ResNet18 (подгружаем предобученную часть из torchvision.models , заменили последний слой, заморозили все параметры кроме классификационного слоя)
    - Генерация заданной цифры с помощью Conditional GAN (на датасете MNIST)
    - Детекция объектов с помощью YOLO 5
    - Очищение документов от шумов с помощью автоэнкодера (данные взяты из датасета Denoising Dirty Documents)
    """
)