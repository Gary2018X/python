#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    :   2022/08/29 13:47:07
# @Author  :   Gary
# @Email   :   None
class LiftState:
    # 抽象状态类
    def open(self):
        pass

    def close(self):
        pass

    def run(self):
        pass

    def stop(self):
        pass


class OpenState(LiftState):
    # 具体状态类
    def open(self):
        print("OPEN:The door is opened...")
        return self

    def close(self):
        print("OPEN:The door start to close...")
        print("OPEN:The door is closed")
        return StopState()

    def run(self):
        print("OPEN:Run Forbidden.")
        return self

    def stop(self):
        print("OPEN:Stop Forbidden.")
        return self


class RunState(LiftState):
    # 具体状态类
    def open(self):
        print("RUN:Open Forbidden.")
        return self

    def close(self):
        print("RUN:Close Forbidden.")
        return self

    def run(self):
        print("RUN:The lift is running...")
        return self

    def stop(self):
        print("RUN:The lift start to stop...")
        print("RUN:The lift stopped...")
        return StopState()


class StopState(LiftState):
    # 具体状态类
    def open(self):
        print("STOP:The door is opening...")
        print("STOP:The door is opened...")
        return OpenState()

    def close(self):
        print("STOP:Close Forbidden")
        return self

    def run(self):
        print("STOP:The lift start to run...")
        return RunState()

    def stop(self):
        print("STOP:The lift is stopped.")
        return self


class Context:
    # 环境类
    lift_state = ""

    def getState(self):
        return self.lift_state

    def setState(self, lift_state):
        self.lift_state = lift_state

    def open(self):
        self.setState(self.lift_state.open())

    def close(self):
        self.setState(self.lift_state.close())

    def run(self):
        self.setState(self.lift_state.run())

    def stop(self):
        self.setState(self.lift_state.stop())


if __name__ == "__main__":
    ctx = Context()
    ctx.setState(StopState())
    ctx.open()
    ctx.run()
    ctx.close()
    ctx.run()
    ctx.stop()
