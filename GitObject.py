class GitObject(object):
    def __init__(self, data=None) -> None:
        if data is not None:
            self.deserialize(data)
        else:
            self.init()

    def serialize(self, repo):
        """
        This function MUST be implemented by subclasses.

        It must read the object's contents from self.data, a byte string,
        do whatever it takes to convert it into a meaningful repesentation.
        What exactly happens depends on each subclass.
        """

        raise Exception("Unimplemented")

    def deserialize(self, data):
        raise Exception("Unimplemented")

    def init(self):
        pass  # Just do nothing. Surprisingly a reasonable default !
