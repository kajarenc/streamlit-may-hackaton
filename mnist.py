import torch
from torchvision import datasets
import torchvision.transforms as transforms
import torch.nn as nn
import torch.nn.functional as F


# define the NN architecture
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # number of hidden nodes in each layer (512)
        hidden_1 = 512
        hidden_2 = 512
        # linear layer (784 -> hidden_1)
        self.fc1 = nn.Linear(28 * 28, hidden_1)
        # linear layer (n_hidden -> hidden_2)
        self.fc2 = nn.Linear(hidden_1, hidden_2)
        # linear layer (n_hidden -> 10)
        self.fc3 = nn.Linear(hidden_2, 10)
        # dropout layer (p=0.2)
        # dropout prevents overfitting of data
        self.dropout = nn.Dropout(0.2)

    def forward(self, x):
        # flatten image input
        x = x.view(-1, 28 * 28)
        # add hidden layer, with relu activation function
        x = F.relu(self.fc1(x))
        # add dropout layer
        x = self.dropout(x)
        # add hidden layer, with relu activation function
        x = F.relu(self.fc2(x))
        # add dropout layer
        x = self.dropout(x)
        # add output layer
        x = self.fc3(x)
        return x


# initialize the NN
model = Net()
num_workers = 0
batch_size = 10
transform = transforms.ToTensor()

model.load_state_dict(torch.load('model.pt'))
model.eval()

test_data = datasets.MNIST(root='data', train=False,
                           download=True, transform=transform)


def get_results():
    test_loader = torch.utils.data.DataLoader(test_data, batch_size=batch_size,
                                              num_workers=num_workers, shuffle=True)
    dataiter = iter(test_loader)
    images, labels = dataiter.next()
    output = model(images)

    _, preds = torch.max(output, 1)
    images = images.numpy()
    result = []
    for idx in range(batch_size):
        result.append({
            'image_np': images[idx],
            'prediction': int(preds[idx].item()),
            'label': int(labels[idx].item())
        })
    return result
