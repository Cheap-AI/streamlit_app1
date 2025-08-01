import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import tensorflow as tf

from PIL import Image

def display_readme():
    with open('README.md', 'r', encoding='utf-8') as file:
        readme_content = file.read()
    st.markdown(readme_content, unsafe_allow_html=True)

def main():
    st.title('Deep-NN VS. Conv-NN for Image Classification')
    
    # Add sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose a page", ["Home", "Doc"])
    
    if page == "Doc":
        display_readme()
    else:
        st.write('**Trained on 60,000 training data, you can observe the effectiveness of CNN on image classification task. The difference is fundamental as this architecture enables 2-D pattern searching (used 3x3 pixel slider in our case)**')
        st.write('You can upload an image to compare the accuracy of the models. One Sequential model with Dense layers (Flatten the image sequence) and another with Conv2D layers.')
        
        file = st.file_uploader("Test with an Image", type=["jpg", "jpeg", "png"])
        if file:
            image = Image.open(file)
            st.image(image, use_column_width=True)

            resized_image = image.resize((32, 32))
            img_array = np.array(resized_image) / 255
            img_array = img_array.reshape((1, 32, 32, 3))

            model = tf.keras.models.load_model('cifar10_model.h5')
            model2 = tf.keras.models.load_model('cifar10_model2.h5')
            
            prediction = model.predict(img_array)
            prediction2 = model2.predict(img_array)
            cifar10_classes = ['airplane', 'automobile', 'bird', 'cat', 'deer',
                               'dog', 'frog', 'horse', 'ship', 'truck']
            
            # Create two columns for side-by-side comparison
            col1, col2 = st.columns(2)
            
            with col1:
                fig1, ax1 = plt.subplots()
                y_pos = np.arange(len(cifar10_classes))
                ax1.barh(y_pos, prediction[0], align='center')
                ax1.set_yticks(y_pos)
                ax1.set_yticklabels(cifar10_classes)
                ax1.invert_yaxis()
                ax1.set_xlabel('Probability')
                ax1.set_title('Deep-NN Prediction')
                st.pyplot(fig1)
            
            with col2:
                fig2, ax2 = plt.subplots()
                y_pos = np.arange(len(cifar10_classes))
                ax2.barh(y_pos, prediction2[0], align='center')
                ax2.set_yticks(y_pos)
                ax2.set_yticklabels(cifar10_classes)
                ax2.invert_yaxis()
                ax2.set_xlabel('Probability')
                ax2.set_title('Conv-NN Prediction')
                st.pyplot(fig2)

            #predicted_class = cifar10_classes[np.argmax(prediction)]    
        else:
            st.text('You have not uploaded an image yet')
        
        # Add README content below the model testing section
        st.markdown("---")
        st.markdown("## Documentation")
        display_readme()

if __name__ == "__main__":
    
    main()