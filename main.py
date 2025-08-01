import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import tensorflow as tf

from PIL import Image

def main():
    st.title('Cifar10 Object Classifier')
    st.write('Upload any image to classify it into one of the 10 objects')
    
    file = st.file_uploader("Test with an Image", type=["jpg", "jpeg", "png"])
    if file:
        image = Image.open(file)
        st.image(image, use_column_width=True)

        resized_image = image.resize((32, 32))
        img_array = np.array(resized_image) / 255
        img_array = img_array.reshape((1, 32, 32, 3))

        model = tf.keras.models.load_model('cifar10_model.h5')


        prediction = model.predict(img_array)
        cifar10_classes = ['airplane', 'automobile', 'bird', 'cat', 'deer',
                           'dog', 'frog', 'horse', 'ship', 'truck']
        
        fig, ax = plt.subplots()
        y_pos = np.arange(len(cifar10_classes))
        ax.barh(y_pos, prediction[0], align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(cifar10_classes)
        ax.invert_yaxis()
        ax.set_xlabel('Probability')
        ax.set_title('Object Prediction')

        st.pyplot(fig)

        #predicted_class = cifar10_classes[np.argmax(prediction)]    
    else:
        st.text('You have not uploaded an image yet')

if __name__ == "__main__":
    
    main()