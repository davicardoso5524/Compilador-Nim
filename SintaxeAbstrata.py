from abc import ABCMeta, abstractmethod

class Program(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor): pass

class SingleProgram(Program):
    def __init__(self, stm):
        self.stm = stm
    def accept(self, visitor):
        return visitor.visitSingleProgram(self)

class CompoundProgram(Program):
    def __init__(self, stm, program):
        self.stm = stm
        self.program = program
    def accept(self, visitor):
        return visitor.visitCompoundProgram(self)

class Stm(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor): pass

class ProcStm(Stm):
    def __init__(self, id, sigParams, stms):
        self.id = id
        self.sigParams = sigParams
        self.stms = stms
    def accept(self, visitor):
        return visitor.visitProcStm(self)

class VarStm(Stm):
    def __init__(self, id, type=None, exp=None):
        self.id = id
        self.type = type
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitVarStm(self)

class IfStm(Stm):
    def __init__(self, exp, stms):
        self.exp = exp
        self.stms = stms
    def accept(self, visitor):
        return visitor.visitIfStm(self)

class WhileStm(Stm):
    def __init__(self, exp, stms):
        self.exp = exp
        self.stms = stms
    def accept(self, visitor):
        return visitor.visitWhileStm(self)

class ForStm(Stm):
    def __init__(self, id, exp, stms):
        self.id = id
        self.exp = exp
        self.stms = stms
    def accept(self, visitor):
        return visitor.visitForStm(self)

class ReturnStm(Stm):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitReturnStm(self)

class ImportStm(Stm):
    def __init__(self, ids):
        self.ids = ids
    def accept(self, visitor):
        return visitor.visitImportStm(self)

class ExpStm(Stm):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitExpStm(self)

class EchoStm(Stm):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitEchoStm(self)

class SigParams(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor): pass

class SingleSigParams(SigParams):
    def __init__(self, param):
        self.param = param
    def accept(self, visitor):
        return visitor.visitSingleSigParams(self)

class CompoundSigParams(SigParams):
    def __init__(self, param, sigParams):
        self.param = param
        self.sigParams = sigParams
    def accept(self, visitor):
        return visitor.visitCompoundSigParams(self)

class EmptySigParams(SigParams):
    def accept(self, visitor):
        return visitor.visitEmptySigParams(self)

class Param(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor): pass

class ParamConcrete(Param):
    def __init__(self, id, type):
        self.id = id
        self.type = type
    def accept(self, visitor):
        return visitor.visitParamConcrete(self)

class Stms(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor): pass

class SingleStms(Stms):
    def __init__(self, stm):
        self.stm = stm
    def accept(self, visitor):
        return visitor.visitSingleStms(self)

class CompoundStms(Stms):
    def __init__(self, stm, stms):
        self.stm = stm
        self.stms = stms
    def accept(self, visitor):
        return visitor.visitCompoundStms(self)

class Exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor): pass

class BinOpExp(Exp):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    def accept(self, visitor):
        return visitor.visitBinOpExp(self)

class CallExp(Exp):
    def __init__(self, call):
        self.call = call
    def accept(self, visitor):
        return visitor.visitCallExp(self)

class AssignExp(Exp):
    def __init__(self, id, exp):
        self.id = id
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitAssignExp(self)

class NumExp(Exp):
    def __init__(self, value):
        self.value = value
    def accept(self, visitor):
        return visitor.visitNumExp(self)

class IdExp(Exp):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitIdExp(self)

class Call(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor): pass

class ParamsCall(Call):
    def __init__(self, id, params):
        self.id = id
        self.params = params
    def accept(self, visitor):
        return visitor.visitParamsCall(self)

class NoParamsCall(Call):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitNoParamsCall(self)

class Params(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor): pass

class SingleParam(Params):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitSingleParam(self)

class CompoundParams(Params):
    def __init__(self, exp, params):
        self.exp = exp
        self.params = params
    def accept(self, visitor):
        return visitor.visitCompoundParams(self)
