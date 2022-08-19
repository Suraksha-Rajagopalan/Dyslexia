from tkinter import Image
import streamlit as st
from PIL import Image
import pickle as pkl
from feature_extractor import get_feature_array

model = pkl.load(open("Decision_tree_model.sav", 'rb'))

st.title("Dyslexia Detection Using Handwriting Samples")
st.write("This is a simple web app that works based on machine learning techniques. This application can predict the presence of dyslexia from the handwriting sample of a person.")
image = st.file_uploader("Upload the handwriting sample that you want to test", type=["png", "jpg", "jpeg"])

if image is not None:
    st.write("please review the image selected")
    st.write(image.name)
    image_uploaded = Image.open(image)
    image_uploaded.save("temp.jpg")
    st.image(image_uploaded, width=224)
    
    

if st.button("Predict", help="click after uploading the correct image"):
    try:
        feature_array = get_feature_array("temp.jpg")
        result = model.predict([feature_array])
        if result[0] == 0:
            st.write("from the tests on this handwriting sample there is very slim chance that this person is sufferning from dyslexia or dysgraphia")
        else:
            st.write("from the tests on this handwriting sample there is very high chance that this person is sufferning from dyslexia or dysgraphia")
    except:
        st.write("something went wrong at the server end please refresh the application and try again")
        
    
       
# def load_image(image):
#     image = Image.open(image)
#     kkpp = image.save("dolls.png")
#     return image


# def main():
#     st.title("File Upload Tutorial")

#     menu = ["Image"]
#     choice = st.sidebar.selectbox("Menu", menu)

#     if choice == "Image":
#         st.subheader("Image")

#     image = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])
#     if image is not None:

#         # To See details
#         file_details = {"filename": image.name, "filetype": image.type,
#                         "filesize": image.size}
#         st.write(file_details)

# # To View Uploaded Image
#         st.image(load_image(image), width=224)

#         model = load_model('model_saved.h5')

#         img = load_img(r"dolls.png", target_size=(224, 224))
#         img = np.array(img)

#         img = img/255
#         img = img.reshape(-1, 224, 224, 3)
#         label = (model.predict(img) < 0.4).astype(np.int32)

#         st.write(
#             "Predicted Class (0 - Non-dyslexia , 1- Dyslexia): ", label[0][0])
# main()