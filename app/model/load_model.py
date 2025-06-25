import onnxruntime as ort

session = ort.InferenceSession("app/model/model.onnx", providers=['CPUExecutionProvider'])