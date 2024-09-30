# Sparky - The Hardware Guru

Sparky is an interactive assistant designed to help users identify and understand various hardware and electronic components. By leveraging voice recognition and image processing, Sparky can respond to questions about tools and electronics, providing concise, layman-friendly explanations. Users can ask about specific tools or show components.

## Demo Video
[![Sparky Demo Video](https://img.youtube.com/vi/4DVWlnijJ0s/0.jpg)](https://youtu.be/4DVWlnijJ0s)

Click the image above or [this link](https://youtu.be/4DVWlnijJ0s) to watch the video.


## Features

- **Voice Recognition**: Users can ask questions about hardware tools.
- **Image Recognition**: Users can show images of components for identification.
- **Interactive Learning**: Sparky provides explanations and helps users understand different tools and electronics.

## Architecture

Sparky is built using a Raspberry Pi as the central hub. It integrates:
- A microphone for voice input
- A speaker for audio output
- A camera for image recognition

The system employs software algorithms for processing voice commands and analyzing images of hardware items. All components are housed in a custom 3D-printed model, giving Sparky a unique and engaging design.

### Main Files
- `hardwareguru.py`: The main assistant that answers user questions.
- `toolidentify.py`: Contains computer vision code to detect tools in the scene.
  
### Component Files
- **6 Additional Files**: These include reference files for checking different hardware and assisting in the debugging process.

## Technology Used

- **Computer Vision**: The bot uses a custom-trained model to detect six classes of tools: `hammer`, `pliers`, `screwdriver`, `wrench`, `ESP_32`, and `Raspberry Pi`.
- **Model Training**: The model is trained using YOLOv8, achieving an accuracy of approximately mAP50 of 82% and mAP50-95 of 67%. This allows the bot to recognize tools effectively.
- **Gemini API**: Ensure that a Gemini API key is generated for interaction sessions with the chatbot.

## Challenges

While developing Sparky, we encountered several challenges:
- **Dataset Collection**: Gathering an appropriate dataset for the custom training model using YOLO was difficult. Achieving satisfactory accuracy required multiple training sessions.
- **Interactivity**: Ensuring the system communicated effectively within a domain-specific context was complex.
- **Integration**: Combining various components and deploying the system on hardware added further complications, especially given our limited timeframe.

## Accomplishments

We are proud to have successfully assembled an assistant that effectively responds to user inquiries and provides live detection of tools, along with accurate summaries. Achieving an accuracy rate of around 80% across six different classes is a significant milestone for us. This accomplishment showcases our ability to blend technology and user experience, allowing Sparky to serve as a reliable assistant in the realm of hardware and electronics.

<table>
  <tr>
    <td colspan=2><div align=center><img width=500px height=600px src="https://github.com/user-attachments/assets/451ef13f-0acb-4238-85c5-c541d2825a2e"></div></td>
  </tr>
  <tr>
    <td> <img width=500px height=500px src="https://github.com/user-attachments/assets/e2f1b670-e3db-4045-9395-074e22366993"></td>
     <td> <img width=500px height=500px src="https://github.com/user-attachments/assets/31e85947-9eda-4634-9db9-1aab416bf79d"> </td>
  </tr>
</table>

## Results of Computer Vision Model:
<table>
  <tr>
    <th>Confusion Matrix</th>
    <td>F1-Curve</td>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/2063e7b4-df39-4e11-9731-e26b4c1b4b56">
    </td>
    <td>
      <img src="https://github.com/user-attachments/assets/81132716-aea1-4441-8951-a29c984c43c5">
    </td>
  </tr>
</table>

## What We Learned

We discovered creative methods to generate domain-specific content using generative AI and learned how to activate computer vision models directly within the chatbot.

## What's Next for Sparky - The Hardware Guru

Moving forward, we plan to enhance Sparky's capabilities by:
- Improving accuracy through the addition of more images and expanding the dataset.
- Enabling Sparky to recognize unknown tools by providing images for on-the-spot training.
- Refining the user interface on the website and integrating the computer vision model.
- Incorporating motors or servos into the hardware to enhance Sparky's aesthetic and functionality.

## Getting Started

To get started with Sparky, ensure you have the following:
1. **Raspberry Pi**: Set up with a microphone, speaker, and camera.
2. **Dependencies**: Install necessary libraries for speech recognition and computer vision.
3. **API Key**: Generate a Gemini API key to initiate interaction sessions.
