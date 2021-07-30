import numpy as np
import torch
import torch.nn.functional as functional
import torchvision.transforms as transforms

from pytorch_grad_cam import GradCAM, ScoreCAM, GradCAMPlusPlus
from pytorch_grad_cam.utils.image import show_cam_on_image

model_path = 'model\\'

MODELS = {
    'inceptionv3': model_path + 'inceptionv3_1.pth',
    'resnet18': model_path + 'resnet18_1.pth',
    'resnext50': model_path + 'resnext50_1.pth',
    'resnext50_bn': model_path + 'resnext50-1_1.pth',
    'inceptionv3_bn': model_path + 'inceptionv3-1_1.pth',
    'resnet18_bn': model_path + 'resnet18-1_1.pth'
}

CLASS_NAMES = ['CNV', 'DME', 'DRUSEN', 'NORMAL']
CLASS_DESCS = [
    'Choroidal Neovascularization(wetAMD)',
    'Diabetic Macular Edema',
    'Drusen(dryAMD)',
    'Normal Retina'
]


def transform_image(image, model):
    mean = [0.224, 0.224, 0.224]
    std = [0.1551, 0.1551, 0.1551]

    input_size = 299 if model in ['', 'inceptionv3', 'inceptionv3_bn', None] else 224
    ###input_size = 496

    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Resize((input_size, input_size)),
        transforms.Normalize(mean, std)
    ])

    return transform(image)


def load_model(model):
    if model is None or model == '':
        model = 'inceptionv3_bn'

    return torch.load(MODELS[model])['model']


def predict_image(model, image):
    model = model.cuda()
    model.eval()

    image = image.unsqueeze(0)
    image = image.cuda()

    with torch.no_grad():
        outputs = model(image)
        _, pred = torch.max(outputs, 1)

        prob_class = functional.softmax(outputs, dim=1)
        prob_class = prob_class.cpu().numpy()[0]

    probabilities = []
    for i in range(0, len(prob_class)):
        probabilities.append(round(float(prob_class[i].item()) * 100, 2))

    torch.cuda.empty_cache()

    return CLASS_DESCS[pred], CLASS_NAMES[pred], probabilities


def stream_image(image):
    image = image.numpy().transpose((1, 2, 0))
    image = np.clip(image, 0, 1)

    return image
