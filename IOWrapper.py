from io import StringIO 
import warnings
class IOWrapper():
    def __init__(self):
        self.inBuffer=""
        self.outBuffer=""
    def isEquals(self,o):
        if (self.inBuffer==o.inBuffer) and (self.outBuffer==o.outBuffer):
            return True
        else :
            return False
    def is_outBuffer_empty(self):
        return (not self.outBuffer)
    def print(self,*args, sep=' ', end='\n', file=None, flush=False):
        # Convert the arguments to strings and join them with the separator
        output = sep.join(map(str, args)) + end
        # If file is specified, write the output to the file
        if file is not None:
            file.write(output)
        if flush:
            file.flush()
        # concatenate output to buffer
        self.outBuffer+=output
    def input(self):
        warningText = "input() function called from IOWrapper.If you are a student,then you are probably making a mistake and not suppossed to take inputs like this, use the passed argument. Nothing will be returned as using this feature is not recommended. "
        warnings.warn(warningText, UserWarning)