from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import torch

class CLIPClassifier:
    def __init__(self):
        self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

    def classify(self, image_path, classes = ["street", "person"]):
        image = Image.open(image_path)

        inputs = self.processor(text= classes, images=image, return_tensors="pt", padding=True)

        outputs = self.model(**inputs)

        image_embeddings = outputs.image_embeds  # Use image_embeds instead of last_hidden_state

        logits_per_image = outputs.logits_per_image  # this is the image-text similarity score
        probs = logits_per_image.softmax(dim=1)

        result = {classes[i]: probs[0,i].item() for i in range(len(classes))}

        return result, image_embeddings.detach().numpy()
    
    def generate_embedding(self, image_path):
        image = Image.open(image_path)

        inputs = self.processor(images=image, return_tensors="pt", padding=True)

        # Check if 'input_ids' is in inputs, if not, add it
        if 'input_ids' not in inputs:
            inputs['input_ids'] = torch.tensor([[0]])  # Add dummy input_ids

        outputs = self.model(**inputs)

        embedding = outputs.image_embeds  # Use image_embeds instead of last_hidden_state

        return embedding.detach().numpy()
    def generate_text_embedding(self, text):
        # Tokenize and process the text
        inputs = self.processor(text=text, return_tensors="pt", padding=True)
        text_inputs = inputs.input_ids.to(self.model.device)

        # Use the text model component of CLIP for text embeddings
        with torch.no_grad():
            text_embedding = self.model.get_text_features(input_ids=text_inputs)

        return text_embedding.detach().numpy()