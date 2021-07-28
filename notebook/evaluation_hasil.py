import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms

from sklearn import metrics
from sklearn.preprocessing import label_binarize
import seaborn as sns
import matplotlib.pyplot as plt

import math
import os

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

model_path = 'D:\\Documents\\PENS\\PA\\model\\kaggleoutput\\randomresize\\resnet18_1.pth'
image_path = 'D:\\Documents\\PENS\\PA\\Dataset\\kermany2018\\OCT2017\\OCT2017\\'

input_size = 224

mean = [0.224, 0.224, 0.224]
std = [0.1551, 0.1551, 0.1551]

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize((input_size, input_size)),
    transforms.Normalize((mean), (std))
])

batch_size = 16
num_epoch = 10
CLASS_NAMES = list(os.listdir(image_path + '/train'))

def plot_train_acc_loss(output_models):
    plt.title('Training Accuracy')
    sns.lineplot(data=output_models['accuracy'])
    print('Train Accuracy : ', [round(data, 5) * 100 for data in output['accuracy']['train']])
    print('Val Accuracy : ', [round(data, 5) * 100 for data in output['accuracy']['val']])
    plt.show()

    plt.title('Training Loss')
    sns.lineplot(data=output_models['loss'])
    print('Train Loss : ', [round(data, 5) for data in output['loss']['train']])
    print('Val Loss : ', [round(data, 5) for data in output['loss']['val']])
    plt.show()

def test_model(output_models):
    test_dataset = torchvision.datasets.ImageFolder(os.path.join(image_path, 'test'), transform)
    data_loader = torch.utils.data.DataLoader(test_dataset, batch_size=batch_size, shuffle=True, num_workers=4)
    model = output_models['model']
    model = model.to(device)

    label_true, label_pred = [], []

    with torch.no_grad():
        for inputs, labels in data_loader:
            inputs, labels = inputs.to(device), labels.to(device)

            outputs = model(inputs)
            _, preds = torch.max(outputs, 1)

            label_true.extend(labels.detach().cpu().numpy())
            label_pred.extend(preds.detach().cpu().numpy())
    
    return label_true, label_pred

def evaluate_confusionmatrix(c_metrics):
    tp, fp, fn, tn = [], [], [], []
    sensitivity, specificity = [], []

    for i in range(0, len(CLASS_NAMES)):
        tp.append(c_metrics[i][i])
        fp.append(c_metrics.sum(axis=0)[i] - tp[i])
        fn.append(c_metrics.sum(axis=1)[i] - tp[i])
        tn.append(c_metrics.sum() - (tp[i] + fp[i] + fn[i]))
        sensitivity.append(tp[i] / (tp[i] + fn[i]))
        specificity.append(tn[i] / (tn[i] + fp[i]))

    accuracy = sum(tp) / c_metrics.sum()

    print('Test Accuracy : ', accuracy * 100)
    print('Sensitivity : ', [round(data, 5) * 100 for data in sensitivity])
    print('Specificity : ', [round(data, 5) * 100 for data in specificity])
    
    return {"accuracy": accuracy,
            "sensitivity": sensitivity,
            "specificity":specificity}


if __name__ == "__main__":
    output = torch.load(model_path)
    
    plot_train_acc_loss(output)
    label_true, label_pred = test_model(output)

    c_metrics = metrics.confusion_matrix(label_true, label_pred)

    plt.title('Confusion Matrix')
    sns.heatmap(c_metrics, 
        annot=True, 
        xticklabels=CLASS_NAMES, 
        yticklabels=CLASS_NAMES,
        cmap='Greens', 
        fmt='g'
    )
    plt.xlabel('Predicted Values')
    plt.ylabel('Actual Values')
    plt.show()
    
    evaluate_confusionmatrix(c_metrics)
    
    classification_report = metrics.classification_report(label_true, label_pred, digits=3)
    
    print(classification_report)