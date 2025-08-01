
## 🔬 Summary

Conv model took half the memory and had double the accuracy. With 60,000 training data, our Conv achieved 95% accuracy while traditional Deep Learning Neural Network only achieved 45%. In Conv, it learns the 'edges' and 'shapes' of the image by creating and running a filter through the image (we used a 3x3 pixel filter, or a kernal). Without such features implemented, traditional Deep Learning models would permanently suffer from model deviations in many cases.

In 2025, in using LLM models we can sometimes heuristically experience the model is giving a low accuracy output against our original intentions. And yet, human communication is not perfect (We often only insinuate what our true intentions are. We barely speak those out of time contraint, etc. So LLM models do not know.) And LLM can only see our written input, so far at least.

What would be the next challenge for the Artificial Neural Network Journey? Maybe a model that can analyze what it is missing in context (semantics) and then asks questions!



## 🔬 Technical Specifications

- **Framework**: TensorFlow 2.x with Keras
- **Frontend**: Streamlit for rapid prototyping
- **Image Processing**: PIL for seamless image handling
- **Visualization**: Matplotlib for stunning charts
- **Model Format**: HDF5 for efficient storage

## 🎲 The 10 Objects Our AI Recognizes

Our neural network has been trained to identify these fascinating categories:
- ✈️ **Airplane** 
- 🚗 **Automobile** 
- 🐦 **Bird** 
- 🐱 **Cat** 
- 🦌 **Deer**
- 🐕 **Dog** 
- 🐸 **Frog** 
- 🐴 **Horse** 
- 🚢 **Ship**
- 🚛 **Truck**


### Architecture Deep Dive
Our neural network features:
- **Input Layer**: 32×32×3 RGB images (flattened to 3,072 features)
- **Hidden Layer**: 1,000 neurons with ReLU activation
- **Output Layer**: 10 neurons with softmax activation
- **Optimizer**: Adam (adaptive learning rate)
- **Loss Function**: Categorical crossentropy

## 🌟 What's Next?

This project is just the beginning! Consider these exciting enhancements:
- Implement convolutional layers for better accuracy
- Add support for custom object categories
- Create a mobile-friendly version
- Add real-time webcam classification
- Include model performance metrics

## 🤝 Contributing

We love contributions! Whether it's bug fixes, feature additions, or documentation improvements, your input makes this project better for everyone.

## 📄 License

This project is open source and available under the MIT License.

