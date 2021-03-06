"""
some networks

"""
import torch.nn as nn
import torch.nn.functional as F

# TODO better network(cnn and lstm)

class vggish_bn(nn.Module):
    def __init__(self):
        super(vggish_bn, self).__init__()

        # convolution block 1
        self.conv1_1 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=(3, 3), padding=1)
        self.bn1_1 = nn.BatchNorm2d(32)
        self.conv1_2 = nn.Conv2d(in_channels=32, out_channels=32, kernel_size=(3, 3), padding=1)
        self.bn1_2 = nn.BatchNorm2d(32)
        self.pool1_1 = nn.MaxPool2d(kernel_size=(2, 2))

        # convolution block 2
        self.conv2_1 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(3, 3), padding=1)
        self.bn2_1 = nn.BatchNorm2d(64)
        self.conv2_2 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=(3, 3), padding=1)
        self.bn2_2 = nn.BatchNorm2d(64)
        self.pool2_1 = nn.MaxPool2d(kernel_size=(2, 2))

        # convolution block 3
        self.conv3_1 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=(3, 3), padding=1)
        self.bn3_1 = nn.BatchNorm2d(128)
        self.conv3_2 = nn.Conv2d(in_channels=128, out_channels=128, kernel_size=(3, 3), padding=1)
        self.bn3_2 = nn.BatchNorm2d(128)
        self.pool3_1 = nn.MaxPool2d(kernel_size=(2, 2))

        # convolution block 4
        self.conv4_1 = nn.Conv2d(in_channels=128, out_channels=256, kernel_size=(3, 3), padding=1)
        self.bn4_1 = nn.BatchNorm2d(256)
        self.conv4_2 = nn.Conv2d(in_channels=256, out_channels=256, kernel_size=(3, 3), padding=1)
        self.bn4_2 = nn.BatchNorm2d(256)
        self.pool4_1 = nn.MaxPool2d(kernel_size=(2, 2))

        # full connect layer
        self.global_pool = nn.AvgPool2d(kernel_size=(2, 31))
        self.fc1 = nn.Linear(256, 10)
        # self.fc2 = nn.Linear(1024, 512)
        # self.fc3 = nn.Linear(512, 10)

    def forward(self, x):
        # block 1
        x = self.conv1_1(x)
        x = self.bn1_1(x)
        x = F.relu(x)
        x = self.conv1_2(x)
        x = self.bn1_2(x)
        x = F.relu(x)
        x = self.pool1_1(x)

        # block 2
        x = self.conv2_1(x)
        x = self.bn2_1(x)
        x = F.relu(x)
        x = self.conv2_2(x)
        x = self.bn2_2(x)
        x = F.relu(x)
        x = self.pool2_1(x)

        # block 3
        x = self.conv3_1(x)
        x = self.bn3_1(x)
        x = F.relu(x)
        x = self.conv3_2(x)
        x = self.bn3_2(x)
        x = F.relu(x)
        x = self.pool3_1(x)

        # block 4
        x = self.conv4_1(x)
        x = self.bn4_1(x)
        x = F.relu(x)
        x = self.conv4_2(x)
        x = self.bn4_2(x)
        x = F.relu(x)
        x = self.pool4_1(x)

        # global Max pool
        x = self.global_pool(x)

        # full connect layer
        x = x.view(-1, 256)
        # x = F.relu(self.fc1(x))
        # x = F.relu(self.fc2(x))
        x = self.fc1(x)
        return x


class embedding_net_shallow(nn.Module):
    def __init__(self):
        super(embedding_net_shallow, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=(5, 5), padding=2)
        self.pool1 = nn.MaxPool2d(kernel_size=(2, 2))
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(5, 5), padding=2)
        self.pool2 = nn.MaxPool2d(kernel_size=(2, 2))
        self.conv3 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=(3, 3), padding=1)
        self.pool3 = nn.MaxPool2d(kernel_size=(10, 125))


        self.fc1 = nn.Linear(128, 32)
        self.fc2 = nn.Linear(32, 2)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.pool1(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = self.pool2(x)
        x = self.conv3(x)
        x = F.relu(x)
        x = self.pool3(x)
        x = x.view(-1, 128)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        return x

    def get_embeddings(self, x):
        return self.forward(x)


class embedding_net(nn.Module):
    def __init__(self):
        super(embedding_net, self).__init__()

        # convolution block 1
        self.conv1_1 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=(3, 3), padding=1)
        self.bn1_1 = nn.BatchNorm2d(32)
        self.conv1_2 = nn.Conv2d(in_channels=32, out_channels=32, kernel_size=(3, 3), padding=1)
        self.bn1_2 = nn.BatchNorm2d(32)
        self.pool1_1 = nn.MaxPool2d(kernel_size=(2, 2))

        # convolution block 2
        self.conv2_1 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(3, 3), padding=1)
        self.bn2_1 = nn.BatchNorm2d(64)
        self.conv2_2 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=(3, 3), padding=1)
        self.bn2_2 = nn.BatchNorm2d(64)
        self.pool2_1 = nn.MaxPool2d(kernel_size=(2, 2))

        # convolution block 3
        self.conv3_1 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=(3, 3), padding=1)
        self.bn3_1 = nn.BatchNorm2d(128)
        self.conv3_2 = nn.Conv2d(in_channels=128, out_channels=128, kernel_size=(3, 3), padding=1)
        self.bn3_2 = nn.BatchNorm2d(128)
        self.pool3_1 = nn.MaxPool2d(kernel_size=(2, 2))

        # convolution block 4
        self.conv4_1 = nn.Conv2d(in_channels=128, out_channels=256, kernel_size=(3, 3), padding=1)
        self.bn4_1 = nn.BatchNorm2d(256)
        self.conv4_2 = nn.Conv2d(in_channels=256, out_channels=256, kernel_size=(3, 3), padding=1)
        self.bn4_2 = nn.BatchNorm2d(256)
        self.pool4_1 = nn.MaxPool2d(kernel_size=(2, 2))

        # full connect layer
        self.global_pool = nn.AvgPool2d(kernel_size=(2, 31))
        self.fc1 = nn.Linear(256, 64)
        self.fc2 = nn.Linear(64, 2)
        # self.fc2 = nn.Linear(1024, 512)
        # self.fc3 = nn.Linear(512, 10)

    def forward(self, x):
        # block 1
        x = self.conv1_1(x)
        x = self.bn1_1(x)
        x = F.relu(x)
        x = self.conv1_2(x)
        x = self.bn1_2(x)
        x = F.relu(x)
        x = self.pool1_1(x)

        # block 2
        x = self.conv2_1(x)
        x = self.bn2_1(x)
        x = F.relu(x)
        x = self.conv2_2(x)
        x = self.bn2_2(x)
        x = F.relu(x)
        x = self.pool2_1(x)

        # block 3
        x = self.conv3_1(x)
        x = self.bn3_1(x)
        x = F.relu(x)
        x = self.conv3_2(x)
        x = self.bn3_2(x)
        x = F.relu(x)
        x = self.pool3_1(x)

        # block 4
        x = self.conv4_1(x)
        x = self.bn4_1(x)
        x = F.relu(x)
        x = self.conv4_2(x)
        x = self.bn4_2(x)
        x = F.relu(x)
        x = self.pool4_1(x)

        # global Max pool
        x = self.global_pool(x)

        # full connect layer
        x = x.view(-1, 256)
        # x = F.relu(self.fc1(x))
        # x = F.relu(self.fc2(x))
        x = self.fc1(x)
        x = self.fc2(x)
        return x

    def get_embeddings(self, x):
        return self.forward(x)


