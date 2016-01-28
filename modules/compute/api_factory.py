class ComputeProcessorFac():
    processor = "aliyun"

    def __init__(self):
        if processor == "aliyun":
            return AliyunComputeProcessor()
