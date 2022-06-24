def handler(context, inputs):
    greeting = "Hello, {0}!".format(inputs["target"])
    print(inputs)

     outputs = {
      "flavor": "large"
    }
     
    return outputs
