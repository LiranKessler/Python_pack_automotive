# This tutorial is from: https://www.youtube.com/watch?v=EMXfZB8FVUA&list=PLqnslRFeH2UrcDBWF5mfPGpqQDSta6VK4&index=2
import torch

if __name__ == '__main__':
    torch.manual_seed(0)
    # Tutorial 2: getting know torch package, creating tensors (ones, zero, random etc..)
    # x = torch.zeros(2, 3)
    # print(x.size())

    # Tutorial 3: gradient calculation with autograd
    """"Calculating backpropagation example"""
    x = torch.randn(3, requires_grad=True)
    print(x)

    y = x+2
    print(y)
    z = y*y*2
    print(z)

    v = torch.tensor([0.1, 1.0, 0.001], dtype=torch.float32)
    z.backward(v)
    print(x.grad)

    """"Canceling grad"""
    x = torch.randn(3, requires_grad=True)
    # x.requires_grad_(False) / x.detach_() / with torch.no_grad():

    # Training example
    weights = torch.ones(4, requires_grad=True)

    for epoch in range(3):
        model_output = (weights*3).sum()
        model_output.backward()
        print(weights.grad)
        weights.grad.zero_()  # Very important!!! not to sum up the grads in each epoch

    # Backpropagation - good explanation of this concept!!!
    x = torch.tensor(1.0)
    y = torch.tensor(2.0)
    w = torch.tensor(1.0, requires_grad=True)

    # forward pass and compute the loss
    y_hat = w * x
    loss = (y_hat - y)**2

    print(loss)

    # backward pass
    loss.backward()
    print(w.grad)



